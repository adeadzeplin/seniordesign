# from CVS_.CVS_circuit_creation import gateNumtoName
# from CVS_.CVS_constants import INPUTSTOTAL
from CVS_.CVS_circuit_calculations import table_column_get, table_output, circuit_output_compare
import ttg

def runParser(listOfGates,ogCircuitOutput):
    for gate in listOfGates:
        gate.g_print()
    CrawlerOut = circuitParsing(listOfGates)
    returnValue = circuitConnecting(CrawlerOut)
    print("Circuit Output:", returnValue)
    circuitPercentSame = circuit_output_compare(returnValue, ogCircuitOutput)
    print("Percent Circuit Output is Equal to OG:", circuitPercentSame)

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


# def organizing(listOfGates):
# #     for gate in listOfGates:
# #         gate.g_print()
# #     # create TT based on num inputs
# #     inputTTList = []
# #     gatesInList = []
# #     TToutputs = []
# #
# #     for i in range(INPUTSTOTAL):
# #         inputTTList.append(i)
# #         # print((list(map(str, list(set(inputTTList))))))
# #     for i in range(len(listOfGates)):
# #         gatesInList.append(listOfGates[i].type)
# #
# #     # print(" \n"  + str(gatesInList))
# #     TToutputs.append(gateNumtoName(gatesInList))
# #     #print(TToutputs,inputTTList,gatesInList)
# #     return inputTTList


def circuitParsing(listOFGates): #this gets a list of outputs, inputs, and other gates types
    temp_output_id = []
    temp_input_id = []
    temp_gate_id = []

    for i in listOFGates:  # start from output
        if i.type == 1: #outputs gates
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


def circuitConnecting(CrawlerOut): # goes through circuit starting from input gates, and determines the outputs of each gate
    print("\n")
    whatInputsConnectedTo = []
    tableInput_IDs = []
    tableInput_TableOut = []
    whatGatesConnectedTo = []
    whatOutputsConnectedTo = []
    circuitInput = []
    circuitOutput = []
    mated_to_list = []
    matches = []

    for i in CrawlerOut[1]:  # inputs----------------------------------------------------------------
        for j in range(len(i.outputs)):
            print(i.type, i.outputs[j].mated_to, i.gate_id)
            tableInput_IDs.append(i.gate_id)
            whatInputsConnectedTo.append(i.outputs[j].mated_to)


    tableInput_IDs_formated = ((list(map(str, list(set(tableInput_IDs))))))  # list with strings in it
    tempTable = ttg.Truths(tableInput_IDs_formated).as_pandas()
    for i in tableInput_IDs_formated:
        print("hello",i)
        tableInput_TableOut.append(tempTable[[i]])

    circuitInput = table_column_get(tableInput_TableOut, circuitInput)


    print("\n")

    for i in CrawlerOut[2]:  # gates----------------------------------------------------------------

        print(i.gate_id, i.type, i.inputs[0]._ID, i.inputs[1]._ID, i.outputs[0]._ID)
        whatGatesConnectedTo.append(i.inputs)
        if i.type == 4: # check if NOT gate
            formatted_gateOutputExpression = []
            mated_to_list.append(i.inputs[0].mated_to)
            normalized_mated_list = []
            for g in mated_to_list:             #loop that reformats t array
                normalized_mated_list.append(g[0])

            gateOutputExpression = "%s %s" % (convertNumtoWord(i.type), normalized_mated_list[0])
            print(gateOutputExpression)

            formatted_gateOutputExpression.append(gateOutputExpression)
            formatted_gateOutputExpression = (list(map(str, list(set(formatted_gateOutputExpression)))))
            gateOutput_both = ttg.Truths(tableInput_IDs_formated, formatted_gateOutputExpression).as_pandas()
            #print(gateOutput_both)
            gateOutputExpression = gateOutput_both[[gateOutputExpression]]
            tablecolumn = []
            # print(gateOutputExpression)
            for u in range(1, len(circuitInput[0]) + 1):
                tablecolumn.append(gateOutputExpression[formatted_gateOutputExpression[0]][u])
            print(tablecolumn)

            i.tableOutput = tablecolumn

        else:       #other gate types
            # print(i.gate_id)

            for j in range(len(i.inputs)):
                mated_to_list.append(i.inputs[j].mated_to)

            normalized_mated_list = []

            for g in mated_to_list:               # resets array in array -> just one array
                normalized_mated_list.append(g[0])

            for c in normalized_mated_list:
                if c in tableInput_IDs:
                    matches.append(c)

            formatted_gateOutputExpression = []

            if len(matches) == 2:  # both inputs are from circuit inputs
                # print('both')
                gateOutputExpression = "%s %s %s" % (matches[0], convertNumtoWord(i.type), matches[1])
                print(gateOutputExpression)
                formatted_gateOutputExpression.append(gateOutputExpression)
                formatted_gateOutputExpression = (list(map(str, list(set(formatted_gateOutputExpression)))))
                gateOutput_both = ttg.Truths(tableInput_IDs_formated, formatted_gateOutputExpression).as_pandas()

                # get column with expression
                gateOutputExpression = gateOutput_both[[gateOutputExpression]]
                tablecolumn = []
                for u in range(1, len(circuitInput[0]) + 1):
                    tablecolumn.append(gateOutputExpression[formatted_gateOutputExpression[0]][u])
                print(tablecolumn)
                # listOFGateOutputs.append(listOFGateOutputs)
                i.tableOutput = tablecolumn
                # print(i.type,i.tableOutput)

            # else if only one input is circuit input, and other is gate output
            elif len(matches) == 1:
                # print('one')
                circuitInput_temp = 0
                for v in matches:  # input to circuit
                    for b in normalized_mated_list:  # output of gate
                        try:
                            if v != b:
                                gateOutputExpression = "%s %s %s" % (v, convertNumtoWord(i.type), b)
                                circuitInput_temp = v
                                print(gateOutputExpression)
                        except:
                            print("fial")

                for n in CrawlerOut[2]:             # looking for check gate output
                    for m in normalized_mated_list:
                        if n.outputs[0]._ID == m:
                            # take gates output
                            # print(n.type, n.tableOutput) #output of gate
                            # print(circuitInput[circuitInput_temp])
                            a = n.tableOutput
                            b = circuitInput[circuitInput_temp]
                            i.tableOutput = table_output(a, b, i.type)
                            print(i.tableOutput)

            # else if BOTH inputs are gate outputs
            elif len(matches) == 0:
                temp_outputs = []
                for n in CrawlerOut[2]:  # looking for check gate output
                    for m in normalized_mated_list:
                        if n.outputs[0]._ID == m:
                            # print( n.outputs[0]._ID, m)
                            temp_outputs.append(n.tableOutput)
                a = temp_outputs[0]
                b = temp_outputs[1]
                i.tableOutput = table_output(a, b, i.type)
                print(i.tableOutput)

            # clears arrays for next gate
            matches = []
            mated_to_list = []

    print("\n")

    for i in CrawlerOut[0]:  # outputs----------------------------------------------------------------
        temp_outputs = []
        for j in range(len(i.inputs)):
            print(i.gate_id, i.type, i.inputs[j].mated_to)
            whatOutputsConnectedTo.append(i.inputs[j].mated_to)
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
                    print(i.tableOutput)

        circuitOutput.append(i.tableOutput)
        mated_to_list = []

    print("\n")

    # table = ttg.Truths(tableInput_IDs_formated)
    # print(table.as_tabulate())

    for i in circuitOutput:
        i.reverse()

    return circuitOutput
#---------------------------------End of circuitConnecting ----------------------------------------------------------
