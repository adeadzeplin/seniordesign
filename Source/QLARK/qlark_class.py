import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import pickle
import time

style.use("ggplot")

# from QLARK.qlark_cvs_interface import QlarkCircuitInterface
from QLARK.cvs_qlark_interface import QlarkCircuitInterface, CircuitStatus


def square(val):
    return val * val


class Qlark:
    def __init__(self,thread_ID,setupdict):
        self.thread_ID = thread_ID
        # AI constants
        self.EPISODE_NUM = 50000    # number of circuit Attempts
        self.EPS_DECAY = .9998  # Rate of random probability decay
        self.LEARNING_RATE = 0.1  # How much a q-value will change
        self.DISCOUNT = 0.95
        self.QRANDOMINIT = -1  # The range of random starting values
        self.EPSILONSTART = .7
        self.NUM_STEPS = setupdict['maxsteps'] # self.environment.ACTION_SPACE*3-6  # number of tries to complete a circuit
        # print(self.NUM_STEPS)
        self.DESIREDLOGIC = setupdict['truthtable']


        # AI Variables
        self.epsilon = self.EPSILONSTART  # probability of randomness. Goes down over time
        self.episode_rewards = []  # list of rewards for every episode
        self.success_flag = False
        self.showcase_flag = False
        self.success_counter = 0

        try:
            f = open(setupdict['savepath'], "rb")
            self.q_table = pickle.load(f)
            f.close()

        except:
            self.q_table = dict()



        # Space for AI to play and get feedback from
        self.environment = QlarkCircuitInterface(DESIRED_LOGIC=self.DESIREDLOGIC,
                                                 C_IN_CT=setupdict['circuitinputs'],
                                                 C_OUT_CT=setupdict['circuitoutputs'],
                                                 MAX_GATE_NUM=setupdict['maxgatenum'],
                                                 ALLOWED_GATE_TYPES=setupdict['allowedgatetypes'])


    def runBest(self):

        self.environment.reset_environment()
        for step in range(0, 20):

            # get state for q-table
            index_q = self.environment.get_state()
            action = np.argmax(self.q_table[index_q])
            # Update the environment and find out how it did
            reward = self.environment.attempt_action(action)
            # get future q
            new_index_q = self.environment.get_state()
            # Check If environment is in end state
            if step == self.NUM_STEPS - 1:
                print("runBest Failed")
                self.environment.breakcircuit()

            if self.environment.getcircuitstatus() == CircuitStatus.Valid:
                pass
            else:
                new_q = self.environment.getspecialreward()
                self.environment.parseLogic()
                break

    # def seetruth(self,desiredCircuit):
    #     self.DESIREDLOGIC = desiredCircuit

    # Train The AI on an Environment
    def train(self):
        self.epsilon = self.EPSILONSTART
        self.success_flag = False
        # Each episode is an attempt from nothing
        for episode in range(self.EPISODE_NUM):

            self.environment.reset_environment()
            episode_reward = 0

            # number of times the ai tries to add to the q table something
            for step in range(0, self.NUM_STEPS):
                # get state for q-table
                index_q = self.environment.get_state()
                # IF STATE DOESNT EXIST MAKE IT SO
                if index_q in self.q_table:
                    pass
                else:
                    self.q_table[index_q] = [np.random.uniform(self.QRANDOMINIT, 0) for i in range(self.environment.ACTION_SPACE)]

                # ACTION based on EPSILON GREEDY/REWARD
                if np.random.random() > self.epsilon:
                    action = np.argmax(self.q_table[index_q])
                else:
                    action = np.random.randint(len(self.q_table[index_q]))

                # Update the environment and find out how it did
                reward = self.environment.attempt_action(action)
                # get future q
                new_index_q = self.environment.get_state()

                # IF THE NEW STATE DOESNT EXIST MAKE IT SO
                if new_index_q in self.q_table:
                    pass
                else:
                    self.q_table[new_index_q] = [np.random.uniform(self.QRANDOMINIT, 0) for i in range(self.environment.ACTION_SPACE)]

                max_future_q = np.max(self.q_table[new_index_q])

                current_q = self.q_table[index_q][action]

                # Check If environment is in end state
                if step == self.NUM_STEPS - 1:
                    self.environment.breakcircuit()
                    # print("LIMIT REACHED")

                if self.environment.getcircuitstatus() == CircuitStatus.Valid:
                    new_q = (1 - self.LEARNING_RATE) * current_q + self.LEARNING_RATE * (reward.value + self.DISCOUNT * max_future_q)
                else:
                    new_q = self.environment.getspecialreward()

                self.q_table[index_q][action] = new_q
                episode_reward += new_q

                if self.environment.circuitstatus == CircuitStatus.Correct:
                    self.success_flag = True
                    self.success_counter += 1
                    self.environment.most_resent_successful_circuit = self.environment.list_of_gates
                    if self.showcase_flag:

                        return
                    # print(f"SUCCESS ON EPISODE: {episode}")
                    if episode % 5000 == 0 :
                        print(f"THREAD: {self.thread_ID} SUCCESS ON EPISODE: {episode}")
                        # self.environment.printout()

                    break
                elif self.environment.circuitstatus != CircuitStatus.Valid:
                    break

            self.episode_rewards.append(episode_reward)
            if episode < self.EPISODE_NUM:
                self.epsilon *= self.EPS_DECAY
            if episode % 5000 == 0:
                print(f"THREAD: {self.thread_ID} REMAINING EPISODES: {self.EPISODE_NUM - episode}")


            if self.epsilon < 0.00005:
                # self.epsilon = self.EPSILONSTART
                print(f"THREAD: {self.thread_ID} Cutting off Training set at {episode}")
                break

        # self.saveq()
        # self.environment.printout()
        # self.environment.parseLogic()
        #
        # self.showaiadata()

    # def saveq(self):
    #     # print("\nSAVING Q-table")
    #     pathname = f"qtable_thread{self.thread_ID}.pickle"
    #     with open(pathname, "wb") as f:  # every once in a while autosave just in case
    #         pickle.dump(self.q_table, f)
    #     # print("SAVING finished")



    def showaidata(self):

        GRAPH_GRANULARITY = 1000
        moving_avg = np.convolve(self.episode_rewards, np.ones((GRAPH_GRANULARITY,)) / GRAPH_GRANULARITY, mode='valid')

        plt.plot([i for i in range(len(moving_avg))], moving_avg)
        plt.ylabel(f"Reward {GRAPH_GRANULARITY}ma")
        plt.xlabel("episode #")
        plt.show()
        print(f"epsilon value: {self.epsilon}")







