import QLARK.qlark_threading as qt
# import multiprocessing
from CVS_.CVS_gate_class import GateType

def qlarklearn(setupdict):
    return qt.notthreading(setupdict)
    # qt.Needlethreading(setupdict)

if __name__ == '__main__':
    initdict = {'truthtable': [[0,1,1,0],[0,0,0,1]],
                'circuitinputs': 2,
                'circuitoutputs': 2,
                'maxgatenum': 2,
                'allowedgatetypes': [GateType.AND.name, GateType.XOR.name],
                'maxsteps': 12,
                'totalthreads': 1,
                'trainingsetspthread':10

                     }
    qlarklearn(initdict)
    # Num_training_set_p_thread = 5               # Number of training sets of 10,000 per thread
    # Number_of_threads = 2                       # number of threads to instantiate
    # qt.Needlethreading(Number_of_threads, desired_truthtable, Num_training_set_p_thread)
