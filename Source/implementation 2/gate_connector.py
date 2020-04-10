import Gate_setup

AND = 1
OR = 2
NOT = 3
NAND = 4
NOR = 5
XOR = 6

gate_output = []


def output_compare(table_output):
    if table_output == gate_output:
        return True
    else:
        return False


def circuit_maker(gate_list, tt_list, input_list):
    named_gates = []
    # make gates/ connect gates and test each combo of inputs
    for i in range(len(gate_list)):
        gate_name = gate_list[i] + str(i)
        if gate_list[i] == 'not':
            pass
        else:
            if gate_list[i] == 'and':
                gate = Gate_setup.And(gate_name)
                gate.A.monitor = 1
                gate.B.monitor = 1
                gate.C.monitor = 1
                gate.A.set(input_list[i])
                gate.B.set(input_list[i+1])
                #print(gate.name)
                #print(gate.A.value)
                #print(gate.B.value)
                named_gates.append(gate)
                #make(tt_list, input_list, gate)
            if gate_list[i] == 'or':
                gate = Gate_setup.Or(gate_name)
                gate.A.monitor = 1
                gate.B.monitor = 1
                gate.C.monitor =1
                gate.A.set(input_list[i])
                gate.B.set(input_list[i + 1])
                #print(gate.A.value)
                #print(gate.B.value)
                named_gates.append(gate)
                #make(tt_list, input_list,gate)

    #named_gates[0].A.set(0)
    #named_gates[0].B.set(1)
    #named_gates[0].C.connect(named_gates[1].A)
    #named_gates[1].B.set(1)
    #print(named_gates[1].C.value)
    #quit()
#connect gates together
    connected = []
    for h in range(len(named_gates)-1):
        if len(named_gates) == 1:
            break
        elif named_gates[h].B.value == named_gates[h+1].A.value:
            named_gates[h].C.connect(named_gates[h+1].A)
            #print(named_gates[h].C.value)
            connected.append(named_gates[h+1].A)
            #print(connected[0].value)


    #print(named_gates[0].A.value)
    #print(named_gates[0].B.value)
    #print(named_gates[1].A.value)
    #print(named_gates[1].B.value)
    #named_gates[0].A.set(1)
    #named_gates[0].B.set(1)
    # named_gates[0].C.connect(named_gates[1].A)
    #named_gates[1].B.set(1)
    #print(named_gates[1].A.value)
    #print(named_gates[1].C.value)
    #quit()

#loops to get outp of circuit into array
    for o in range(len(tt_list)):
        for y in range(len(input_list)):
            for u in range(len(named_gates)):
                for r in range(len(connected)):
                    if named_gates[u].C.value == connected[r].value:
                        #print(named_gates[u].C.connects)
                        pass
                    else:
                        if named_gates[u].A.value == input_list[y]:
                            named_gates[u].A.set(tt_list[o][y])
                        elif named_gates[u].B.value == input_list[y]:
                            named_gates[u].B.set(tt_list[o][y])
        gate_output.append(named_gates[len(named_gates) - 1].C.value)

    print("gate output: " ,gate_output)
    print("gate list:   ", gate_list)
    print("input list:  ",input_list)
    print("Truth table: ",tt_list)

    #check for overlap?
def make(tt_list, input_list, gate):
    print(gate.name)
    for l in range(len(tt_list)):
        for j in range(len(input_list)):
            if gate.in1 == input_list[j]:
                gate.in1 = tt_list[l][j]
                print(gate.in1)
            if gate.in2 == input_list[j]:
                gate.in2 = tt_list[l][j]
                print(gate.in2)
        #print(gate.out)