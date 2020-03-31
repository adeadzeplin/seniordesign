def table_check(i, circuit, output_list,input_array):
    #print(input_array)
        # set 1st input =0 reset 0, set 1st =0 set second = 1 rest zero, set 1st = 1, second = 0  rest zero, set 1st =1, second=1 rest zero....
    #this needs to be dynamic needs to know which inputs are occupied with outputs of other gates?
    #right now this just works for 'A + B' or 'A * B'
    if i == 0:
        x = 0
        y = 0
        circuit[0].C.monitor = 1
        circuit[0].A.set(x)
        circuit[0].B.set(y)
        output_list[i] = circuit[0].C.value
    elif i == 1:
        x = 1
        y = 0
        circuit[0].A.set(x)
        circuit[0].B.set(y)
        output_list[i] = circuit[0].C.value
    elif i == 2:
        x = 0
        y = 1
        circuit[0].A.set(x)
        circuit[0].B.set(y)
        output_list[i] = circuit[0].C.value
    elif i == 3:
        x = 1
        y = 1
        circuit[0].A.set(x)
        circuit[0].B.set(y)
        output_list[i] = circuit[0].C.value