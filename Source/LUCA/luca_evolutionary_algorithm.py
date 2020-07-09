import numpy as np
from LUCA.luca_circuit import Circuit
from LUCA.luca_functions import *
from CVS_.CVS_parser import *
from CVS_.CVS_circuit_calculations import *
import CVS_.CVS_constants as con


class EvolutionaryAlgorithm:

    def __init__(self, pop, gens):
        self.population_size = pop
        self.population = []
        self.new_population = []
        self.max_num_generations = gens
        self.historical_fitness = []

    def initialization(self):
        inputs = 3
        outputs = 2
        con.OUTPUTSTOTAL = outputs
        con.INPUTSTOTAL = inputs
        rows = 4
        columns = 4
        for i in range(self.population_size):
            attempt = Circuit(inputs, outputs, rows, columns)
            self.population.append(attempt)

        for p in self.population:
            Gate.gate_id_counter = 0
            Connector.id = 0
            p.create_circuit_inputs()
            p.create_circuit_gates()
            p.create_circuit_outputs()
            if (p.num_rows - p.num_outputs) >= 1:
                p.create_dummy_gate()
                connect_gates_d(p.gate_list, p.stan_circuit, p.num_ports, p.output_list, p.dummy_list)
            else:
                connect_gates(p.gate_list, p.stan_circuit, p.num_ports, p.output_list)
            p.genes, p.gate_counter = create_genes(p.stan_circuit)

    def selection(self, ogCircuitOutput):
        temp = []
        for i in self.population:
            Circuit_Errors = circuit_connection_check(i.stan_circuit)
            if Circuit_Errors == None:
                i.fitness = runParser(i.stan_circuit, ogCircuitOutput)
                temp.append(i.fitness)
            else:
                print("Error: ", Circuit_Errors)
                i.fitness = 0
                temp.append(i.fitness)
                for j in i.stan_circuit:
                    j.g_print()
        self.historical_fitness.append(temp)

    def crossover(self):
        for i in range(0, self.population_size):
            parent1 = accept_reject(self.population_size, self.population)
            parent2 = accept_reject(self.population_size, self.population)
            child = Circuit(parent1.num_inputs, parent1.num_outputs, parent1.num_rows, parent1.num_columns)
            create_child(child, parent1, parent2)
            self.new_population.append(child)

    def mutation(self):
        print("MUTATION")
        mutation_rate = 0.20
        two_input_gates = [2, 3, 5, 6, 7, 9]
        one_input_gates = [4, 8]
        mutate_flag = True
        for i in self.new_population:
            mutate = np.random.uniform(0, 1)
            mutate_gate_index = np.random.randint(0, len(i.genes) - i.num_outputs)
            if mutate < mutation_rate:
                mutate_gate_length = len(i.genes[mutate_gate_index])
                if mutate_gate_length == 4:
                    while mutate_flag:
                        gate_loc = np.random.randint(0, len(two_input_gates))
                        gate_val = two_input_gates[gate_loc]
                        if gate_val != i.genes[mutate_gate_index][-1]:
                            i.genes[mutate_gate_index][-1] = gate_val
                            mutate_flag = False
                elif mutate_gate_length == 3:
                    while mutate_flag:
                        gate_loc = np.random.randint(0, len(one_input_gates))
                        gate_val = one_input_gates[gate_loc]
                        if gate_val != i.genes[mutate_gate_index][-1]:
                            i.genes[mutate_gate_index][-1] = gate_val
                            mutate_flag = False

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
                    print(i.fitness, 'NUM GATES IN CIRCUIT', i.gate_counter)
                    for j in i.stan_circuit:
                        j.g_print()
                        flag = False
            if flag is False:
                return flag
            else:
                flag = True
                return flag
