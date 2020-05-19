from Source.CVS_gate_class import Gate, GateType
from Source.CVS_constants import INPUTSTOTAL, OUTPUTSTOTAL

# Constants
#inputsTotal = INPUTSTOTAL
#outputsTotal = OUTPUTSTOTAL


def Output_to_Input(GateList, a, b):
    if a == b:
        return
    else:
        try:
            if GateList[a].type == GateType.circuitInput or GateList[b].type == GateType.circuitInput:
                if GateList[a].type == GateType.circuitOutput or GateList[b].type == GateType.circuitOutput:
                    print("asd")

            return GateList[a].gateConnect(GateList[b])
        except:
            return False



def create_circuit_inputs(mega_list):
    for i in range(INPUTSTOTAL):
        mega_list.append(Gate(GateType.circuitInput, 0, 1))  # making input circuit port


def create_circuit_outputs(mega_list):
    for i in range(OUTPUTSTOTAL):
        mega_list.append(Gate(GateType.circuitOutput, 1, 0))  # making output circuit port


def gateNumtoName(listofGatesNum):
    temp =[]
    for i in range(len(listofGatesNum)):
        if listofGatesNum[i] == 0:
            temp.append( "IN")
        elif listofGatesNum[i] == 1:
            temp.append("OUT")
        elif listofGatesNum[i] == 2:
            temp.append("AND")
    return temp
