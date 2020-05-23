
from QLARK.qlark_class import Qlark

from CVS_ import CVS_parser, CVS_circuit_creation, CVS_gate_class
def CVS_():
    listOfGates = []
    # Half adder
    # make A B inputs
    CVS_circuit_creation.create_circuit_inputs(listOfGates)
    CVS_circuit_creation.create_circuit_outputs(listOfGates)

    # make XOR gate with A B inputs
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.NOT))

    # not gate
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 2)
    CVS_circuit_creation.Output_to_Input(listOfGates, 2, 1)


    ParserOutputs = CVS_parser.organizing(listOfGates)
    CrawlerOut = CVS_parser.circuitCrawling(listOfGates)
    CVS_parser.printTable(ParserOutputs[0], CrawlerOut)
def joint():
    listOfGates = []
    CVS_circuit_creation.create_circuit_inputs(listOfGates)
    CVS_circuit_creation.create_circuit_outputs(listOfGates)


if __name__ == '__main__':
    Qlearingai = Qlark()
    Qlearingai.run()
