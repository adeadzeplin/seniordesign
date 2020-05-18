import gate_class, functions
import ttg

# Constants
inputsTotal = 2
outputsTotal = 1
listOfGates_IO = []
listOfGates = []
# Half adder
# make A B inputs
inputGateList = functions.create_circuit_inputs(listOfGates)
outputGateList = functions.create_circuit_outputs(listOfGates)

# make XOR gate with A B inputs
listOfGates.append(gate_class.Gate(gate_class.GateType.AND))

for gate in listOfGates:
    gate.g_print()
print(listOfGates_IO)
for gate in listOfGates_IO:
    gate.g_print()
# connect gates
# create TT based on num inputs
# add column based on outputs
# metrics calculation

