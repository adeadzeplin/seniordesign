import QLARK.qlark_threading as qt
# import multiprocessing
from CVS_.CVS_gate_class import GateType
from qlark_gui_class import getrootpath
def qlarklearn(setupdict):
    return qt.notthreading(setupdict)
    # qt.Needlethreading(setupdict)



if __name__ == '__main__':


    # for filename in os.listdir(ROOT_DIR):
    #     if filename.endswith('.pickle'):
    #         print(filename)


    initdict = {
        'truthtable': [[1, 0, 0, 1, 0, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 0]],  # Truthtable Full Adder
        'circuitinputs': 3,  #
        'circuitoutputs': 2,  #
        'maxgatenum': 6,  # Total num of gates AI is allowed to place
        'allowedgatetypes': [GateType.AND.name,  # For Qlark             please dont touch
                             GateType.XOR.name,  # For Qlark             please dont touch
                             GateType.OR.name],  # For Qlark             please dont touch
        'maxsteps': 15,  # For Qlark             please dont touch
        'totalthreads': 1,  # For Qlark threading   please dont touch
        'trainingsetspthread': 1,  # For Qlark threading   please dont touch
        'savepath': f'{getrootpath()}fulladder_qtable.pickle'
    }
    qlarklearn(initdict)
    # Num_training_set_p_thread = 5               # Number of training sets of 10,000 per thread
    # Number_of_threads = 2                       # number of threads to instantiate
    # qt.Needlethreading(Number_of_threads, desired_truthtable, Num_training_set_p_thread)
