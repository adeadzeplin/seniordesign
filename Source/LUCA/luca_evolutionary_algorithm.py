import numpy as np
from LUCA.luca_circuit import Circuit
from LUCA.luca_functions import *
from CVS_.CVS_parser import *
from CVS_.CVS_circuit_calculations import *


class EvolutionaryAlgorithm:

    def __init__(self, pop, gens):
        self.population_size = pop
        self.population = []
        self.new_population = []
        self.max_num_generations = gens

    def initialization(self, allowed_gate_types, inputs, outputs, r, c):
        inputs = inputs
        outputs = outputs
        rows = r
        columns = c
        for i in range(self.population_size):
            attempt = Circuit(inputs, outputs, rows, columns)
            self.population.append(attempt)

        for p in self.population:
            Gate.gate_id_counter = 0
            Connector.id = 0
            p.create_circuit_inputs()
            p.create_circuit_gates(allowed_gate_types)
            p.create_circuit_outputs()
            p.create_dummy_gate()
            connect_gates_d(p.gate_list, p.stan_circuit, p.num_ports, p.output_list, p.dummy_list)
            p.genes, p.gate_counter = create_genes(p.stan_circuit)

    def selection(self, ogCircuitOutput):
        max_fit = 0
        for i in self.population:
            Circuit_Errors = circuit_connection_check(i.stan_circuit)
            if Circuit_Errors == None:
                i.fitness = runLUCAParser(i.stan_circuit, ogCircuitOutput)
                #for j in i.stan_circuit:
                 #   j.g_print()
                if i.fitness > max_fit:
                    max_fit = i.fitness
            else:
                print("Error: ", Circuit_Errors)
                i.fitness = 0
                #for j in i.stan_circuit:
                    #j.g_print()
        return max_fit

    def crossover(self):
        for i in range(0, self.population_size):
            parent1 = accept_reject(self.population_size, self.population)
            parent2 = accept_reject(self.population_size, self.population)
            child = Circuit(parent1.num_inputs, parent1.num_outputs, parent1.num_rows, parent1.num_columns)
            create_child(child, parent1, parent2)
            self.new_population.append(child)
        convert_form(self.new_population, parent1)

    def mutation(self, allowed_gate_types):
        mutation_rate = 0.05
        two_input_gates = [2, 3, 5, 6, 7, 9]
        one_input_gates = [4, 8]
        mutate_flag = True
        gate_flag = True
        for i in self.new_population:
            mutate = np.random.uniform(0, 1)
            mutate_gate_index = np.random.randint(0, len(i.genes) - i.num_outputs - i.num_dummy)
            if mutate < mutation_rate:
                mutate_gate_length = len(i.genes[mutate_gate_index])
                if mutate_gate_length == 4:
                    while mutate_flag:
                        while gate_flag:
                            gate_loc = np.random.randint(0, len(two_input_gates))
                            gate_val = two_input_gates[gate_loc]
                            for gt in allowed_gate_types:
                                if gate_val == gt:
                                    if gate_val != i.genes[mutate_gate_index][-1]:
                                        i.genes[mutate_gate_index][-1] = gate_val
                                        mutate_flag = False
                                        gate_flag = False
                elif mutate_gate_length == 3:
                    while mutate_flag:
                        while gate_flag:
                            gate_loc = np.random.randint(0, len(one_input_gates))
                            gate_val = one_input_gates[gate_loc]
                            for gt in allowed_gate_types:
                                if gate_val == gt:
                                    if gate_val != i.genes[mutate_gate_index][-1]:
                                        i.genes[mutate_gate_index][-1] = gate_val
                                        mutate_flag = False
                                        gate_flag = False

    def termination(self, generation):
        flag = True
        if generation == self.max_num_generations:
            print("MAX GEN LIMIT REACHED")
            flag = False
            return flag
        else:
            for i in self.population:
                if i.fitness == 1.0:
                    print("GENERATION:", generation)
                    print(i.genes)
                    print('NUM GATES IN CIRCUIT', i.gate_counter)
                    for j in i.stan_circuit:
                        j.g_print()
                        flag = False
            if flag is False:
                return flag
            else:
                flag = True
                return flag

    def update_population(self):
        for i in range(self.population_size):
            self.population[i].genes.clear()

    def check_children(self):
        for j in self.population:
            for k in j.stan_circuit:
                if k.type != 0 and k.type != 1 and k.type != 99:
                    for i in k.outputs:
                        if not i.mated_to:
                            j.dummy_list[0].makePorts(1, 0)
                            Output_to_Input(j.stan_circuit, k.gate_id, j.num_ports - 1)

    def test_mutation(self, allowed_gate_types):
        mutation_rate = 0.10
        gates = [2, 3, 4, 5, 6, 7, 8, 9]
        mutate_flag = True
        gate_flag = True
        for i in self.new_population:
            mutate = np.random.uniform(0, 1)
            mutate_gate_index = np.random.randint(0, len(i.genes) - i.num_outputs - i.num_dummy)
            if mutate < mutation_rate:
                mutate_gate_length = len(i.genes[mutate_gate_index])
                while mutate_flag:
                    while gate_flag:
                        gate_loc = np.random.randint(0, len(gates))
                        gate_val = gates[gate_loc]
                        for gt in allowed_gate_types:
                            if gate_val == gt:
                                if gate_val != i.genes[mutate_gate_index][-1]:
                                    if mutate_gate_length == 4 and gate_val != 4 and gate_val != 8:
                                        #print(i.genes)
                                        i.genes[mutate_gate_index][-1] = gate_val
                                        mutate_flag = False
                                        gate_flag = False
                                        #print('mutated')
                                        #print(i.genes)
                                    elif mutate_gate_length == 4 and (gate_val == 4 or gate_val == 8):
                                        #print(i.genes)
                                        i.genes[mutate_gate_index][-1] = gate_val
                                        delinp = np.random.randint(0,2)
                                        del i.genes[mutate_gate_index][delinp]
                                        mutate_flag = False
                                        gate_flag = False
                                        #print('mutated2')
                                        #print(i.genes)
                                    elif mutate_gate_length == 3 and (gate_val == 4 or gate_val == 8):
                                        #print(i.genes)
                                        i.genes[mutate_gate_index][-1] = gate_val
                                        mutate_flag = False
                                        gate_flag = False
                                        #print('mutated3')
                                        #print(i.genes)
                                    elif mutate_gate_length == 3 and gate_val != 4 and gate_val != 8:
                                        #print(i.genes)
                                        input1 = i.genes[mutate_gate_index][0]
                                        input_flag = True
                                        id = i.genes[mutate_gate_index][-2]
                                        for j in i.stan_circuit:
                                            if j.gate_id == id:
                                                g_cgp = j.cgp_id
                                        while input_flag:
                                            input2 = np.random.randint(0, id)
                                            for j in i.stan_circuit:
                                                if j.gate_id == input2:
                                                    g2_cgp = j.cgp_id
                                                    if g_cgp[1] > g2_cgp[1] and input2 != input1:
                                                        input_flag = False
                                                        #print(id, input2, g_cgp, g2_cgp)
                                                        i.genes[mutate_gate_index][-1] = gate_val
                                                        i.genes[mutate_gate_index].insert(0, input2)
                                                        mutate_flag = False
                                                        gate_flag = False
                                                        #print('mutated4')
                                                        #print(i.genes)
                                                        break
                                                    else:
                                                        input_flag = True
