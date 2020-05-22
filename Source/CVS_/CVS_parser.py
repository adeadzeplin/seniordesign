from Source.CVS_circuit_creation import gateNumtoName
from Source.CVS_constants import INPUTSTOTAL
import ttg


def organizing(listOfGates):
    for gate in listOfGates:
        gate.g_print()
    print(listOfGates[3].type)
    # create TT based on num inputs
    inputTTList = []
    gatesInList = []
    TToutputs = []
    for i in range(INPUTSTOTAL):
        inputTTList.append(i)
        print((list(map(str, list(set(inputTTList))))))
    for i in range(len(listOfGates)):
        gatesInList.append(listOfGates[i].type)
    print(gatesInList)

    TToutputs.append(gateNumtoName(gatesInList))
    print(TToutputs)
    return inputTTList, TToutputs

def circuitCrawling(listOFGates,TToutputs):
    temp_output_id = []
    temp_input_id = []
    temp_gate_id = []
    for i in listOFGates:   #start from output
        if i.type == 1:
            #for j in range(len(listOFGates)):
            try:
                #print(i.inputs[j].mated_to)
                temp_output_id.append(i)
            except:
                print('fail')
        elif i.type == 0:             #if input is reached, by this point a list of gates should be found
            #for j in range(len(listOFGates)):
            try:
                #print(i.outputs[j].mated_to)
                temp_input_id.append(i)
            except:
                    print('fail')
        else:                         #rest of gates added here
            try:
                # print(i.outputs[j].mated_to)
                temp_gate_id.append(i)
            except:
                print('fail')

    print(temp_output_id)
    print(temp_input_id)
    print(temp_gate_id)

    crawlerOutput = [temp_output_id, temp_input_id,temp_gate_id]
    return crawlerOutput
    #Look at gates inputs

def convertNumtoWord(gate_id):
    if gate_id == 2: return "and"
    elif gate_id == 3: return "or"
    elif gate_id == 4: return "not"
    elif gate_id == 5: return "nand"
    elif gate_id == 6: return "nor"
    elif gate_id == 7: return "xor"

def printTable(inputTTList, CrawlerOut):
    #print(CrawlerOut)
    #format crawler out
    #input1, operand, input2 = "","",""
    #expression = "%s %s %s"% (input1, operand, input2)
    formattedLabel = []
    #print(CrawlerOut[0])
    for i in CrawlerOut[2]:
        if i.type == 4:
            # print(i.type)
            gateName = convertNumtoWord(i.type)
            # print(gateName)
            # print(inputTTList)
            input1 = inputTTList[0]
            operand = gateName
            expression = "%s %s" % (operand, input1)
            print(expression)
            formattedLabel.append(expression)
        else:
            # print((list(map(str, list(set(formattedLabel))))))
            formattedLabel = (list(map(str, list(set(formattedLabel)))))
            #print(i.type)
            gateName = convertNumtoWord(i.type)
            print(gateName)
            #print(inputTTList)
            input1 = inputTTList[0]
            input2 = inputTTList[1]
            operand = gateName
            expression = "%s %s %s" % (input1, operand, input2)
            #print(expression)
            formattedLabel.append(expression)

        print(formattedLabel)
        #print((list(map(str, list(set(formattedLabel))))))
        #formattedLabel = (list(map(str, list(set(formattedLabel)))))


    table = ttg.Truths((list(map(str, list(set(inputTTList))))),formattedLabel)
    print(table)
