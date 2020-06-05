
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



