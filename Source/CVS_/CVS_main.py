from CVS_ import CVS_parser, CVS_circuit_creation, CVS_gate_class, CVS_circuit_calculations


def CVS():
    listOfGates = []
    CVS_circuit_creation.create_circuit_inputs(listOfGates)
    CVS_circuit_creation.create_circuit_outputs(listOfGates)

    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND,4))

    #4 input gate
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 2, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 3, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 4)

    ogCircuitOutput = [[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]]
#   ogCircuitOutput = [[1, 0, 0, 1, 0, 1, 1, 0],[1, 1, 1, 0, 1, 0, 0, 0]]

    Circuit_Errors = CVS_circuit_calculations.circuit_connection_check(listOfGates)
    if Circuit_Errors == None:
        CVS_parser.runParser(listOfGates,ogCircuitOutput)
    else:
        print(Circuit_Errors)

    # metrics calculation


if __name__ == '__main__':
    CVS()
