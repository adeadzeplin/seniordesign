import QLARK.qlark_threading as qt


if __name__ == '__main__':

    desired_truthtable =  [[0,1,1,0],[0,0,0,1]] # Half Adder circuit Truth Table

    Num_training_set_p_thread = 1               # Number of training sets of 10,000 per thread
    Number_of_threads = 4                       # number of threads to instantiate
    qt.Needlethreading(Number_of_threads, desired_truthtable, Num_training_set_p_thread)


