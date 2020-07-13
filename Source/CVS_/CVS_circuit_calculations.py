import enum
from CVS_ import CVS_gate_class

def circuit_Metrics(listOfGates):
    renamed_list = []
    metrics = []
    for gate in listOfGates:
        renamed_list.append(gate.type)
    #print(renamed_list)

    metrics.append(total_Delay(renamed_list))
    metrics.append(total_Power(renamed_list))
    metrics.append(total_transistor(renamed_list))

    return metrics

def total_Power(renamed_list):
    esti_power = 0
    for i in renamed_list:
        if i == 0 or i == 1:  #inputs/outputs
            esti_power += 0
        elif i == 6:
            esti_power += 20  #uA
        elif i == 7:
            esti_power += 40  #uA
        elif i == 8:
            esti_power += 0  #LUCA space gate
        elif i == 9:
            esti_power += 40
        else:
            esti_power += 40  #uA
    return esti_power


def total_Delay(renamed_list):
    esti_delay = 0
    for i in renamed_list:
        if i == 0 or i == 1:
            esti_delay += 0
        elif i == 2:
            esti_delay += 8.5  # ns
        elif i == 3:
            esti_delay += 7
        elif i == 4 or i == 5:
            esti_delay += 6.5
        elif i == 6:
            esti_delay += 13
        elif i == 7:
            esti_delay += 12
        elif i == 8:  # LUCA space gate
            esti_delay += 0
        elif i == 9:
            esti_delay += 24
    return esti_delay

def total_transistor(renamed_list):
    transistor_num = 0
    for i in renamed_list:
        if i == 0 or i == 1:
            transistor_num += 0
        elif i == 2 or i == 3:
            transistor_num += 6
        elif i == 7:
            transistor_num += 8
        elif i == 4:
            transistor_num += 2
        elif i == 5 or i == 6:
            transistor_num += 4
        elif i == 8:  # LUCA space gate
            transistor_num += 0
        elif i == 9:
            transistor_num += 8
    return transistor_num

def circuit_connection_check(listofallgates):
    input_gate_counter = 0
    logic_gate_counter = 0
    output_gate_counter = 0

    #is there a circuit>???
    if listofallgates == []:
        return circuit_errors.ERROR_NO_CIRCUIT

    # checks if gates exist
    for gate in listofallgates:
        if gate.type == 0:
            input_gate_counter += 1
        elif gate.type == 1:
            output_gate_counter += 1
        else:
            logic_gate_counter += 1

    if input_gate_counter == 0:
        return circuit_errors.ERROR_MISSING_INPUT
    elif logic_gate_counter == 0:
        return circuit_errors.ERROR_MISSING_LOGIC
    elif output_gate_counter == 0:
        return circuit_errors.ERROR_MISSING_OUTPUT

    # checks is each gate has any inputs and outputs        #can simplify
    for gate in listofallgates:
        # if gate.type == 8:
        #     pass
        # else:
            # --------------- OUTPUTS --------------
        for j in range(len(gate.outputs)):
            if gate.type == 0:  # if  input gate does not have outputs
                if len(gate.outputs[j].mated_to) == 0:
                    return circuit_errors.ERROR_CIRCUIT_INPUT
                else:
                    pass  # print(gate.gate_id,gate.outputs[j].mated_to)
            elif gate.type == 4 or gate.type == 8:
                if len(gate.outputs[j].mated_to) == 0:
                    return circuit_errors.ERROR_CONNECTED_GATE_OUTPUT_MISSING
                # elif len(gate.inputs[j].mated_to) > 1:
                #     return circuit_errors.ERROR_MORE_THAN_2_MATED
                else:
                    pass
            elif gate.type != 1:
                if len(gate.outputs[j].mated_to) == 0:
                    return circuit_errors.ERROR_CONNECTED_GATE_OUTPUT_MISSING
                # elif len(gate.inputs[j].mated_to) > 2:
                #     return circuit_errors.ERROR_MORE_THAN_2_MATED
                else:
                    pass
                    # print(gate.gate_id,gate.inputs[j].mated_to,gate.outputs[j].mated_to)

        for k in range(len(gate.inputs)):
            # --------------- INPUTS --------------
            if gate.type == 1:  # if output gate have no inputs or more than 1 input
                if len(gate.inputs[k].mated_to) == 0 or len(gate.inputs[k].mated_to) > 1:
                    return circuit_errors.ERROR_CIRCUIT_OUTPUT
                else:
                    pass  # print(gate.gate_id,gate.inputs[k].mated_to)
            elif gate.type == 4 or gate.type == 8:
                if gate.inputs[k].mated_to == []:
                    # print(gate.inputs[k].mated_to)
                    # print("ERROR_GATE_MISSING_INPUTS")
                    return circuit_errors.ERROR_GATE_MISSING_INPUTS
                # elif len(gate.inputs[k].mated_to) == 1:
                #     return circuit_errors.ERROR_ONE_LOGIC_GATE_INPUT
                elif len(gate.inputs[k].mated_to) > 1:
                    # print("ERROR_MORE_THAN_2_MATED")
                    return circuit_errors.ERROR_MORE_THAN_2_MATED
            elif gate.type != 0:  # error check #1
                if gate.inputs[k].mated_to == []:
                    # print(gate.inputs[k].mated_to)
                    # print("ERROR_GATE_MISSING_INPUTS")
                    if gate.type == 99:
                        pass
                    else:
                        return circuit_errors.ERROR_GATE_MISSING_INPUTS
                # elif len(gate.inputs[k].mated_to) == 1:
                #     return circuit_errors.ERROR_ONE_LOGIC_GATE_INPUT
                elif len(gate.inputs[k].mated_to) > 2:
                    # print("ERROR_MORE_THAN_2_MATED")
                    return circuit_errors.ERROR_MORE_THAN_2_MATED

            #Circuit Recursion Check
            #Check if the current gate is connected to an output of a gate further down in the list
            #This is will casue the current gate to not receive an output array when it tries to calc logic
            # if gate.type == CVS_gate_class.ConnectorType.INPUT or gate.type == CVS_gate_class.ConnectorType.OUTPUT:
            #     pass
            # else:
            #     for gate2 in listofallgates:
            #         if gate2.type == CVS_gate_class.ConnectorType.INPUT or gate2.type == CVS_gate_class.ConnectorType.OUTPUT or gate2.type == 99:
            #             pass
            #         else:
            #             #print("position", listofallgates.index(gate))
            #             #print(gate.gate_id, gate2.gate_id)
            #             #for j in range(len(gate.inputs)):
            #             #print("inputs",gate.inputs[j].mated_to,gate2.inputs[j].mated_to,"outputs",gate.outputs[0].mated_to,gate2.outputs[0].mated_to)
            #             #print("id", gate.inputs[0]._ID,gate.inputs[1]._ID, gate2.outputs[0].mated_to)
            #             #print("gate2",gate2.outputs[0].mated_to[0], gate2.outputs[0].mated_to)
            #             #print("where",gate.inputs[0]._ID, gate2.outputs[0].mated_to, "tab", gate.inputs[1]._ID, gate2.outputs[0].mated_to)
            #             for input in gate.inputs:
            #                 for output in gate2.outputs[0].mated_to:
            #                     if input._ID == output:
            #                         if listofallgates.index(gate) < listofallgates.index(gate2)+2:
            #                             print("CVS recursion")
            #                             return circuit_errors.ERROR_CIRCUIT_LOOP

