from LUCA.luca_evolutionary_algorithm import EvolutionaryAlgorithm
from LUCA.luca_circuit import *


def main():
    generation = 1
    running = True
    while running:
        print('GENERATION', generation)
        population = 20
        generations = 100
        LUCA = EvolutionaryAlgorithm(population, generations)
        LUCA.initialization()
        #ogCircuitOutput = [[0, 1, 1, 0], [0, 0, 0, 1]]
        #ogCircuitOutput = [[0,1,1,1,0],[1,0,0,0,0],[0,0,0,0,1]]
        ogCircuitOutput = [[0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0],[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],[0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0]]
        LUCA.selection(ogCircuitOutput)
        running, max_fit, avg_fit = LUCA.termination(generation)
        print('Max Fitness:', max_fit, 'Average Fitness:', avg_fit)
        generation += 1
        LUCA.crossover()
        LUCA.mutation()
        LUCA.population = LUCA.new_population
        convert_form(LUCA.population)


if __name__ == '__main__':
    main()
