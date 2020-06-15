import numpy as np
import luca_logic
import luca_functions


class Circuit:

    def __init__(self, size, gates):
        self.circuit_size = size
        self.fitness = 0
        self.genes = np.zeros(18, dtype='object')
        self.num_gates = gates
        self.transistor_count = 0
        self.truth_table = np.zeros((4, 4), dtype=int)

    def gate_selector(self, gate_id):
        if gate_id[1] == 0:
            gt = np.random.randint(1, 8)
        else:
            gt = np.random.randint(1, 9)
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

    def input_selector(self, gate_id, gate_output):
        inputs = [0, 0]
        run, test = 1, 1
        if gate_id[1] == 0:  # on first column of gates
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

    def create_circuit(self, gate_output, rows):
        gate_id = [0, 0]
        for j in range(0, (self.num_gates * 4), 4):
            gate_type = self.gate_selector(gate_id)
            output = gate_output
            inputs = self.input_selector(gate_id, gate_output)
            self.genes[j] = inputs[0]
            self.genes[j+1] = inputs[1]
            self.genes[j+2] = gate_type
            self.genes[j+3] = output
            gate_output += 1
            gate_id[0] += 1
            if gate_id[0] == rows:
                gate_id[1] += 1
                gate_id[0] = 0
        self.genes[self.num_gates * 4] = gate_output
        self.genes[(self.num_gates * 4) + 1] = gate_output + 1

    def calc_fitness(self, half_adder):
        fit = 0
        for j in range(0, 4):
            if self.truth_table[j][2] == half_adder[j][2]:
                fit = fit + 1
            if self.truth_table[j][3] == half_adder[j][3]:
                fit = fit + 1
        self.fitness = fit

    def circuit_sim(self):
        for j in range(0, 4):
            gate_inputs = luca_functions.input_select(j)
            a = gate_inputs[0]
            b = gate_inputs[1]
            run = self.circuit(a, b)
            self.truth_table[j][0] = a  # input 1
            self.truth_table[j][1] = b  # input 2
            self.truth_table[j][2] = run[6]  # output 1
            self.truth_table[j][3] = run[7]  # output 2

    def circuit(self, a, b):
        out = np.zeros(8, dtype=int)
        for i in range(0, self.circuit_size, 4):
            if i == (self.circuit_size - 2):
                fnl_out1 = self.genes[i]
                fnl_out2 = self.genes[i + 1]
                out[fnl_out1] = out[4]
                out[fnl_out2] = out[5]
                break
            inp1 = self.genes[i]
            if inp1 == 0:
                inp1 = a
            elif inp1 == 1:
                inp1 = b
            else:
                inp1 = out[inp1]
            inp2 = self.genes[i + 1]
            if inp2 == 0:
                inp2 = a
            elif inp2 == 1:
                inp2 = b
            else:
                inp2 = out[inp2]
            gate_type = self.genes[i + 2]
            otp = self.genes[i + 3]
            if gate_type == "AND":
                out[otp] = luca_logic.logic_and(inp1, inp2)
            elif gate_type == "OR":
                out[otp] = luca_logic.logic_or(inp1, inp2)
            elif gate_type == "NOT":
                out[otp] = luca_logic.logic_not(inp1)
            elif gate_type == "NOR":
                out[otp] = luca_logic.logic_nor(inp1, inp2)
            elif gate_type == "NAND":
                out[otp] = luca_logic.logic_nand(inp1, inp2)
            elif gate_type == "XOR":
                out[otp] = luca_logic.logic_xor(inp1, inp2)
            elif gate_type == "XNOR":
                out[otp] = luca_logic.logic_xnor(inp1, inp2)
            elif gate_type == "NOGATE":
                out[otp] = inp1
        return out

    def crossover(self, parent2):
        child = Circuit(parent2.circuit_size, parent2.num_gates)
        midpoint = 7
        for j in range(0, self.circuit_size):
            if j > midpoint:
                child.genes[j] = self.genes[j]
            else:
                child.genes[j] = parent2.genes[j]
        return child

    def mutate(self):
        loc = np.random.randint(0, 16)
        #print(self.genes[loc])
