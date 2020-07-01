import threading
import pickle
from QLARK.qlark_class import Qlark
import numpy as np

class QlarkThread(threading.Thread):
    threadIDcounter = 1

    def __init__(self, setupdict):
        super().__init__()
        self.id = QlarkThread.threadIDcounter
        QlarkThread.threadIDcounter +=1
        self.trainingsetnum = setupdict['trainingsetspthread']
        self.qtable = None
        self.success_flag = False
        self.success_counter = 0
        self.setupdict = setupdict

    def run(self):
        print(f"Starting Thread : {self.id}")
        self.Q_AI = self.TrainQlark()
        self.qtable = self.Q_AI.q_table
        self.success_flag = self.Q_AI.success_flag
        self.success_counter = self.Q_AI.success_counter
        print(f"Exiting Thread: {self.id}")

    def TrainQlark(self):
        Qlearningai = Qlark(self.id,self.setupdict)
        for i in range(self.trainingsetnum):
            print(f"Thread: {self.id} - Number of training sets remaining: {self.trainingsetnum-i}")
            Qlearningai.train()
            if Qlearningai.success_flag == True:
                print(f"THREAD: {self.id} QLARK SUCCESSFULLY LEARNED on set: {i}")
                break
        # Qlearingai.runBest()
        return Qlearningai



def saveqtable(q_table):
    print("\nSAVING Q-table")
    f = open("qtable.pickle", "wb")
    pickle.dump(q_table, f)
    f.close()


def Needlethreading(setupdict):
    qtablelist = []
    thread_list = []

    for i in range(setupdict['totalthreads']):
        tempthread = QlarkThread(setupdict)
        tempthread.start()
        thread_list.append(tempthread)
    for thread in thread_list:
        thread.join()
    print("Threads Should Be Finished now")
    # print(f"Qtablelist check: {qtablelist}")
    print("Averaging Q-tables Now")

    max_success = 0
    thread_winner_index = 0
    for i, thread in enumerate(thread_list):
        if thread.success_flag:
            if thread.success_counter >= max_success:
                max_success = thread.success_counter
                thread_winner_index = i
    if max_success == 0:
        thread_winner_index = np.random.randint(len(thread_list))
    print(f"max success count: {max_success}")
    print(f"thread winner id: {thread_list[thread_winner_index].id}")
    best_qtable = thread_list[thread_winner_index].qtable


    saveqtable(best_qtable)
    RunBestAI(setupdict)
    thread_list[thread_winner_index].Q_AI.showaidata()

def notthreading(setupdict):
    Qlearningai = Qlark(33, setupdict)
    for i in range(setupdict["trainingsetspthread"]):
        print(f'Number of training sets remaining: {setupdict["trainingsetspthread"] - i}')
        Qlearningai.train()
        if Qlearningai.success_flag == True:
            print(f"QLARK SUCCESSFULLY LEARNED on set: {i}")
            break

    saveqtable(Qlearningai.q_table)
    RunBestAI(setupdict)


def RunBestAI(setupdict):
    BestAI = Qlark("BESTPOSSIBLE",setupdict)
    BestAI.EPSILONSTART = .25
    BestAI.showcase_flag = True
    BestAI.train()
    BestAI.environment.parseLogic()
    BestAI.showaidata()



