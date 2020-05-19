
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
from dan_classes import *
from dan_functions import create_circuit_inputs,create_circuit_outputs,OutputOfAtoInputofB,RandomListIndex,checkciruitcompletion,totalports,INPUT_NUM,OUTPUT_NUM

import pprint
style.use("ggplot")

list_of_gates = []

def new_q_table_state(big_list):
    mini_index = []
    # https: // datascience.stackexchange.com / questions / 55785 / q - table - creation - and -update -
    # for -dynamic - action - space
    # # This state to state_id conversion should be a re-usable function
    # state_id = '/'.join([str(x) for x in state])
    # # Example state_id is '20/12/56/9/76/30'

    temp = []
    for i in big_list:
        temp.append(i.gate_id)
        temp.append(i.type.value)

        for x in i.inputs:
            temp.append(x._ID)
            temp.append(x.type.value)
            for n in x.mated_to:
                temp.append(n)

        for y in i.outputs:
            temp.append(y._ID)
            temp.append(y.type.value)
            for m in y.mated_to:
                temp.append(m)
        # mini_index.append(tuple(temp))
    state_id = '/'.join([str(x) for x in temp])
    return state_id


def reset_cirucit(gate_list):
    for i in range(len(gate_list)):
        gate_list.pop()
    Connector._id = 0
    Gate.gate_idcounter = 0


# print(temp)
# q_table[bruh] = [np.random.uniform(-5,0) for i in range(4)]
HM_EPISODES = 20000
NUM_STEPS = 100
EPS_SET = 0.5
epsilon = EPS_SET # randomness
EPS_DECAY = .9998
LEARNING_RATE = 0.1
DISCOUNT = 0.95


init_flag = True
MAXNUMOFGATES = 1
# maxarg = 4
episode_rewards = []
NUM_OF_GATE_OPTIONS = 1


def actionF(action,list):

    if action < NUM_OF_GATE_OPTIONS:
        if len(list)  < MAXNUMOFGATES + INPUT_NUM + OUTPUT_NUM:
            if action   == 0 :
                list.append(Gate(GateType.NAND))
                return GateCost.COST_NAND
            elif action == 1 :
                list.append(Gate(GateType.NOT))
                return GateCost.COST_NOT
            elif action == 3 :
                list.append(Gate(GateType.NOR))
                return GateCost.COST_NOR
            elif action == 4 :
                list.append(Gate(GateType.AND))
                return GateCost.COST_AND
            elif action == 5 :
                list.append(Gate(GateType.OR))
                return GateCost.COST_OR
            elif action == 6 :
                list.append(Gate(GateType.XOR))
                return GateCost.COST_XOR
            else:
                return GateCost.COST_ILEGAL
        else:
            return GateCost.COST_ILEGAL
    else:
        if  len(list) == MAXNUMOFGATES + INPUT_NUM + OUTPUT_NUM:
            action -= NUM_OF_GATE_OPTIONS
            mod = (action % (MAXNUMOFGATES + INPUT_NUM + OUTPUT_NUM))
            div = (action // (MAXNUMOFGATES + INPUT_NUM + OUTPUT_NUM))

            # print(action,div,mod)
            # if   mod >= len(list_of_gates):
            #     print(f"mod Too high {mod}")
            #     print(f"len(list_of_gates) {len(list_of_gates)}")
            # if div >= len(list_of_gates):
            #     print(f"div Too hig {div}")
            #     print(f"len(list_of_gates) {len(list_of_gates)}")
            # print(f"len(list_of_gates) {len(list_of_gates)}")

            return OutputOfAtoInputofB(list, div, mod)
        else:
            return GateCost.COST_ILEGAL




def square(val):
    return val * val

ACTION_SPACE = square(MAXNUMOFGATES + INPUT_NUM + OUTPUT_NUM)+NUM_OF_GATE_OPTIONS
from graphics import *



try:
    with open("qtable.pickle", "rb") as f:
        q_table = pickle.load(f)
except:
    q_table = dict()

# Each episode is an attempt from nothing
for episode in range(HM_EPISODES):
    reset_cirucit(list_of_gates)
    create_circuit_inputs(list_of_gates)
    create_circuit_outputs(list_of_gates)
    episode_reward = 0
    # number of times the ai tries something
    for i in range(0, NUM_STEPS):
        index_Q = new_q_table_state(list_of_gates)
        # IF STATE DOESNT EXIST MAKE IT SO
        if index_Q in q_table:
            pass
        else:
            q_table[index_Q] =  [np.random.uniform(-1, 0) for i in range(ACTION_SPACE)]
            # print(f"NEEEEEEEEEEEE{len(list_of_gates)}")
            # print(q_table[index_Q])

        # print(index_Q)
        # ACTION EPSILON GREEDY/REWARD
        if np.random.random() > epsilon:
            action = np.argmax(q_table[index_Q])
        else:
            action = np.random.randint(len(q_table[index_Q]))
        reward = actionF(action, list_of_gates)
        new_index_Q = new_q_table_state(list_of_gates)



        # IF STATE DOESNT EXIST MAKE IT SO
        if new_index_Q in q_table:
            pass
        else:
            # print(f"N))0000{# len(list_of_gates)}")
            q_table[new_index_Q] = [np.random.uniform(-1, 0) for i in range(ACTION_SPACE)]
            # print(q_table[new_index_Q])


        max_future_q = np.max(q_table[new_index_Q])
        current_q = q_table[index_Q][action]

        # Check If circuit is complete
        if checkciruitcompletion(list_of_gates):

            if len(list_of_gates) >= MAXNUMOFGATES + INPUT_NUM + OUTPUT_NUM:
                new_q = reward.value + GateCost.Cost_COMPLETE.value + GateCost.COST_CORRECT.value
                print(f"CIRCUIT GOOD ON EPISODE: {episode}")
                # for gate in list_of_gates:
                #     gate.g_print()
                # break

            else:
                new_q = reward.value + GateCost.Cost_COMPLETE.value + GateCost.COST_INCORRECT.value
        # elif reward == GateCost.COST_ILEGAL:
        #     new_q = reward.value

        else:

            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward.value + DISCOUNT * max_future_q)

        q_table[index_Q][action] = new_q
        episode_reward += new_q

        if checkciruitcompletion(list_of_gates):
            if len(list_of_gates) > 6:
                break
            print(f"completed circuit on EPISODE: {episode}")
            break
        elif reward == GateCost.COST_ILEGAL:
            break
            # pass
    # print(f"episode reward {episode_reward}")
    episode_rewards.append(episode_reward)
    if episode < HM_EPISODES:
        epsilon *= EPS_DECAY
    if epsilon < 0.0005:
        # exit()
        # epsilon = EPS_SET
        with open("qtable.pickle", "wb") as f:
            pickle.dump(q_table, f)
        print("EPSILON RESET")
    # for state in q_table:
    #     print(q_table[state])
for gate in list_of_gates:
    gate.g_print()

with open("qtable.pickle", "wb") as f:
    pickle.dump(q_table, f)
print(f"epsilon value: {epsilon}")
SHOW_EVERY = HM_EPISODES//10
moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,)) / SHOW_EVERY, mode='valid')

plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f"Reward {SHOW_EVERY}ma")
plt.xlabel("episode #")
plt.show()

print("print")
# episode_rewards.append(episode_reward)



