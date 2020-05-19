from Source import CVS_parser, CVS_circuit_creation, CVS_gate_class


def CVS():
    listOfGates = []
    # Half adder
    # make A B inputs
    CVS_circuit_creation.create_circuit_inputs(listOfGates)
    CVS_circuit_creation.create_circuit_outputs(listOfGates)

    # make XOR gate with A B inputs
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    # listOfGates.append(gate_class.Gate(gate_class.GateType.XOR))

    # connect gates
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 3)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 4)
    CVS_circuit_creation.Output_to_Input(listOfGates, 3, 2)

    # circuit_creation.Output_to_Input(listOfGates, 0, 4)
    # circuit_creation.Output_to_Input(listOfGates, 1, 5)
    # circuit_creation.Output_to_Input(listOfGates, 6, 2)
    #
    # circuit_creation.Output_to_Input(listOfGates, 0, 7)
    # circuit_creation.Output_to_Input(listOfGates, 1, 8)
    # circuit_creation.Output_to_Input(listOfGates, 9, 3)

    ParserOutputs = CVS_parser.organizing(listOfGates)
    CrawlerOut = CVS_parser.circuitCrawling(listOfGates, ParserOutputs[1])
    CVS_parser.printTable(ParserOutputs[0], CrawlerOut)

    # add column based on outputs
    # metrics calculation


if __name__ == '__main__':
    CVS()
