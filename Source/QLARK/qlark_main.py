import QLARK.qlark_threading as qt
import multiprocessing

def qlarklearn(desired_truthtable):
    Num_training_set_p_thread = 6  # Number of training sets of 10,000 per thread
    Number_of_threads = 4  # number of threads to instantiate
    qt.Needlethreading(Number_of_threads, desired_truthtable, Num_training_set_p_thread)

if __name__ == '__main__':

    desired_truthtable =  [[0,1,1,0],[0,0,0,1]] # Half Adder circuit Truth Table
    qlarklearn(desired_truthtable)
    # Num_training_set_p_thread = 5               # Number of training sets of 10,000 per thread
    # Number_of_threads = 2                       # number of threads to instantiate
    # qt.Needlethreading(Number_of_threads, desired_truthtable, Num_training_set_p_thread)
