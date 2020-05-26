import enum

def Total_Power():
    pass


def Total_Delay():
    pass

def circuit_connection_check(listofallgates):
    for gate in listofallgates:
        for j in range(len(gate.outputs)):
            if gate.type == 0:
                if len(gate.outputs[j].mated_to) == 0 :
                    return circuit_errors.ERROR_CIRCUIT_INPUT
                else:
                    pass #print(gate.gate_id,gate.outputs[j].mated_to)
            else:
                if len(gate.outputs[j].mated_to) == 0 or len(gate.inputs[j].mated_to) > 2:
                    return circuit_errors.ERROR_GATE
                else:
                    pass #print(gate.gate_id,gate.inputs[j].mated_to,gate.outputs[j].mated_to)

        for k in range(len(gate.inputs)):
            if gate.type == 1:
                if len(gate.inputs[k].mated_to) == 0 or len(gate.inputs[k].mated_to) > 1:
                    return circuit_errors.ERROR_CIRCUIT_OUTPUT
                else:
                    pass #print(gate.gate_id,gate.inputs[k].mated_to)

class circuit_errors(enum.Enum):
    #Circuit Error codes
    ERROR_CIRCUIT_INPUT =1
    ERROR_CIRCUIT_OUTPUT =2
    ERROR_GATE =3



def table_column_get(tableInput_TableOut,circuitInput):
    tableColumn = []
    for q in range(len(tableInput_TableOut)):
        if len(tableInput_TableOut) ==1:
            for k in range(1, len(tableInput_TableOut) +2):
                #print(k,tableInput_TableOut[q][str(q)][k])
                tableColumn.append(tableInput_TableOut[q][str(q)][k])
            temp = tableColumn
            tableColumn = []
            circuitInput.append(temp)

        elif len(tableInput_TableOut)**2 <=4:
            for k in range(1, len(tableInput_TableOut) ** 2+1):
                # print(k,tableInput_TableOut[q][str(q)][k])
                tableColumn.append(tableInput_TableOut[q][str(q)][k])
            temp = tableColumn
            tableColumn = []
            circuitInput.append(temp)
        else:
            for k in range(1, len(tableInput_TableOut) ** 2):
                # print(k,tableInput_TableOut[q][str(q)][k])
                tableColumn.append(tableInput_TableOut[q][str(q)][k])
            temp = tableColumn
            tableColumn = []
            circuitInput.append(temp)
    print(circuitInput)
    return circuitInput

def table_output(a,b, gatetype):
    #print(a,b,gatetype)
    output = []

    if gatetype == 2 :
        for i in range(len(a)):
            if a[i] == 1 and b[i] == 1:
                output.append(1)
            else:
                output.append(0)
    elif gatetype == 3 :
        for i in range(len(a)):
            if a[i]==1 or b[i]==1:
                output.append(1)
            else:
                output.append(0)
    elif gatetype == 4 :
        for i in range(len(a)):
            output.append(not a[i])
    elif gatetype == 5 :
        for i in range(len(a)):
            if a[i] == 1 and b[i] == 1:
                output.append(0)
            else:
                output.append(1)
    elif gatetype == 6 :
        for i in range(len(a)):
            if a[i] == 1 or b[i] == 1:
                output.append(0)
            else:
                output.append(1)
    elif gatetype == 7 :
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