import gate_class, circuit_creation, Parser
from Constants import listOfGates


def main():
    # listOfGates = []
    # Half adder
    # make A B inputs
    inputGateList = circuit_creation.create_circuit_inputs(listOfGates)
    outputGateList = circuit_creation.create_circuit_outputs(listOfGates)

    # make XOR gate with A B inputs
    listOfGates.append(gate_class.Gate(gate_class.GateType.AND))
    #listOfGates.append(gate_class.Gate(gate_class.GateType.XOR))

    # connect gates
    circuit_creation.Output_to_Input(listOfGates, 0, 3)
    circuit_creation.Output_to_Input(listOfGates, 1, 4)
    circuit_creation.Output_to_Input(listOfGates, 3, 2)

    # circuit_creation.Output_to_Input(listOfGates, 0, 4)
    # circuit_creation.Output_to_Input(listOfGates, 1, 5)
    # circuit_creation.Output_to_Input(listOfGates, 6, 2)
    #
    # circuit_creation.Output_to_Input(listOfGates, 0, 7)
    # circuit_creation.Output_to_Input(listOfGates, 1, 8)
    # circuit_creation.Output_to_Input(listOfGates, 9, 3)

    ParserOutputs = Parser.organizing()
    CrawlerOut = Parser.circuitCrawling(listOfGates, ParserOutputs[1])
    Parser.printTable(ParserOutputs[0],CrawlerOut)

    # add column based on outputs
    # metrics calculation


if __name__ == '__main__':
    main()
