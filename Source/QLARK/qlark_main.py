from QLARK.qlark_class import Qlark


if __name__ == '__main__':

    desired_truthtable =  [[0,1,1,0],[0,0,0,1]]

    Qlearingai = Qlark(desired_truthtable)
    Qlearingai.train()
    Qlearingai.runBest()
