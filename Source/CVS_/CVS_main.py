from CVS_ import CVS_parser, CVS_circuit_creation, CVS_gate_class, CVS_circuit_calculations


def CVS():
    listOfGates = []
    # Half adder
    # make A B inputs
    CVS_circuit_creation.create_circuit_inputs(listOfGates)
    CVS_circuit_creation.create_circuit_outputs(listOfGates)

    # make XOR gate with A B inputs
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    # #
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.NOT))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.NOT))

    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND,4))


    # connect gates
    #one gate
    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 3)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 1, 3)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 3, 2)
    #
    # ogCircuitOutput = [[0,0,0,1]]

    #not gate
    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 2)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 2, 1)
    # ogCircuitOutput = [[1,0]]

    #4 input gate
    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 2, 5)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 3, 5)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 5, 4)
    #
    # ogCircuitOutput = [[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]]




# half adder
    #xor 4
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 4)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 4)
    CVS_circuit_creation.Output_to_Input(listOfGates, 4, 2)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 4, 3)

    # and 5
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 3)

    ogCircuitOutput = [[0,1,1,0],[0,0,0,1]]

  #  [0, 0, 0, 1, 0, 1, 1, 1]

# full adder
    #xor 5
    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 5, 8)
    #
    # #and 6
    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 6)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 1, 6)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 6, 9)
    #
    # #and 7
    # CVS_circuit_creation.Output_to_Input(listOfGates, 2, 7)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 5, 7)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 7, 9)
    #
    # #xor 8
    # CVS_circuit_creation.Output_to_Input(listOfGates, 5, 8)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 2, 8)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 8, 3)
    #
    # #xor 9
    # CVS_circuit_creation.Output_to_Input(listOfGates, 7, 9)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 6, 9)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 9, 4)
    #
    # ogCircuitOutput = [[0, 1, 1, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1]]


# # larger circuit test
#     CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 5, 8)
#
#     #and 6
#     CVS_circuit_creation.Output_to_Input(listOfGates, 0, 6)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 1, 6)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 6, 9)
#
#     #and 7
#     CVS_circuit_creation.Output_to_Input(listOfGates, 2, 7)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 5, 7)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 7, 9)
#
#     #xor 8
#     CVS_circuit_creation.Output_to_Input(listOfGates, 5, 8)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 2, 8)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 8, 10)
#
#     #xor 9
#     CVS_circuit_creation.Output_to_Input(listOfGates, 7, 9)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 6, 9)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 9, 11)
#
#     #not 10
#     CVS_circuit_creation.Output_to_Input(listOfGates, 8, 10)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 10, 3)
#
#     #not 11
#     CVS_circuit_creation.Output_to_Input(listOfGates, 9, 11)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 11, 4)
#
#     ogCircuitOutput = [[1, 0, 0, 1, 0, 1, 1, 0],[1, 1, 1, 0, 1, 0, 0, 0]]

    #test circuit
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))

    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 4)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 8, 10)
    CVS_circuit_creation.Output_to_Input(listOfGates, 4, 3)

    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 2)


    ogCircuitOutput = [[0, 1, 1, 0], [0, 0, 0, 1]]


    #intial circuit connection check
    Circuit_Errors = CVS_circuit_calculations.circuit_connection_check(listOfGates)
    # Circuit_Errors = None
    if Circuit_Errors == None:
        CVS_parser.runParser(listOfGates,ogCircuitOutput)
    else:
        print(Circuit_Errors)

    # metrics calculation


if __name__ == '__main__':
    CVS()
