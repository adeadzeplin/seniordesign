from Source import CVS_parser, CVS_circuit_creation, CVS_gate_class


def CVS():
    listOfGates = []
    # Half adder
    # make A B inputs
    CVS_circuit_creation.create_circuit_inputs(listOfGates)
    CVS_circuit_creation.create_circuit_outputs(listOfGates)

    # make XOR gate with A B inputs
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    #listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    # listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))

    # connect gates
# one gate
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 3)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 3)
    CVS_circuit_creation.Output_to_Input(listOfGates, 3, 2)

# half adder
#     CVS_circuit_creation.Output_to_Input(listOfGates, 0, 4)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 6, 2)
#
#     CVS_circuit_creation.Output_to_Input(listOfGates, 0, 7)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 1, 8)
#     CVS_circuit_creation.Output_to_Input(listOfGates, 9, 3)

    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 4)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 1, 4)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 4, 2)
    #
    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 5, 3)



# full adder
    #xor 5
    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 1, 6)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 7, 14)
    #
    # #and 6
    # CVS_circuit_creation.Output_to_Input(listOfGates, 0, 8)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 1, 9)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 10, 17)
    #
    # #and 7
    # CVS_circuit_creation.Output_to_Input(listOfGates, 2, 12)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 7, 11)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 13, 18)
    #
    # #xor 8
    # CVS_circuit_creation.Output_to_Input(listOfGates, 2, 15)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 7, 14)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 16, 3)
    #
    # #xor 9
    # CVS_circuit_creation.Output_to_Input(listOfGates, 13, 17)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 10, 18)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 19, 4)

    ParserOutputs = CVS_parser.organizing(listOfGates)
    CrawlerOut = CVS_parser.circuitCrawling(listOfGates, ParserOutputs[1])
    CVS_parser.printTable(ParserOutputs[0], CrawlerOut)

    # add column based on outputs
    # metrics calculation


if __name__ == '__main__':
    CVS()
