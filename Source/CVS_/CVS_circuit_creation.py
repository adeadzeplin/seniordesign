from CVS_.CVS_gate_class import Gate
from CVS_.CVS_constants import INPUTSTOTAL, OUTPUTSTOTAL


def Output_to_Input(GateList, a, b):
    if a == b:
        return
    else:
        try:
            if GateList[a].type == 0 or GateList[b].type == 0:
                if GateList[a].type == 1 or GateList[b].type == 1:
                    return "weird stuff happening flag here"
            #print(GateList[a].gate_id, GateList[b].gate_id)
            return GateList[a].gateConnect(GateList[b])
        except:
            return "False"


def create_circuit_inputs(mega_list):
    for i in range(INPUTSTOTAL):
        mega_list.append(Gate(0, 0, 1))  # making input circuit port


def create_circuit_outputs(mega_list):
    for i in range(OUTPUTSTOTAL):
        mega_list.append(Gate(1, 1, 0))  # making output circuit port


# def gateNumtoName(listofGatesNum):
#     temp =[]
#     for i in range(len(listofGatesNum)):
#         if listofGatesNum[i] == 0:
#             temp.append("IN")
#         elif listofGatesNum[i] == 1:
#             temp.append("OUT")
#         elif listofGatesNum[i] == 2:
#             temp.append("AND")
#         elif listofGatesNum[i] == 3:
#             temp.append("OR")
#         elif listofGatesNum[i] == 4:
#             temp.append("NOT")
#         elif listofGatesNum[i] == 5:
#             temp.append("NAND")
#         elif listofGatesNum[i] == 6:
#             temp.append("NOR")
#         elif listofGatesNum[i] == 7:
#             temp.append("XOR")
#     return temp
