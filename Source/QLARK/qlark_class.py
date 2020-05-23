import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import pickle
import time

style.use("ggplot")

from qlark_environment_class import BootLeg_Logic

def square(val):
    return val * val


class Qlark:
    def __init__(self):
        # AI constants
        self.EPISODE_NUM = 50000    # number of circuit Attempts
        self.EPS_DECAY = .9998  # Rate of random probability decay
        self.LEARNING_RATE = 0.1  # How much a q-value will change
        self.DISCOUNT = 0.95
        self.QRANDOMINIT = -5  # The range of random starting values
        self.EPSILONSTART = .7

        # AI Variables
        self.epsilon = self.EPSILONSTART  # probability of randomness. Goes down over time
        self.episode_rewards = []  # list of rewards for every episode

        try:
            with open("qtable.pickle", "rb") as f:
                self.q_table = pickle.load(f)
        except:
            self.q_table = dict()

        # Space for AI to play and get feedback from
        self.environment = BootLeg_Logic(C_IN_CT=2, C_OUT_CT=1, MAX_GATE_NUM=1, NUM_OF_GATE_TYPES=2)

        self.NUM_STEPS = 50#self.environment.ACTION_SPACE*3-6  # number of tries to complete a circuit
        print(self.NUM_STEPS)


    # Train The AI on an Environment
    def run(self):

        # Each episode is an attempt from nothing
        for episode in range(self.EPISODE_NUM):

            self.environment.reset()
            episode_reward = 0

            # number of times the ai tries to add to the q table something
            for step in range(0, self.NUM_STEPS):
                # get state for q-table
                index_q = self.new_q_table_state()
                # IF STATE DOESNT EXIST MAKE IT SO
                if index_q not in self.q_table:
                    self.q_table[index_q] = [np.random.uniform(self.QRANDOMINIT, 0) for i in range(self.environment.ACTION_SPACE)]

                # ACTION based on EPSILON GREEDY/REWARD
                if np.random.random() > self.epsilon:
                    action = np.argmax(self.q_table[index_q])
                else:
                    action = np.random.randint(len(self.q_table[index_q]))
                    # decay epsilon everytime it's used
                    # self.epsilon *= self.EPS_DECAY
                # Update the environment and find out how it did
                reward = self.environment.takeaction(action)
                # get future q
                new_index_q = self.new_q_table_state()

                # IF THE NEW STATE DOESNT EXIST MAKE IT SO
                if new_index_q not in self.q_table:
                    self.q_table[new_index_q] = [np.random.uniform(self.QRANDOMINIT, 0) for i in range(self.environment.ACTION_SPACE)]

                max_future_q = np.max(self.q_table[new_index_q])

                current_q = self.q_table[index_q][action]

                # Check If environment is in win state
                if self.environment.checkwin():
                    new_q = self.environment.getspecialreward(reward)
                else:
                    new_q = (1 - self.LEARNING_RATE) * current_q + self.LEARNING_RATE * (reward.value + self.DISCOUNT * max_future_q)

                self.q_table[index_q][action] = new_q
                episode_reward += new_q

                if self.environment.checkwin():
                    # print(f"SUCCESS ON EPISODE: {episode}")
                    if episode % 10000 == 0 or episode > self.EPISODE_NUM*.90:
                        print(f"SUCCESS ON EPISODE: {episode}")
                        self.environment.printout()
                    break
                elif self.environment.checklose(reward):
                    # print(step)
                    break
                    # pass
            # print(f"episode reward {episode_reward}")
            self.episode_rewards.append(episode_reward)
            if episode < self.EPISODE_NUM:
                self.epsilon *= self.EPS_DECAY
            if episode % 20000 == 0:
                print(f"REMAINING EPISODES: {self.EPISODE_NUM - episode}")
                self.saveq()

                pass
            if self.epsilon < 0.001:
                self.epsilon = self.EPSILONSTART
                print("Epsilon RESET")
            # self.environment.printout()
                pass
            if step == self.NUM_STEPS - 1:
                print("LIMIT REACHED")
        self.saveq()
        self.environment.printout()
        self.showaiadata()

    def saveq(self):
        print("\nSAVING Q-table")
        with open("qtable.pickle", "wb") as f:  # every once in a while autosave just in case
            pickle.dump(self.q_table, f)
        print("SAVING finished")

        # with open(f"qtable-{int(time.time())}.pickle", "wb") as f:
        #     pickle.dump(self.q_table, f)
        # with open("qtable_backup.pickle", "wb") as f:
        #     pickle.dump(self.q_table, f)

    def showaiadata(self):

        GRAPH_GRANULARITY = 100
        moving_avg = np.convolve(self.episode_rewards, np.ones((GRAPH_GRANULARITY,)) / GRAPH_GRANULARITY, mode='valid')

        plt.plot([i for i in range(len(moving_avg))], moving_avg)
        plt.ylabel(f"Reward {GRAPH_GRANULARITY}ma")
        plt.xlabel("episode #")
        plt.show()
        print(f"epsilon value: {self.epsilon}")


    def new_q_table_state(self):
        return self.environment.getstate()




