import Gate_setup
import tablecheck
import ttg

def list_check(list_input, input_want):
    for i in range(len(list_input)):
        if list_input[i] == input_want:
            return True
    return False


def expression_check(expression):
    print(expression)
    expr_split = expression.split()
    print(expr_split)

    OR = "+"
    AND = "*"
    NOT = "!"
    Nand = "#"
    Nor = "$"
    Xor = "^"

    # input list function
    input_list = []
    gate_list = []
    for i in range(len(expr_split)):
        if expr_split[i] == '*':
            # check here
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            if not list_check(input_list, expr_split[i + 1]):
                input_list.append(expr_split[i + 1])  # append right input

        if expr_split[i] == '+':
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            if not list_check(input_list, expr_split[i + 1]):
                input_list.append(expr_split[i + 1])  # append right input

        if expr_split[i] == "!":
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            #if not list_check(input_list, expr_split[i + 1]):
                #input_list.append(expr_split[i + 2])  # append right input

        if expr_split[i] == '#':
            # check here
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            if not list_check(input_list, expr_split[i + 1]):
                input_list.append(expr_split[i + 1])  # append right input

        if expr_split[i] == '$':
            # check here
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            if not list_check(input_list, expr_split[i + 1]):
                input_list.append(expr_split[i + 1])  # append right input

        if expr_split[i] == '^':
            # check here
            if not list_check(input_list, expr_split[i - 1]):
                input_list.append(expr_split[i - 1])  # append left input
            if not list_check(input_list, expr_split[i + 1]):
                input_list.append(expr_split[i + 1])  # append right input

    #need to add paranthesis
    print(input_list)
    for i in range(1):
        # check for each operation and create gates and attach inputs to them
        #need to check for parathesis at some point before everything
        if AND in expr_split:
            #print("success")
            # start instantiation
            AND_total = 0
            for i in range(len(expr_split)):
                if expr_split[i] == '*':
                    # take words before and after + word and make instansiation withh dynamic names based on i val
                    name = 'A' + str(AND_total)
                    name = Gate_setup.And(name)
                    name.C.monitor = 0
                    name.A.set(expr_split[i - 1])
                    name.B.set(expr_split[i + 1])
                    gate_list.append(name)
                    AND_total = AND_total + 1
            #append a 'flag' value in gatelist to signal end of AND connection will need to add to other functions to check for flag and skip it
            #gate_list.append("and_end")
            # print(AND_total) #number of AND operations in given statement
        if OR in expr_split:
            #print("success")
            OR_total = 0
            for i in range(len(expr_split)):
                if expr_split[i] == '+':
                    name = 'O' + str(OR_total)
                    name = Gate_setup.Or(name)
                    name.C.monitor = 0
                    name.A.set(expr_split[i - 1])
                    name.B.set(expr_split[i + 1])
                    gate_list.append(name)
                    OR_total = OR_total +1
        # append a 'flag' value in gatelist to signal end of AND connection
        #gate_list.append("or_end")

        if Nand in expr_split:
            #print("success")
            Nand_total = 0
            for i in range(len(expr_split)):
                if expr_split[i] == '#':
                    name = 'NA' + str(Nand_total)
                    name = Gate_setup.Nand(name)
                    name.C.monitor = 0
                    name.A.set(expr_split[i - 1])
                    name.B.set(expr_split[i + 1])
                    gate_list.append(name)
                    Nand_total = Nand_total +1


        if Nor in expr_split:
            #print("success")
            Nor_total = 0
            for i in range(len(expr_split)):
                if expr_split[i] == '$':
                    name = 'NO' + str(Nor_total)
                    name = Gate_setup.Nor(name)
                    name.C.monitor = 0
                    name.A.set(expr_split[i - 1])
                    name.B.set(expr_split[i + 1])
                    gate_list.append(name)
                    Nor_total = Nor_total +1

        if Xor in expr_split:
            #print("success")
            Xor_total = 0
            for i in range(len(expr_split)):
                if expr_split[i] == '^':
                    name = 'XO' + str(Xor_total)
                    name = Gate_setup.Xor(name)
                    name.C.monitor = 0
                    name.A.set(expr_split[i - 1])
                    name.B.set(expr_split[i + 1])
                    gate_list.append(name)
                    Xor_total = Xor_total +1

        if NOT in expr_split:
            #print("success")
            NOT_total = 0
            for i in range(len(expr_split)):
                if expr_split[i] == '!':
                    name = 'N' + str(NOT_total)
                    name = Gate_setup.Not(name)
                    name.B.monitor = 0
                    name.A.set(expr_split[i ])
                    gate_list.append(name)
                    NOT_total = NOT_total +1

    circuit_build(input_list, gate_list,expression)
# combine created gates into one circuit
# connect output to inputs where needed

def circuit_build(input_list,gate_list,expression):
    circuit = []
    for i in range(len(gate_list)):
        print(gate_list[i].name + gate_list[i].A.value + gate_list[i].B.value + gate_list[i].C.value)

    for i in range(len(gate_list)):
        #print(i)
        if i+1 == len(gate_list):
            pass
        else:
            if gate_list[i].A.value == gate_list[i+1].B.value:
                print('-------------')
                gate_list[i].C.connect(gate_list[i-1].A)
                for i in range(len(gate_list)):
                    print(gate_list[i].name + gate_list[i].A.value + gate_list[i].B.value + gate_list[i].C.value)



    #print(gate_list[1].name)
    #connect outputs here
    #gate_list[0].C.connect(gate_list[1].A)
    for i in range(len(gate_list)):
        circuit.append(gate_list[i])
    in_out_test(input_list,circuit,expression)


# test inputs and outputs function, import final circuit
def in_out_test(input_list, circuit,expression):

    loop = (len(input_list)) ** 2
    output_list = [0 for x in range(loop)]
    #print(loop)
    print(output_list)
    input_list_length = len(input_list)
    input_array = [0 for x in range(input_list_length)]  # makes list with n indexes base don length of input array
    #print(ttg.Truths(input_list, ["A or C"]))
    for i in range(0,loop):
       tablecheck.table_check(i,circuit,output_list,input_list)

    # test each input value combination
    # i.e. A=0 B=0,A=1 B=0,A=0 B=1,A=1 B=1
    # make a table with varying inputs with output
    print(output_list)

expression = "A + C"
expression_check(expression)

# give it a boolean expression
# F = A * B' * C + A * B * C + (C + D)(D' + E)

# F = A + B
# F = A * B
# F = A' + B
# F = A' * B
# F = (A + B) + C
# F = A + (B * C)
# F = (A + B) * (A + B)

# Parse equation
# Check both sides of operation to see inputs for that gate
# F = output final output 1 or 0, which gets logged into a truth table txt
# * = AND if " * " instantiate AND gate with letters on each side as inputs
# + = OR if " + " instantiate OR gate with letters on each side as inputs
# ' = NOT if " ' " next to letter, then instantiate a NOT gate, then check one char over to see which gate to use
# () = if encounter para's,
#
# For each operation, instantiate a new gate


# Search for unique Letters
# Total of unique letters = num inputs
#

#OR = "+"
#AND = "*"
#NOT = "!"
#Nand = "#"
#Nor = "$"
#Xor = "^"