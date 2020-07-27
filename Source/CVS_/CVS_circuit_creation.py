from CVS_.CVS_gate_class import Gate, GateType


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


def create_circuit_inputs(mega_list, inputs):
    for i in range(inputs):
        mega_list.append(Gate(GateType.circuitInput, 0, 1))  # making input circuit port


def create_circuit_outputs(mega_list, outputs):
    for i in range(outputs):
        mega_list.append(Gate(GateType.circuitOutput, 1, 0))  # making output circuit port
