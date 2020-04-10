import ttg
import gate_connector

def prop_delay_calc(gate_types):
    delay= 0
    for i in gate_types:
        if i == 'and':
            delay =delay + 5
        if i == 'or':
            delay =delay + 5
        if i == 'not':
            delay =delay + 1
        if i == 'nand':
            delay =delay + 6
        if i == 'nor':
            delay =delay + 6
        if i == 'xor':
            delay =delay + 8
    return delay

def list_check(list_input, input_want):
    for i in range(len(list_input)):
        if list_input[i] == input_want:
            return True
    return False

def input_only(expr_split):
    input_list = []
    gate_list = []
    for i in range(len(expr_split)):
        if expr_split[i] == 'and':
            gate_list.append('and')
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            if not list_check(input_list, expr_split[i + 1]):
                input_list.append(expr_split[i + 1])  # append right input

        if expr_split[i] == 'or':
            gate_list.append('or')
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            if not list_check(input_list, expr_split[i + 1]):
                input_list.append(expr_split[i + 1])  # append right input

        if expr_split[i].__contains__("~"):
            gate_list.append('not')
            if not list_check(input_list, expr_split[i]):
                input_list.append(expr_split[i])  # append left input

        if expr_split[i] == 'nand':
            gate_list.append('nand')
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            if not list_check(input_list, expr_split[i + 1]):
                input_list.append(expr_split[i + 1])  # append right input

        if expr_split[i] == 'nor':
            gate_list.append('nor')
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            if not list_check(input_list, expr_split[i + 1]):
                input_list.append(expr_split[i + 1])  # append right input

        if expr_split[i] == 'xor':
            gate_list.append('xor')
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            if not list_check(input_list, expr_split[i + 1]):
                input_list.append(expr_split[i + 1])  # append right input

    return input_list,gate_list

def expression_check(expression):
    print(expression)
    expr_split = expression.split()
    print(expr_split)

    for i in range(len(expr_split)):
        expr_split[i] = expr_split[i].replace("(", "")
        expr_split[i] = expr_split[i].replace(")", "")

    output_array =[]
    tt_array = []
    array_temp = []
    lists = input_only(expr_split)
    print(lists)
    print(ttg.Truths(lists[0], [expression]))
    table = ttg.Truths(lists[0], [expression])
    tbl = table.as_pandas()
    #print(tbl)
    for i in range(1,len(lists[0])**2):
        output_array.append(tbl[expression][i])
        array_temp = [None] * len(lists[0])
        for j in range(len(lists[0])):
            columns = lists[0][j]
            tbl_input = tbl[columns][i] #column
            array_temp[j] = tbl_input
        tt_array.append(array_temp)

    #print(output_array)
    #print(input_array)

    output_match = gate_connector.output_compare(output_array)
    #print(output_match)
    gate_connector.circuit_maker(lists[1],tt_array,lists[0])

    num_inputs = len(lists[0])
    num_gates = len(lists[1])
    prop_delay = prop_delay_calc(lists[1])
    print('prop delay:   ' + str(prop_delay))


expression = 'A and B or C'
#print(ttg.Truths(['A','B','C'], ['(~C)', expression]))
expression_check(expression)