from dan_classes import Gate, GateType, GateCost
import numpy as np
# number of circuit inputs/outputs
INPUT_NUM = 2
OUTPUT_NUM = 1


def create_circuit_inputs(mega_list):
    for i in range(INPUT_NUM):
        mega_list.append(Gate(GateType.CIRCUIT_INPUT, 0, 1))


def create_circuit_outputs(mega_list):
    for i in range(OUTPUT_NUM):
        mega_list.append(Gate(GateType.CIRCUIT_OUTPUT, 1, 0))


def OutputOfAtoInputofB(GateList, a, b):
    if a == b:
        return GateCost.COST_ILEGAL
    else:
        try:
            if GateList[a].type == GateType.CIRCUIT_INPUT or GateList[b].type == GateType.CIRCUIT_INPUT:
                if GateList[a].type == GateType.CIRCUIT_OUTPUT or GateList[b].type == GateType.CIRCUIT_OUTPUT:
                    return GateCost.COST_ILEGAL

            # only close if all the other circuits are closed
            # if GateList[b].type == GateType.CIRCUIT_OUTPUT:
            #     for gate in GateList:
            #         if gate.type == GateType.CIRCUIT_OUTPUT:
            #             pass
            #         elif len(gate.outputs)>0:
            #             return GateCost.COST_ILEGAL

            return GateList[a].connect_to_(GateList[b])
        except:
            return GateCost.COST_ILEGAL


def RandomListIndex(mylist):
    return np.random.randint(len(mylist))
def checkciruitcompletion(list):
    for gate in list:
        for port in gate.inputs:
            if len(port.mated_to) == 0:
                return False
        for port in gate.outputs:
            if len(port.mated_to) == 0:
                return False
    return True

def totalports(biglist):
    total_input_ports = 0
    total_output_ports = 0
    for i in biglist:
        for j in i.inputs:
            total_input_ports   += 1
        for k in i.outputs:
            total_output_ports  += 1
    return total_input_ports, total_output_ports


 # if action == 0:
    #     # if less than the gate limit
    #     if len(list) - 1 - 1 <= MAXNUMOFGATES:
    #         list.append(Gate(GateType.NAND))
    #         return GateCost.COST_NAND
    #     else:
    #         return GateCost.COST_ILEGAL
    # # elif action == 1:
    # #     return OutputOfAtoInputofB(list, 0, 2)
    # # elif action == 2:
    # #     return OutputOfAtoInputofB(list, 1, 2)
    # elif action == 1:
    #     return OutputOfAtoInputofB(list, 0, 3)
    # elif action == 2:
    #     return OutputOfAtoInputofB(list, 1, 3)
    # elif action == 3:
    #     return OutputOfAtoInputofB(list, 3, 2)
    # else:
    #     return GateCost.COST_ILEGAL