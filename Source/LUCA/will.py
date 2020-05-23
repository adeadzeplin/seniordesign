import numpy as np
import func

#   AND     1
#   OR      2
#   NOT     3
#   NOR     4
#   NAND    5
#   XOR     6
#   XNOR    7
#   NOGATE  8


def calc_fitness(tt, pop_size, half_adder):
    fitness = np.zeros(pop_size, dtype=int)
    for i in range(0, pop_size):
        fit = 0
        for j in range(0, 4):
            if tt[i][j][2] == half_adder[j][2]:
                fit = fit + 1
            if tt[i][j][3] == half_adder[j][3]:
                fit = fit + 1
        fitness[i] = fit
    return fitness


def selection(fitness, population, num_parents, circuit_size):
    parents = np.empty([num_parents, circuit_size], dtype="object")            # empty array for parents to be stored
    for num in range(num_parents):
        fitness_value = np.where(fitness == np.max(fitness))    # find max fitness value of the population
        parents[num] = population[fitness_value[0][0]]          # store the member genotype with the highest fitness as parent
        fitness[fitness_value[0][0]] = 0                        # set the fitness of that member to 0 so it is not selected again
        np.random.permutation(parents)
    return parents


def crossover(parents, num_offspring, circuit_size):
    offspring = np.empty([num_offspring, circuit_size], dtype="object")
    j, k = 0, 1
    for i in range(0, num_offspring):
        if i % 2 == 0:  # if even
            offspring[i, 0:7] = parents[j, 0:7]
            offspring[i, 7:] = parents[j + 1, 7:]
            j = j+1
        elif i % 2 == 1:  # if odd
            offspring[i, 0:7] = parents[k, 0:7]
            offspring[i, 7:] = parents[k - 1, 7:]
            k = k + 1
    return offspring


def mutation(offspring):
    for i in range(len(offspring)):
        mutate_chance = np.random.rand()                            # random float between 0 - 1
        gate_change = np.random.choice([2, 6, 10, 14])               # which gate will be changed if mutation occurs
        if mutate_chance <= 0.20:       # 10% chance of mutation occurring
            new_gate = np.random.randint(1, 9)  # randomly pick a new gate to use
            offspring[i, gate_change] = new_gate
    return offspring


def next_generation(parents, mutated_offspring):
    population = np.vstack((parents, mutated_offspring))
    return population
