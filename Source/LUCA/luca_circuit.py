import numpy as np
from CVS_.CVS_gate_class import Gate
from LUCA.luca_functions import *


class Circuit:

    def __init__(self, i, o, r, c):
        self.fitness = 0
        self.genes = []
        self.stan_circuit = []
        self.num_inputs = i
        self.num_outputs = o
        self.num_rows = r
        self.num_columns = c
        self.num_gates = self.num_rows * self.num_columns
        self.num_dummy = 1
        if self.num_rows == self.num_outputs:
            self.num_dummy = 0
        self.num_ports = self.num_inputs + self.num_outputs + self.num_gates + self.num_dummy
        self.gate_list = []
        self.input_list = []
        self.output_list = []
        self.is_child = False
        self.cgp = [0, 0]
        self.dummy_list = []

    def create_circuit_inputs(self):
        for j in range(0, self.num_inputs):
            inp = Gate(0, 0, 1)
            inp.cgp_id = self.cgp
            self.cgp = define_input_cgp(self.cgp[0], self.cgp[1])
            self.stan_circuit.append(inp)
            self.input_list.append(inp)
            if j == self.num_inputs - 1:
                self.cgp = [0, 1]

    def create_circuit_gates(self):
        for k in range(0, self.num_gates):
            gate = create_gate(self.cgp)
            self.stan_circuit.append(gate)
            self.gate_list.append(gate)
            self.cgp = define_cgp(self.cgp[0], self.cgp[1], self.num_rows)

    def create_circuit_outputs(self):
        for j in range(0, self.num_outputs):
            out = Gate(1, 1, 0)
            out.cgp_id = self.cgp
            self.cgp = define_output_cgp(self.cgp[0], self.cgp[1])
            self.stan_circuit.append(out)
            self.output_list.append(out)

    def create_dummy_gate(self):
        dummy = Gate(99, (self.num_rows - self.num_outputs), 0)
        self.stan_circuit.append(dummy)
        self.dummy_list.append(dummy)
        dummy.cgp_id = self.cgp
        self.cgp = define_output_cgp(self.cgp[0], self.cgp[1])

