import numpy as np
from LUCA.luca_circuit import Circuit
from LUCA.luca_functions import *


class EvolutionaryAlgorithm:

    def __init__(self, pop, gens):
        self.population_size = pop
        self.population = []
        self.new_population = []
        self.max_num_generations = gens

    def initialization(self):
        inputs = 2
        outputs = 2
        rows = 2
        columns = 2
        for i in range(self.population_size):
            attempt = Circuit(inputs, outputs, rows, columns)
            self.population.append(attempt)

    def selection(self):
        print("SELECT")

    def crossover(self):
        for i in range(0, self.population_size):
            parent1 = accept_reject(self.population_size, self.population)
            parent2 = accept_reject(self.population_size, self.population)
            child = Circuit(parent1.num_inputs, parent1.num_outputs, parent1.num_rows, parent1.num_columns)
            create_child(child, parent1, parent2)
            self.new_population.append(child)

    def mutation(self):
        mutation_rate = 0.10
        for i in self.new_population:
            mutate_flag = False
            mutate = np.random.uniform(0, 1)
            mutate_gate_index = np.random.randint(0, len(i.genes) - i.num_outputs)
            if mutate < mutation_rate:
                mutate_gate_length = len(i.genes[mutate_gate_index])
                for j in range(0, len(i.genes) - i.num_outputs):
                    if len(i.genes[j]) == mutate_gate_length and j != mutate_gate_index:
                        gt_1 = i.genes[mutate_gate_index][-1]
                        gt_2 = i.genes[j][-1]
                        i.genes[mutate_gate_index][-1] = gt_2
                        i.genes[j][-1] = gt_1
                        mutate_flag = True
                        break
                    else:
                        pass

    def termination(self):
        for i in self.population:
            if i.fitness == 1.0:
                print(i.genes)
                print(i.fitness)
                for j in i.stan_circuit:
                    j.g_print()
                return False
        return True
