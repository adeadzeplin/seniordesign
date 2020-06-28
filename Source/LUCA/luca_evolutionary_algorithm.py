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
        print("Define Circuit parameters")
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
        print('CROSS')

    def mutation(self):
        print("MUTATAT")

    def termination(self):
        print("TEREMINATOR")


    def crossover2(self, parent2):
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