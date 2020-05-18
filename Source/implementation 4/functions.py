from gate_class import Gate, GateType
#from main import inputsTotal,outputsTotal

def Output_to_Input(GateList,a,b):
    if a==b:
        return
    else:
        try:
            if GateList[a].type == GateType.circuitInput or GateList[b].type == GateType.circuitInput:
                if GateList[a].type == GateType.circuitOutput or GateList[b].type == GateType.circuitOutput:
                    print("asd")

            return GateList[a].gateConnect(GateList[b])
        except:
            #return GateCost.COST_ILEGAL
            print("as")

def create_circuit_inputs(mega_list):
    from main import inputsTotal
    for i in range(inputsTotal):
        mega_list.append(Gate(GateType.circuitInput, 0, 1)) #making input circuit port

def create_circuit_outputs(mega_list):
    from main import outputsTotal
    for i in range(outputsTotal):
        mega_list.append(Gate(GateType.circuitOutput, 1, 0)) #making output circuit port

def Total_Power():
    pass

def Total_Delay():
    pass

def gateNumtoName(listofGatesNum):
    for i in range(listofGatesNum):
        if listofGatesNum[i] == 0:
            return "IN"
        elif listofGatesNum[i] == 1:
            return "OUT"
        elif listofGatesNum[i] == 2:
            return "AND"