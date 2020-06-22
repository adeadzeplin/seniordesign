import QLARK.qlark_threading as qt
import multiprocessing

if __name__ == '__main__':

    desired_truthtable =  [[0,1,1,0],[0,0,0,1]] # Half Adder circuit Truth Table

    Num_training_set_p_thread = 1               # Number of training sets of 10,000 per thread
    Number_of_threads = 1                       # number of threads to instantiate
    qt.Needlethreading(Number_of_threads, desired_truthtable, Num_training_set_p_thread)
    # p = Process(target=qt.Needlethreading, args=(Number_of_threads,desired_truthtable,Num_training_set_p_thread,))
    # p.start()
    # p.join()
#     with Pool(processes=4) as pool:  # start 4 worker processes
#         result = pool.apply_async(qt.Needlethreading(), [10])  # evaluate "f(10)" asynchronously
#         print(result.get(timeout=1))  # prints "100" unless your computer is *very* slow
#         print(pool.map(f, range(10)))  # prints "[0, 1, 4,..., 81]"
#
# def multiprocess_handler(poolsize):
#     p = multiprocessing.Pool(poolsize)
#     p.map(mp_worker, data)