# from CVS_.CVS_circuit_creation import gateNumtoName
from CVS_.CVS_circuit_calculations import table_column_get, table_output, circuit_output_compare, circuit_Metrics, \
    circuit_errors, getfancyprintoutstring, scancirc
import ttg
from CVS_.CVS_gate_class import GateType


def runParser(listOfGates, ogCircuitOutput):
    for gate in listOfGates:
        gate.g_print()
    CrawlerOut = circuitParsing(listOfGates)
    returnValue = circuitConnecting(CrawlerOut, listOfGates)
    print("Circuit Output:", returnValue)
    circuitPercentSame = circuit_output_compare(returnValue, ogCircuitOutput)
    print("Percent Circuit Output is Equal to OG:", circuitPercentSame)
    metrics = circuit_Metrics(listOfGates)
    print('\n')
    print("Power(uA) | Delay(ns) | Transistors ", metrics)
    # print(getfancyprintoutstring(0,listOfGates))

    return circuitPercentSame


def ParserMetrics(listOfGates, ogCircuitOutput):
    CrawlerOut = circuitParsing(listOfGates)
    returnValue = circuitConnecting(CrawlerOut, listOfGates)
    circuitPercentSame = circuit_output_compare(returnValue, ogCircuitOutput)
    # print("Percent Circuit Output is Equal to OG:", circuitPercentSame)
    metrics = circuit_Metrics(listOfGates)
    # print("\n","Power(uA) | Delay(ns) | Transistors ", metrics)
    return circuitPercentSame, metrics, returnValue


def runParserMuted(listOfGates, ogCircuitOutput):
    CrawlerOut = circuitParsing(listOfGates)
    returnValue = circuitConnecting(CrawlerOut, listOfGates)
    return circuit_output_compare(returnValue, ogCircuitOutput)


def runLUCAParser(listOfGates, ogCircuitOutput):
    # for gate in listOfGates:
    #     gate.g_print()
    CrawlerOut = circuitParsing(listOfGates)
    returnValue = circuitConnecting(CrawlerOut, listOfGates)
    # print("Circuit Output:", returnValue)
    circuitPercentSame = circuit_output_compare(returnValue, ogCircuitOutput)
    # print("Percent Circuit Output is Equal to OG:", circuitPercentSame)
    metrics = circuit_Metrics(listOfGates)
    # print("Power(uA) | Delay(ns) | Transistors ", metrics)
    # print(getfancyprintoutstring(0,listOfGates))
    # print('\n')

    return circuitPercentSame


# def convertNumtoWord(type):
#     if type == 2:
#         return "and"
#     elif type == 3:
#         return "or"
#     elif type == 4:
#         return "not"
#     elif type == 5:
#         return "nand"
#     elif type == 6:
#         return "nor"
#     elif type == 7:
#         return "xor"
#     elif type == 9:
#         return "xnor"


def circuitParsing(listOFGates):  # this gets a list of outputs, inputs, and other gates types
    temp_output_id = []
    temp_input_id = []
    temp_gate_id = []

    # for i in listOFGates:  # start from output
    #     if i.type == 1:  # outputs gates
    #         try:
    #             temp_output_id.append(i)
    #         except:
    #             print('fail')
    #     elif i.type == 0:  # if input is reached, by this point a list of gates should be found
    #         try:
    #             temp_input_id.append(i)
    #         except:
    #             print('fail')
    #     else:  # rest of gates added here
    #         try:
    #             temp_gate_id.append(i)
    #         except:
    #             print('fail')

    for i in listOFGates:  # start from output
        if i.type == 1:  # outputs gates
            temp_output_id.append(i)
        elif i.type == 0:  # if input is reached, by this point a list of gates should be found
            temp_input_id.append(i)
        else:  # rest of gates added here
            temp_gate_id.append(i)


    # print(temp_output_id)
    # print(temp_input_id)
    # print(temp_gate_id)

    crawlerOutput = [temp_output_id, temp_input_id, temp_gate_id]
    return crawlerOutput


