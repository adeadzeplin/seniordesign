import numpy as np


def initial_population(pop, circ_inp, rows, num_gates):
    array_size = (num_gates * 4) + 2
    population = np.zeros((pop, array_size), dtype='object')
    for k in range(pop):
        gate_id = [0, 0]
        gate_output = circ_inp
        for i in range(0, (num_gates * 4), 4):
            population[k][i + 2] = gate_selector(gate_id)
            population[k][i + 3] = gate_output
            inputs = input_selector(gate_id, gate_output)
            population[k][i] = inputs[0]
            population[k][i + 1] = inputs[1]

            gate_output += 1
            gate_id[0] += 1
            if gate_id[0] == rows:
                gate_id[1] += 1
                gate_id[0] = 0
        population[k][num_gates * 4] = gate_output
        population[k][(num_gates * 4) + 1] = gate_output + 1
    return population


def input_select(j):
    gate_inputs = [0, 0]
    if j == 0:
        gate_inputs[0] = 0
        gate_inputs[1] = 0
    elif j == 1:
        gate_inputs[0] = 0
        gate_inputs[1] = 1
    elif j == 2:
        gate_inputs[0] = 1
        gate_inputs[1] = 0
    elif j == 3:
        gate_inputs[0] = 1
        gate_inputs[1] = 1
    return gate_inputs


def gate_selector(gate_id):
    if gate_id[1] == 0:
        gt = np.random.randint(0, 8)
    else:
        gt = np.random.randint(0, 9)
    if gt == 1:
        gt = 'AND'
    elif gt == 2:
        gt = 'OR'
    elif gt == 3:
        gt = 'NOT'
    elif gt == 4:
        gt = 'NOR'
    elif gt == 5:
        gt = 'NAND'
    elif gt == 6:
        gt = 'XOR'
    elif gt == 7:
        gt = 'XNOR'
    elif gt == 8:
        gt = 'NOGATE'
    return gt


def input_selector(gate_id, gate_output):
    inputs = [0, 0]
    run = 1
    test = 1
    if gate_id[1] == 0:     # on first column of gates
        inputs[0] = np.random.randint(0, 2)
        if inputs[0] == 0:
            inputs[1] = 1
        else:
            inputs[1] = 0
    else:
        while test:
            if gate_id[0] != 0:
                gate_id[0] -= gate_id[0]
                gate_output -= 1
            else:
                test = 0
        inputs[0] = np.random.randint(0, gate_output)
        inputs[1] = np.random.randint(0, gate_output)
        while run:
            if inputs[1] == inputs[0]:
                inputs[1] = np.random.randint(0, gate_output)
            else:
                run = 0
    return inputs


def mutated_gate(gt):
    if gt == 1:
        gt = 'AND'
    elif gt == 2:
        gt = 'OR'
    elif gt == 3:
        gt = 'NOT'
    elif gt == 4:
        gt = 'NOR'
    elif gt == 5:
        gt = 'NAND'
    elif gt == 6:
        gt = 'XOR'
    elif gt == 7:
        gt = 'XNOR'
    elif gt == 8:
        gt = 'NOGATE'
    return gt