import enum
import numpy as np


def Total_Power():
    pass


def Total_Delay():
    pass


def circuit_connection_check(listofallgates):
    input_gate_counter = 0
    logic_gate_counter = 0
    output_gate_counter = 0

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
        for j in range(len(gate.outputs)):
            if gate.type == 0:
                if len(gate.outputs[j].mated_to) == 0:
                    return circuit_errors.ERROR_CIRCUIT_INPUT
                else:
                    pass  # print(gate.gate_id,gate.outputs[j].mated_to)
            elif gate.type != 1:
                if len(gate.outputs[j].mated_to) == 0 or len(gate.inputs[j].mated_to) > 2:
                    return circuit_errors.ERROR_GATE
                else:
                    pass  # print(gate.gate_id,gate.inputs[j].mated_to,gate.outputs[j].mated_to)

        for k in range(len(gate.inputs)):
            if gate.type == 1:
                if len(gate.inputs[k].mated_to) == 0 or len(gate.inputs[k].mated_to) > 1:
                    return circuit_errors.ERROR_CIRCUIT_OUTPUT
                else:
                    pass  # print(gate.gate_id,gate.inputs[k].mated_to)


class circuit_errors(enum.Enum):
    # Circuit Error codes
    ERROR_CIRCUIT_INPUT = 10        #if input gate has no mated gates
    ERROR_CIRCUIT_OUTPUT = 20       #if output gate has no mated gates
    ERROR_GATE = 30                 #if gate doesnt have the right amount of mated inputs and outputs (1,2)
    ERROR_MISSING_INPUT = 40        #there are no input gates in the cirucit
    ERROR_MISSING_LOGIC = 50        #there are no gates in the cirucit
    ERROR_MISSING_OUTPUT = 60       #there are no output gates in the cirucit
    ERROR_GATE_MISSING_INPUTS = 70  #gate has no mated gates


def circuit_output_compare(circuitOutput, ogOutput):
    counterRight = 0
    counterWrong = 0
    counterLen = 0
    tempCircuitOutput = circuitOutput
    same_counter = 0

    # for u in ogOutput:
    #     counterLen += len(u)
    #
    # for k in ogOutput:
    #     for p in tempCircuitOutput:
    #         if k == p:
    #             counterRight += len(p)
    #             same_counter +=1
    #             #tempCircuitOutput.pop((tempCircuitOutput.index(p)))
    # if counterRight == counterLen :
    #     return counterRight/counterLen

    for i in range(len(ogOutput)):
        for j in range(len(ogOutput[i])):
            #sprint(ogOutput[i][j])
            if len(circuitOutput[i]) != len(ogOutput[i]):   #if the output arrays are not the same size i.e [], just ignore
                counterWrong += 1
            else:
                if ogOutput[i][j] == circuitOutput[i][j]:   #check if the values are the same between wanted output vs AI output
                    counterRight += 1
                else:
                    counterWrong += 1

    return counterRight / (counterRight + counterWrong)

# [0,0] take first values from each output column and compare first values in og circuit out
# [0,1]


def table_column_get(tableInput_TableOut, circuitInput):
    tableColumn = []
    for q in range(len(tableInput_TableOut)):
        if len(tableInput_TableOut) == 1:       #one gate
            for k in range(1, len(tableInput_TableOut) + 2):
                # print(k,tableInput_TableOut[q][str(q)][k])
                tableColumn.append(tableInput_TableOut[q][str(q)][k])
            temp = tableColumn
            tableColumn = []
            circuitInput.append(temp)

        elif 2**len(tableInput_TableOut) <= 4:
            for k in range(1, 2**len(tableInput_TableOut) + 1):
                #print(k,tableInput_TableOut[q][str(q)][k])
                tableColumn.append(tableInput_TableOut[q][str(q)][k])
            temp = tableColumn
            tableColumn = []
            circuitInput.append(temp)
        else:
            for k in range(1, 2**len(tableInput_TableOut)+1):
                # print(k,tableInput_TableOut[q][str(q)][k])
                tableColumn.append(tableInput_TableOut[q][str(q)][k])
            temp = tableColumn
            tableColumn = []
            circuitInput.append(temp)
    #print(circuitInput)
    return circuitInput


def table_output(a, b, gatetype):
    # print(a,b,gatetype)
    output = []

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

    return output


    # AND = 2
    # OR = 3
    # NOT = 4
    # NAND = 5
    # NOR = 6
    # XOR = 7
