from LUCA.luca_evolutionary_algorithm import EvolutionaryAlgorithm
from LUCA.luca_circuit import *


def main():
    generation = 1
    running = True
    population = 40
    generations = 10000
    allowed_gate_types = [2, 3, 4, 5, 6, 7, 8, 9]
    LUCA = EvolutionaryAlgorithm(population, generations)
    LUCA.initialization(allowed_gate_types)
    while running:
        print('GENERATION', generation)
        if not LUCA.new_population:
            pass
        else:
            LUCA.new_population.clear()
        LUCA.check_children()
        half_adder = [[0, 1, 1, 0], [0, 0, 0, 1]]
        ogCircuitOutput = [[0,1,1,1,0],[1,0,0,0,0],[0,0,0,0,1]]
        two_bit_comparator = [[0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0],[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],[0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0]]
        ogCircuitOutput = half_adder
        max_fit = LUCA.selection(ogCircuitOutput)
        print(max_fit)
        running = LUCA.termination(generation)
        generation += 1
        LUCA.crossover()
        LUCA.mutation(allowed_gate_types)
        LUCA.check_children()
        LUCA.update_population()
        for j in range(len(LUCA.new_population)):
            LUCA.population[j] = LUCA.new_population[j]

if __name__ == '__main__':
    main()