def circuitConnecting(CrawlerOut,
                      listOfGates):  # goes through circuit starting from input gates, and determines the outputs of each gate
    # print("\n")
    if listOfGates == []:
        return print("empty list")
    recursion_counter = 0

    mated_to_list = []
    circuitOutput = []

    circuitInput = []
    tableInput_IDs = []
    tableInput_TableOut = []
    for i in CrawlerOut[1]:  # inputs----------------------------------------------------------------
        for j in range(len(i.outputs)):
            #   print(i.type, i.outputs[j].mated_to, i.gate_id)
            tableInput_IDs.append(i.gate_id)

    # generate inital input states
    tableInput_IDs_formated = ((list(map(str, list(set(tableInput_IDs))))))  # list with strings in it
    try:
        tempTable = ttg.Truths(tableInput_IDs_formated).as_pandas()
        for i in tableInput_IDs_formated:
            tableInput_TableOut.append(tempTable[[i]])
        circuitInput = table_column_get(tableInput_TableOut, circuitInput)
    except:
        print(tableInput_IDs_formated)


    # pass generate table inputs, into input gate outputs
    for i in CrawlerOut[1]:
        i.tableOutput = circuitInput[i.gate_id]

    # make a new list of gates

    # CopiedListofGates.append(CrawlerOut[1])
    # CopiedListofGates.append(CrawlerOut[2])
    # CopiedListofGates.append(CrawlerOut[0])

    # (CopiedListofGates)

    CopiedListofGates = listOfGates

    while len(CopiedListofGates) != 0:
        for gate_c in CopiedListofGates:
            if gate_c.type == GateType.circuitInput:
                # iterate trough mated to list
                for gate_searching in CopiedListofGates:
                    if gate_searching == gate_c:
                        pass
                    # print(gate_c.gate_id,gate_searching.gate_id)
                    if gate_searching.type == GateType.circuitInput or gate_searching.type == GateType.circuitOutput:
                        pass
                    else:
                        # print(gate_c.gate_id,"testing", gate_c.outputs[0]._ID)
                        # print(gate_searching.gate_id,"testing",gate_searching.inputs[0].mated_to)
                        for num in range(len(gate_c.outputs[0].mated_to)):
                            for num2 in range(len(gate_searching.inputs)):
                                if gate_c.outputs[0]._ID == gate_searching.inputs[num2].mated_to[0]:
                                    gate_searching.logicInputs.append(gate_c.tableOutput)
                                    CopiedListofGates.pop(CopiedListofGates.index(gate_c))
                                    # print(gate_searching.gate_id,"gate input", gate_searching.logicInputs)
                            break
                # print("currnet gate", gate_c.gate_id, gate_c.logicInputs, gate_c.tableOutput)
                # CopiedListofGates.pop(CopiedListofGates.index(gate_c))


            elif gate_c.type == GateType.circuitOutput:
                # print(gate_c.gate_id, "outputs", gate_c.logicInputs)
                if gate_c.logicInputs == []:
                    if recursion_counter == 20:
                        print("OUTPUT HAS NO INPUTS")
                        return "imma bonehead"
                    recursion_counter += 1
                    pass
                elif gate_c.type == GateType.DUMMY:
                    pass
                else:
                    circuitOutput.append(gate_c.logicInputs[0])
                    # print("currnet gate", gate_c.gate_id, gate_c.logicInputs, gate_c.tableOutput)
                    CopiedListofGates.pop(CopiedListofGates.index(gate_c))

            else:
                if gate_c.type == GateType.NOT or gate_c.type == GateType.NOGATE:
                    if len(gate_c.logicInputs) == 0:
                        pass
                    else:
                        gate_c.tableOutput = table_output(gate_c.logicInputs[0], [], gate_c.type)
                        # pass output to connected gates?
                        for gate_searching in CopiedListofGates:
                            if gate_searching == gate_c:
                                pass
                            # print(gate_c.gate_id, gate_searching.gate_id)
                            if gate_searching.type == GateType.circuitInput:
                                pass
                            else:
                                # print(gate_c.gate_id,"testing", gate_c.outputs[0]._ID)
                                # print(gate_searching.gate_id,"testing",gate_searching.inputs[0].mated_to)
                                for num in range(len(gate_c.outputs[0].mated_to)):
                                    for num2 in range(len(gate_searching.inputs)):
                                        if gate_c.outputs[0]._ID == gate_searching.inputs[num2].mated_to[0]:
                                            gate_searching.logicInputs.append(gate_c.tableOutput)
                                            # print(gate_searching.gate_id, "gate input", gate_searching.logicInputs)
                                            CopiedListofGates.pop(CopiedListofGates.index(gate_c))
                                    break
                        # print("currnet gate", gate_c.gate_id, gate_c.logicInputs, gate_c.tableOutput)
                        #CopiedListofGates.pop(CopiedListofGates.index(gate_c))

                # check if gate has gate has logic inputs
                if len(gate_c.logicInputs) == 0 or len(gate_c.logicInputs) == 1:
                    pass
                else:
                    # logic gates
                    if gate_c.type == 99:
                        pass
                    else:
                        gate_c.tableOutput = table_output(gate_c.logicInputs[0], gate_c.logicInputs[1], gate_c.type)
                        # pass output to connected gates?
                        for gate_searching in CopiedListofGates:
                            if gate_searching == gate_c:
                                pass
                            # print(gate_c.gate_id, gate_searching.gate_id)
                            if gate_searching.type == GateType.circuitInput:
                                pass
                            else:
                                # print(gate_c.gate_id,"testing", gate_c.outputs[0]._ID)
                                # print(gate_searching.gate_id,"testing",gate_searching.inputs[0].mated_to)
                                for num in range(len(gate_c.outputs[0].mated_to)):
                                    for num2 in range(len(gate_searching.inputs)):
                                        if gate_c.outputs[0]._ID == gate_searching.inputs[num2].mated_to[0]:
                                            gate_searching.logicInputs.append(gate_c.tableOutput)
                                            CopiedListofGates.pop(CopiedListofGates.index(gate_c))
                                            # print(gate_searching.gate_id, "gate input", gate_searching.logicInputs)
                                    break
                        # print("currnet gate", gate_c.gate_id, gate_c.logicInputs, gate_c.tableOutput)
                        # CopiedListofGates.pop(CopiedListofGates.index(gate_c))

            # print("currnet gate",gate_c.gate_id, gate_c.logicInputs,gate_c.tableOutput)
            # CopiedListofGates.pop(CopiedListofGates.index(gate_c))

    # table = ttg.Truths(tableInput_IDs_formated)
    # print(table.as_tabulate())

    for i in circuitOutput:
        i.reverse()

    # circuitOutput_fixed = []
    # print("hhere",circuitOutput)
    # for i in circuitOutput:
    #     circuitOutput_fixed = i
    #
    # print(circuitOutput_fixed)

    return circuitOutput
# ---------------------------------End of circuitConnecting ----------------------------------------------------------
