import numpy as np
import luca_functions

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
