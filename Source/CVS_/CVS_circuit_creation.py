from CVS_.CVS_gate_class import Gate, GateType
from CVS_.CVS_constants import INPUTSTOTAL, OUTPUTSTOTAL

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
                    return "weird stuff happening flag here"
            #print(GateList[a].gate_id, GateList[b].gate_id)
            return GateList[a].gateConnect(GateList[b])
        except:
            return "False"



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
            temp.append("IN")
        elif listofGatesNum[i] == 1:
            temp.append("OUT")
        elif listofGatesNum[i] == 2:
            temp.append("AND")
        elif listofGatesNum[i] == 3:
            temp.append("OR")
        elif listofGatesNum[i] == 4:
            temp.append("NOT")
        elif listofGatesNum[i] == 5:
            temp.append("NAND")
        elif listofGatesNum[i] == 6:
            temp.append("NOR")
        elif listofGatesNum[i] == 7:
            temp.append("XOR")
    return temp
