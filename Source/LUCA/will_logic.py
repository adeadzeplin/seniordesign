import numpy as np
import func

half_adder = np.array([[0, 0, 0, 0],
                       [0, 1, 1, 0],
                       [1, 0, 1, 0],
                       [1, 1, 0, 1]], dtype=int)

full_adder = np.array([[0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1],
                       [0, 1, 0, 0, 1],
                       [0, 1, 1, 1, 0],
                       [1, 0, 0, 0, 1],
                       [1, 0, 1, 1, 0],
                       [1, 1, 0, 1, 0],
                       [1, 1, 1, 1, 1]], dtype=int)
# add gate counter within the sim to help with fitness scoring


def circuit_sim(population, pop_size, circuit_size):
    truth_table = np.zeros((pop_size, 4, 4), dtype=int)
    for k in range(0, pop_size):
        for j in range(0, 4):
            gate_inputs = func.input_select(j)
            a = gate_inputs[0]
            b = gate_inputs[1]
            run = circuit(population, pop_size, circuit_size, a, b)
            truth_table[k][j][0] = a            # input 1
            truth_table[k][j][1] = b            # input 2
            truth_table[k][j][2] = run[k][6]    # output 1
            truth_table[k][j][3] = run[k][7]    # output 2
    return truth_table


def circuit(population, pop_size, circuit_size, a, b):
    out = np.zeros((pop_size, 8), dtype=int)
    for k in range(0, pop_size):
        for i in range(0, circuit_size, 4):
            if i == (circuit_size - 2):
                fnl_out1 = population[k][i]
                fnl_out2 = population[k][i+1]
                out[k][fnl_out1] = out[k][4]
                out[k][fnl_out2] = out[k][5]
                break
            inp1 = population[k][i]
            if inp1 == 0:
                inp1 = a
            elif inp1 == 1:
                inp1 = b
            else:
                inp1 = out[k][inp1]
            inp2 = population[k][i+1]
            if inp2 == 0:
                inp2 = a
            elif inp2 == 1:
                inp2 = b
            else:
                inp2 = out[k][inp2]
            gate_type = population[k][i+2]
            otp = population[k][i+3]
            if gate_type == "AND":
                out[otp] = logic_and(inp1, inp2)
            elif gate_type == "OR":
                out[k][otp] = logic_or(inp1, inp2)
            elif gate_type == "NOT":
                out[k][otp] = logic_not(inp1)
            elif gate_type == "NOR":
                out[k][otp] = logic_nor(inp1, inp2)
            elif gate_type == "NAND":
                out[k][otp] = logic_nand(inp1, inp2)
            elif gate_type == "XOR":
                out[k][otp] = logic_xor(inp1, inp2)
            elif gate_type == "XNOR":
                out[k][otp] = logic_xnor(inp1, inp2)
            elif gate_type == "NOGATE":
                out[k][otp] = inp1
    return out


def logic_and(input1, input2):
    if input1 == 1 and input2 == 1:
        output = 1
        return output
    else:
        output = 0
        return output


def logic_or(input1, input2):
    if input1 == 1 or input2 == 1:
        output = 1
        return output
    else:
        output = 0
        return output


def logic_nor(input1, input2):
    if input1 == 0 and input2 == 0:
        output = 1
        return output
    elif input1 == 0 and input2 == 1:
        output = 0
        return output
    elif input1 == 1 and input2 == 0:
        output = 0
        return output
    elif input1 == 1 and input2 == 1:
        output = 0
        return output


def logic_not(input1):
    if input1 == 0:
        output = 1
        return output
    elif input1 == 1:
        output = 0
        return output


def logic_xor(input1, input2):
    if input1 != input2:
        output = 1
        return output
    else:
        output = 0
        return output


def logic_xnor(input1, input2):
    if input1 == input2:
        output = 1
        return output
    else:
        output = 0
        return output


def logic_nand(input1, input2):
    if input1 == 1 and input2 == 1:
        output = 0
        return output
    else:
        output = 1
        return output
