import gate_class, functions
import ttg

# Constants
inputsTotal = 2
outputsTotal = 1

listOfGates = []
# Half adder
# make A B inputs
inputGateList = functions.create_circuit_inputs(listOfGates)
outputGateList = functions.create_circuit_outputs(listOfGates)

# make XOR gate with A B inputs
listOfGates.append(gate_class.Gate(gate_class.GateType.AND))

# connect gates
functions.Output_to_Input(listOfGates,0,3)
functions.Output_to_Input(listOfGates,1,3)
functions.Output_to_Input(listOfGates,3,2)


for gate in listOfGates:
    gate.g_print()

# create TT based on num inputs
inputTTList = []
gatesInList = []
TToutputs = []
for i in range(inputsTotal):
    inputTTList.append(i)
    print((list(map(str,list(set(inputTTList))))))
for i in range(len(listOfGates)):
    gatesInList = listOfGates[i].type
    print(gatesInList)

#TToutputs.append(functions.gateNumtoName(gatesInList))

table = ttg.Truths((list(map(str,list(set(inputTTList))))) )
print(table)

# add column based on outputs
# metrics calculation

