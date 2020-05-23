def Total_Power():
    pass


def Total_Delay():
    pass

def table_column_get(tableInput_TableOut,circuitInput):
    tableColumn = []
    for q in range(len(tableInput_TableOut)):
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