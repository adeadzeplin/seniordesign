import numpy as np
from luca_circuit import Circuit


class Simulation:

    def __init__(self, pop, r, c, g):
        self.mutation_rate = 0
        self.pop_size = pop
        self.population = []
        self.max_generations = g
        self.num_circuit_inputs = 2
        self.rows = r
        self.columns = c
        self.num_gates = self.rows * self.columns
        self.circuit_size = (self.num_gates * 4) + 2
        self.newpop = []

    def create_population(self):
        for i in range(self.pop_size):
            self.population.append(Circuit(self.circuit_size, self.num_gates))

    def initialize_population(self):
        for i in range(self.pop_size):
            self.population[i].create_circuit(self.num_circuit_inputs, self.rows)

    def next_generation(self):
        for i in range(self.pop_size):
            parent1 = self.accept_reject()
            parent2 = self.accept_reject()
            child = parent1.crossover(parent2)
            child.mutate()
            self.newpop.append(child)
        return self.newpop

    def accept_reject(self):
        while True:
            index = np.random.randint(0, self.pop_size)
            partner = self.population[index]
            val = np.random.randint(0, 8)
            if val < partner.fitness * 8:
                return partner

