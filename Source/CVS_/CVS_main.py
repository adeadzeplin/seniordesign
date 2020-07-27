from CVS_ import CVS_parser, CVS_circuit_creation, CVS_gate_class, CVS_circuit_calculations


# INPUTSTOTAL = 3
# OUTPUTSTOTAL = 1

def half_adder(listOfGates):
    # half adder
    inputs = 2
    outputs = 2

    # make A B inputs
    CVS_circuit_creation.create_circuit_inputs(listOfGates, inputs)
    CVS_circuit_creation.create_circuit_outputs(listOfGates, outputs)

    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    # xor 4
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 4)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 4)
    CVS_circuit_creation.Output_to_Input(listOfGates, 4, 2)
    # CVS_circuit_creation.Output_to_Input(listOfGates, 4, 3)

    # and 5
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 3)

    ogCircuitOutput = [[0, 1, 1, 0], [0, 0, 0, 1]]
    return ogCircuitOutput


def full_adder(listOfGates):
    # full adder
    inputs = 3
    outputs = 2

    # make A B inputs
    CVS_circuit_creation.create_circuit_inputs(listOfGates, inputs)
    CVS_circuit_creation.create_circuit_outputs(listOfGates, outputs)

    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))

    # xor 5
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 8)

    # and 6
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 6)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 6)
    CVS_circuit_creation.Output_to_Input(listOfGates, 6, 9)

    # and 7
    CVS_circuit_creation.Output_to_Input(listOfGates, 2, 7)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 7)
    CVS_circuit_creation.Output_to_Input(listOfGates, 7, 9)

    # xor 8
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 8)
    CVS_circuit_creation.Output_to_Input(listOfGates, 2, 8)
    CVS_circuit_creation.Output_to_Input(listOfGates, 8, 3)

    # xor 9
    CVS_circuit_creation.Output_to_Input(listOfGates, 7, 9)
    CVS_circuit_creation.Output_to_Input(listOfGates, 6, 9)
    CVS_circuit_creation.Output_to_Input(listOfGates, 9, 4)

    ogCircuitOutput = [[0, 1, 1, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1]]
    return ogCircuitOutput


def large_circuit(listOfGates):
    # larger circuit test
    inputs = 3
    outputs = 2

    # make A B inputs
    CVS_circuit_creation.create_circuit_inputs(listOfGates, inputs)
    CVS_circuit_creation.create_circuit_outputs(listOfGates, outputs)
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.AND))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.XOR))
    #
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.NOT))
    listOfGates.append(CVS_gate_class.Gate(CVS_gate_class.GateType.NOT))

    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 8)

    # and 6
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 6)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 6)
    CVS_circuit_creation.Output_to_Input(listOfGates, 6, 9)

    # and 7
    CVS_circuit_creation.Output_to_Input(listOfGates, 2, 7)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 7)
    CVS_circuit_creation.Output_to_Input(listOfGates, 7, 9)

    # xor 8
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 8)
    CVS_circuit_creation.Output_to_Input(listOfGates, 2, 8)
    CVS_circuit_creation.Output_to_Input(listOfGates, 8, 10)

    # xor 9
    CVS_circuit_creation.Output_to_Input(listOfGates, 7, 9)
    CVS_circuit_creation.Output_to_Input(listOfGates, 6, 9)
    CVS_circuit_creation.Output_to_Input(listOfGates, 9, 11)

    # not 10
    CVS_circuit_creation.Output_to_Input(listOfGates, 8, 10)
    CVS_circuit_creation.Output_to_Input(listOfGates, 10, 3)

    # not 11
    CVS_circuit_creation.Output_to_Input(listOfGates, 9, 11)
    CVS_circuit_creation.Output_to_Input(listOfGates, 11, 4)

    ogCircuitOutput = [[1, 0, 0, 1, 0, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 0]]
    return ogCircuitOutput


def out_of_order(listOfGates):
    # Out of Order test
    inputs = 3
    outputs = 2

    # make A B inputs
    CVS_circuit_creation.create_circuit_inputs(listOfGates, inputs)
    CVS_circuit_creation.create_circuit_outputs(listOfGates, outputs)

    # gate 5 (id 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 5)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 6)
    # gate 6 (id 6)
    CVS_circuit_creation.Output_to_Input(listOfGates, 5, 6)
    CVS_circuit_creation.Output_to_Input(listOfGates, 8, 6)
    CVS_circuit_creation.Output_to_Input(listOfGates, 6, [7, 9])
    # gate 7 (id 7)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 7)
    CVS_circuit_creation.Output_to_Input(listOfGates, 6, 7)
    CVS_circuit_creation.Output_to_Input(listOfGates, 7, 3)
    # gate 9 (id 8)
    CVS_circuit_creation.Output_to_Input(listOfGates, 2, 8)
    CVS_circuit_creation.Output_to_Input(listOfGates, 10, 8)
    CVS_circuit_creation.Output_to_Input(listOfGates, 8, 6)
    # gate 10 (id 9)
    CVS_circuit_creation.Output_to_Input(listOfGates, 6, 9)
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 9)
    CVS_circuit_creation.Output_to_Input(listOfGates, 9, 4)
    # gate 11 (id 10)
    CVS_circuit_creation.Output_to_Input(listOfGates, 0, 10)
    CVS_circuit_creation.Output_to_Input(listOfGates, 1, 10)
    CVS_circuit_creation.Output_to_Input(listOfGates, 10, 8)

    ogCircuitOutput = [[0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 1]]
    return ogCircuitOutput


def CVS():
    listOfGates = []

    # Select Circuit

    # ogCircuitOutput = half_adder(listOfGates)
    ogCircuitOutput = full_adder(listOfGates)
    # ogCircuitOutput = large_circuit(listOfGates)
    # ogCircuitOutput = out_of_order(listOfGates)

    circ_printer = CVS_circuit_calculations.PrintClass()
    print(circ_printer.getfancyprintoutstring(listOfGates))

    # intial circuit connection check
    Circuit_Errors = CVS_circuit_calculations.circuit_connection_check(listOfGates)
    # Circuit_Errors = None
    if Circuit_Errors == None:
        CVS_parser.runParser(listOfGates, ogCircuitOutput)
    else:
        print(Circuit_Errors)

    # metrics calculation


if __name__ == '__main__':
    CVS()
