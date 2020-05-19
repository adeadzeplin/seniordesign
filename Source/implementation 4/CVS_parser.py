from CVS_circuit_creation import gateNumtoName
from Constants import INPUTSTOTAL
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
    temp_path = []
    temp_input_id = []
    for i in listOFGates:   #start from output
        if i.type == 1:
            for j in range(len(listOFGates)):
                try:
                    print(i.inputs[j].mated_to)
                    temp_path.append(i)
                except:
                    print('fail')
        elif i.type == 0:             #if input is reached, by this point a list of gates should be found
            for j in range(len(listOFGates)):
                try:
                    print(i.outputs[j].mated_to)
                    temp_input_id.append(i)
                except:
                    print('fail')
        else:                         #rest of gates added here
            pass

    print(temp_path)
    print(temp_input_id)

    crawlerOutput = [temp_path, temp_input_id]
    return crawlerOutput
    #Look at gates inputs

def convertNumtoWord(gate_id):
    if gate_id == 2: return "AND"
    elif gate_id == 3: return "OR"
    elif gate_id == 4: return "NOT"
    elif gate_id == 5: return "NAND"
    elif gate_id == 6: return "NOR"
    elif gate_id == 7: return "XOR"

def printTable(inputTTList, CrawlerOut):
    #print(CrawlerOut)
    #format crawler out
    input1, operand, input2 = "","",""
    expression = "%s %s %s"% (input1, operand, input2)
    formattedLabel = []
    for i in CrawlerOut[0]:
        print(i.gate_id)
        gateName = convertNumtoWord(i.gate_id)


    table = ttg.Truths((list(map(str, list(set(inputTTList))))),formattedLabel)
    print(table)
