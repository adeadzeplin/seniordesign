from CVS_ import CVS_parser, CVS_circuit_creation, CVS_gate_class, CVS_circuit_calculations
import numpy as np


def CVS(gates, connections):
    CVS_gate_class.Gate.gate_id_counter = 0
    CVS_gate_class.Connector.id = 0
    listOfGates = []
    CVS_circuit_creation.create_circuit_inputs(listOfGates)

    for i in range(0, len(gates)):
        listOfGates.append(CVS_gate_class.Gate(gates[i]))
    CVS_circuit_creation.create_circuit_outputs(listOfGates)

    for j in range(len(connections)):
        CVS_circuit_creation.Output_to_Input(listOfGates, connections[j][0], connections[j][1])



    #ogCircuitOutput = [[0, 1, 1, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1]]
    ogCircuitOutput = [[0,1,1,0],[0,0,0,1]]
    #intial circuit connection check
    Circuit_Errors = CVS_circuit_calculations.circuit_connection_check(listOfGates)

    if Circuit_Errors == None:
        fit = CVS_parser.runParser(listOfGates, ogCircuitOutput)
        return fit
    else:
        print(Circuit_Errors)
        fit = 0
        return fit

if __name__ == '__main__':
    CVS()
