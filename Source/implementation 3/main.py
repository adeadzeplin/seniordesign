import ttg


def gate_Logic(input1,input2,gate):
    output = 0
    if gate == 1:
        output = input1 and input2
    elif gate == 2:
        output = input1 or input2
    elif gate == 3:
        output =  not input1
    elif gate == 4:
        output = not (input1 and input2)
    elif gate == 5:
        output = not (input1 and input2)
    elif gate == 6:
        if input1 and input2:
            output = 0
        else:
            output = 1
    #print(output)
    return output

# [ input1, input2, gate type, output ]

#half adder
w,h = 2,2
gate_Matrix = [[0 for x in range(w)] for y in range(h)]
gate_Matrix[0][0] = [1,2,1,1]
gate_Matrix[1][0] = [1,2,6,2]
#gate_Matrix[0][1] = [1,2,2,3]

print(gate_Matrix)

#full adder
#w,h = 3,2
#gate_Matrix = [[0 for x in range(w)] for y in range(h)]
#gate_Matrix[0][0] = [0,1,6,1]
#gate_Matrix[1][0] = [0,1,1,2]
#gate_Matrix[0][1] = [3,2,6,3]
#gate_Matrix[1][1] = [3,2,1,4]
#gate_Matrix[0][2] = [2,4,2,5]
#print(gate_Matrix)

output_Matrix = [[0 for x in range(w)] for y in range(h)]
print(output_Matrix)

num_inputs = []
num_outputs = []

#check max inputs
for x in range(h):
    for y in range(w):
        #check each num
        if gate_Matrix[x][y] == 0:
            pass
        else:
            for z in range(4):
                if z ==0:
                    #print('output ' + str(gate_Matrix[x][y][z]) + '\n')
                    num_inputs.append(gate_Matrix[x][y][z])
                if z ==1:
                    #print('output ' + str(gate_Matrix[x][y][z]) + '\n')
                    num_inputs.append(gate_Matrix[x][y][z])
#print(num_inputs)
#print(list(set(num_inputs)))
num_inputs_str = (list(map(str,list(set(num_inputs)))))


#check max outputs
for x in range(h):
    for y in range(w):
        #check each num
        if gate_Matrix[x][y] == 0:
            pass
        else:
            for z in range(4):
                if z ==3:
                    #print('output ' + str(gate_Matrix[x][y][z]) + '\n')
                    num_outputs.append(gate_Matrix[x][y][z])
#print(num_outputs)
#print(list(set(num_outputs)))
num_outputs_str = (list(map(str,list(set(num_outputs)))))


#create table
table = ttg.Truths(num_inputs_str)
print(table)





#matrix read logic
for x in range(h):
    for y in range(w):
        #check each num
        if gate_Matrix[x][y] == 0:
            pass
        else:
            output_Matrix[x][y] = gate_Logic(gate_Matrix[x][y][0],gate_Matrix[x][y][1],gate_Matrix[x][y][2])
        #for z in range(4):
         #   if z ==0:
          #      print('input1 ' + str(gate_Matrix[x][y][z]))
           # if z ==1:
            #    print('input2 ' + str(gate_Matrix[x][y][z]))
            #if z ==2:
            #    print('gate type '+ str(gate_Matrix[x][y][z]))
            #if z ==3:
            #    print('output ' + str(gate_Matrix[x][y][z]) + '\n')

print(output_Matrix)