class circuit_errors(enum.Enum):
    # Circuit Error codes
    ERROR_CIRCUIT_INPUT = 10  # if input gate has no mated gates
    ERROR_CIRCUIT_OUTPUT = 20  # if output gate has no mated gates
    ERROR_GATE_IN = 30  # if gate doesnt have the right amount of mated inputs (1,2)
    ERROR_GATE_OUT = 30  # if gate doesnt have the right amount of mated outputs (1,2)
    ERROR_MISSING_INPUT = 40  # there are no input gates in the circuit
    ERROR_MISSING_LOGIC = 50  # there are no logic gates in the circuit
    ERROR_MISSING_OUTPUT = 60  # there are no output gates in the circuit
    ERROR_GATE_MISSING_INPUTS = 70  # gate has no mated gates
    ERROR_CONNECTED_GATE_OUTPUT_MISSING = 80
    ERROR_MORE_THAN_2_MATED = 90
    ERROR_NONE_MATED = 900
    ERROR_CIRCUIT_LOOP = 35
    ERROR_NO_CIRCUIT = 45



def circuit_output_compare(circuitOutput, ogOutput):
    counterRight = 0
    counterWrong = 0

    # print(circuitOutput,ogOutput)
    if  circuitOutput == []:
        return 0


    for i in range(len(ogOutput)):
        for j in range(len(ogOutput[i])):
            if len(circuitOutput[i]) != len(ogOutput[i]):  #if the output arrays are not the same size i.e [], just ignore
                counterWrong += 1
            else:
                if ogOutput[i][j] == circuitOutput[i][j]:  #check if the values are the same between wanted output vs AI output
                    counterRight += 1
                else:
                    counterWrong += 1

    return counterRight / (counterRight + counterWrong)

# [0,0] take first values from each output column and compare first values in og circuit out
# [0,1]


