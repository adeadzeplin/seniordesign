from LUCA.luca_evolutionary_algorithm import EvolutionaryAlgorithm
from LUCA.luca_circuit import *


def main():
    generation = 1
    running = True
    while running:
        print('GENERATION', generation)
        population = 100
        max_generations = 100
        LUCA = EvolutionaryAlgorithm(population, max_generations)
        LUCA.initialization()
        ogCircuitOutput = [[0, 1, 1, 0], [0, 0, 0, 1]]
        #ogCircuitOutput = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         #                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
         #                   [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
          #                  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1]]

        #ogCircuitOutput = [[0,1,0,0], [1,0,0,1], [0,0,1,0]]
        LUCA.selection(ogCircuitOutput)
        running = LUCA.termination(generation)
        generation += 1
        LUCA.crossover()
        LUCA.mutation()
        LUCA.population = LUCA.new_population
        convert_form(LUCA.population)

if __name__ == '__main__':
    main()