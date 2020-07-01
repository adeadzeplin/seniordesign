# from CVS_.CVS_circuit_creation import gateNumtoName
from CVS_.CVS_constants import INPUTSTOTAL
from CVS_.CVS_circuit_calculations import table_column_get, table_output, circuit_output_compare,circuit_Metrics
import ttg


def runParser(listOfGates, ogCircuitOutput):
    for gate in listOfGates:
        gate.g_print()
    CrawlerOut = circuitParsing(listOfGates)
    returnValue = circuitConnecting(CrawlerOut)
    print("Circuit Output:", returnValue)
    circuitPercentSame = circuit_output_compare(returnValue, ogCircuitOutput)
    print("Percent Circuit Output is Equal to OG:", circuitPercentSame)

    metrics = circuit_Metrics(listOfGates)
    print("\n","Power(uA) | Delay(ns) | Transistors ", metrics)



def runQParser(listOfGates, ogCircuitOutput):
    CrawlerOut = circuitParsing(listOfGates)
    returnValue = circuitConnecting(CrawlerOut)
    return circuit_output_compare(returnValue, ogCircuitOutput)


def convertNumtoWord(type):
    if type == 2:
        return "and"
    elif type == 3:
        return "or"
    elif type == 4:
        return "not"
    elif type == 5:
        return "nand"
    elif type == 6:
        return "nor"
    elif type == 7:
        return "xor"


def circuitParsing(listOFGates):  # this gets a list of outputs, inputs, and other gates types
    temp_output_id = []
    temp_input_id = []
    temp_gate_id = []

    for i in listOFGates:  # start from output
        if i.type == 1:  # outputs gates
            try:
                temp_output_id.append(i)
            except:
                print('fail')
        elif i.type == 0:  # if input is reached, by this point a list of gates should be found
            try:
                temp_input_id.append(i)
            except:
                print('fail')
        else:  # rest of gates added here
            try:
                temp_gate_id.append(i)
            except:
                print('fail')

    # print(temp_output_id)
    # print(temp_input_id)
    # print(temp_gate_id)

    crawlerOutput = [temp_output_id, temp_input_id, temp_gate_id]
    return crawlerOutput


def circuitConnecting(CrawlerOut):  # goes through circuit starting from input gates, and determines the outputs of each gate
    # print("\n")
    tableInput_IDs = []
    tableInput_TableOut = []
    circuitInput = []
    circuitOutput = []
    mated_to_list = []

    for i in CrawlerOut[1]:  # inputs----------------------------------------------------------------
        for j in range(len(i.outputs)):
            # print(i.type, i.outputs[j].mated_to, i.gate_id)
            tableInput_IDs.append(i.gate_id)

    # generate inital input states
    tableInput_IDs_formated = ((list(map(str, list(set(tableInput_IDs))))))  # list with strings in it
    tempTable = ttg.Truths(tableInput_IDs_formated).as_pandas()
    for i in tableInput_IDs_formated:
        tableInput_TableOut.append(tempTable[[i]])
    circuitInput = table_column_get(tableInput_TableOut, circuitInput)

    # pass generate table inpputs, into input gate outputs
    for i in CrawlerOut[1]:
        i.tableOutput = circuitInput[i.gate_id]

    # print("\n")

    for i in CrawlerOut[2]:  # gates----------------------------------------------------------------
        # if i.gate_id:
        #     print(i.gate_id, i.type, i.inputs[0]._ID, i.outputs[0]._ID)
        # else:
        #     print(i.gate_id, i.type, i.inputs[0]._ID, i.inputs[1]._ID, i.outputs[0]._ID)

        connected_gate_output = []
        # extract outputs from connected gates
        input_len = len(i.inputs)
        for num in range(input_len):
            # print(i.inputs[num].mated_to[0])

            # error check #1

            connector_id = i.inputs[num].mated_to[0]
            if connector_id < INPUTSTOTAL:  # if gate is connected to only input gates
                # print(CrawlerOut[1][connector_id].tableOutput)
                connected_gate_output.append(CrawlerOut[1][connector_id].tableOutput)
            else:
                for gate in CrawlerOut[2]:
                    # print("testing",gate.inputs[0]._ID,gate.inputs[1]._ID, gate.outputs[0]._ID)
                    if gate.outputs[0]._ID == connector_id:
                        # print(gate.tableOutput)
                        connected_gate_output.append((gate.tableOutput))
        if i.type == 4:
            i.tableOutput = table_output(connected_gate_output[0], [], i.type)
        else:

            if connected_gate_output[1] == [] or connected_gate_output[0] == []:
                # print("error here")
                pass
                # return "ERROR_CONNECTED_GATE_OUTPUT_MISSING"
            else:
                i.tableOutput = table_output(connected_gate_output[0], connected_gate_output[1], i.type)

    for i in CrawlerOut[0]:  # outputs----------------------------------------------------------------
        for j in range(len(i.inputs)):
            # print(i.inputs[j].mated_to)
            mated_to_list.append(i.inputs[j].mated_to)
        normalized_mated_list = []
        # print(mated_to_list)
        for g in mated_to_list:
            normalized_mated_list.append(g[0])
        # print(normalized_mated_list)

        for n in CrawlerOut[2]:  # looking for check gate output
            for m in normalized_mated_list:
                if n.outputs[0]._ID == m:
                    # print(n.outputs[0]._ID, m)
                    # print(i.inputs[0]._ID, i.outputs)
                    i.tableOutput = n.tableOutput
                    # print(i.tableOutput)

        circuitOutput.append(i.tableOutput)
        mated_to_list = []

    # print("\n")

    # table = ttg.Truths(tableInput_IDs_formated)
    # print(table.as_tabulate())

    for i in circuitOutput:
        i.reverse()

    return circuitOutput
# ---------------------------------End of circuitConnecting ----------------------------------------------------------