def table_column_get(tableInput_TableOut, circuitInput):
    tableColumn = []
    for q in range(len(tableInput_TableOut)):
        if len(tableInput_TableOut) == 1:  # one gate
            for k in range(1, len(tableInput_TableOut) + 2):
                # print(k,tableInput_TableOut[q][str(q)][k])
                tableColumn.append(tableInput_TableOut[q][str(q)][k])
            temp = tableColumn
            tableColumn = []
            circuitInput.append(temp)

        elif 2 ** len(tableInput_TableOut) <= 4:
            for k in range(1, 2 ** len(tableInput_TableOut) + 1):
                # print(k,tableInput_TableOut[q][str(q)][k])
                tableColumn.append(tableInput_TableOut[q][str(q)][k])
            temp = tableColumn
            tableColumn = []
            circuitInput.append(temp)
        else:
            for k in range(1, 2 ** len(tableInput_TableOut) + 1):
                # print(k,tableInput_TableOut[q][str(q)][k])
                tableColumn.append(tableInput_TableOut[q][str(q)][k])
            temp = tableColumn
            tableColumn = []
            circuitInput.append(temp)
    # print(circuitInput)
    return circuitInput


def table_output(a, b, gatetype):
    # print(a,b,gatetype)
    output = []
    # if a == [] or b==[]:
    #     output = []
    #     return output

    if gatetype == 2:
        for i in range(len(a)):
            if a[i] == 1 and b[i] == 1:
                output.append(1)
            else:
                output.append(0)
    elif gatetype == 3:
        for i in range(len(a)):
            if a[i] == 1 or b[i] == 1:
                output.append(1)
            else:
                output.append(0)
    elif gatetype == 4:
        for i in range(len(a)):
            tempnot = (not a[i])
            output.append(tempnot.real)
    elif gatetype == 5:
        for i in range(len(a)):
            if a[i] == 1 and b[i] == 1:
                output.append(0)
            else:
                output.append(1)
    elif gatetype == 6:
        for i in range(len(a)):
            if a[i] == 1 or b[i] == 1:
                output.append(0)
            else:
                output.append(1)
    elif gatetype == 7:
        for i in range(len(a)):
            if a[i] == b[i]:
                output.append(0)
            else:
                output.append(1)
    elif gatetype == 8:
        if a == []:
            output = b
        else:
            output = a
    elif gatetype == 9:
        for i in range(len(a)):
            if a[i] == b[i]:
                output.append(1)
            else:
                output.append(0)

    return output
#
# def gateNumtoName(listofGatesNum):
#     temp =[]
#     for i in range(len(listofGatesNum)):
#         if listofGatesNum[i] == 0:
#             temp.append("IN")
#         elif listofGatesNum[i] == 1:
#             temp.append("OUT")
#         elif listofGatesNum[i] == 2:
#             temp.append("AND")
#         elif listofGatesNum[i] == 3:
#             temp.append("OR")
#         elif listofGatesNum[i] == 4:
#             temp.append("NOT")
#         elif listofGatesNum[i] == 5:
#             temp.append("NAND")
#         elif listofGatesNum[i] == 6:
#             temp.append("NOR")
#         elif listofGatesNum[i] == 7:
#             temp.append("XOR")
#     return temp

# AND = 2
# OR = 3
# NOT = 4
# NAND = 5
# NOR = 6
# XOR = 7


class PrintClass():
    def __init__(self):
        self.recursion_depthCounter = 0
        pass

    def scancirc(self, scanedorder, gate_id, list_gates):
        # print(scanedorder)
        self.recursion_depthCounter += 1

        gate = None
        for i in list_gates:
            # print((i.gate_id , gate_id))
            if i.gate_id == gate_id:
                scanedorder.append((i.gate_id, i.type.name))
                gate = i
                break
        if gate == None:
            print('fuck')
        if self.recursion_depthCounter >= 100:
            print("recursive termination")
            recursion_error_flag = True
            return 'there was a circuit loop that caused a recursive error'
        # check if the gate has any inputs
        if len(gate.inputs) > 0:
            for inputport in gate.inputs:
                # check if input port has connections
                if len(inputport.mated_to) > 0:
                    for ngate in list_gates:
                        for outputport in ngate.outputs:
                            for matched_id in outputport.mated_to:
                                if matched_id == inputport._ID:
                                    self.scancirc(scanedorder, ngate.gate_id, list_gates)
                                    break

        return scanedorder


    def getfancyprintoutstring(self, listogates):
        arrow = ' -> '
        superlist = []
        recursion_error_flag = False
        for gate in listogates:
            megalist = []
            if gate.type == CVS_gate_class.GateType.circuitOutput:
                # megalist.append(self.scancirc(megalist,gate.gate_id))
                self.recursion_depthCounter = 0
                superlist.append(self.scancirc(megalist, gate.gate_id, listogates))
                if recursion_error_flag == True:
                    return 'there was a circuit loop that caused a recursive error'

        # print(superlist)
        theprintout = ''
        for logicout in superlist:
            if isinstance(logicout, str):
                theprintout += logicout
            else:
                for line in reversed(logicout):
                    if line[1] == CVS_gate_class.GateType.circuitOutput.name:
                        theprintout += f"CircOUT:{line[0]}"
                    elif line[1] == CVS_gate_class.GateType.circuitInput.name:
                        theprintout += f"CircIN:{line[0]}{arrow}"
                    else:
                        theprintout += f"{line[1]}:{line[0]}{arrow}"
                theprintout += "\n"

        return theprintout
