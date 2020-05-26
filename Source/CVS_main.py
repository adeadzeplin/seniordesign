from Source import CVS_parser, CVS_circuit_creation, CVS_gate_class, CVS_circuit_calculations


def CVS():
    listOfGates = []
    # Half adder
    # make A B inputs
    CVS_circuit_creation.create_circuit_inputs(listOfGates)
    CVS_circuit_creation.create_circuit_outputs(listOfGates)

    # make XOR gate with A B inputs
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.NOT))

    # connect gates
    #one gate
    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 3)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 1, 3)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 3, 2)

    #not gate
    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 2)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 2, 1)


# half adder
    #xor 4
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 4)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 4)
    CVS_circuit_creation.Output_to_Input(listOfGates, 4, 2)
    #and 5
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 3)



# full adder
#     #xor 5
#     CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 5, 18)
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
#     CVS_circuit_creation.Output_to_Input(listOfGates, 8, 3)
#
#     #xor 9
#     CVS_circuit_creation.Output_to_Input(listOfGates, 7, 9)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 6, 9)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 9, 4)

    #intial circuit connection check
    Circuit_Errors = CVS_circuit_calculations.circuit_connection_check(listOfGates)

    if Circuit_Errors == None:
        ParserOutputs = CVS_parser.organizing(listOfGates)
        CrawlerOut = CVS_parser.circuitCrawling(listOfGates)
        returnValue = CVS_parser.printTable(ParserOutputs[0], CrawlerOut)
        print(returnValue)
    else:
        print(Circuit_Errors)

    # add column based on outputs
    # metrics calculation


if __name__ == '__main__':
    CVS()
