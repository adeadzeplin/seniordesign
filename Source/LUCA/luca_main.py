import numpy as np
from LUCA.luca_evolutionary_algorithm import EvolutionaryAlgorithm
from CVS_.CVS_gate_class import Gate, Connector
from LUCA.luca_circuit import *
from LUCA.luca_functions import connect_gates
from CVS_.CVS_circuit_calculations import circuit_connection_check
from CVS_.CVS_parser import runLUCAParser


def main():
    generation = 1
    running = True
    while running:
        print('GENERATION', generation)
        population = 20
        generations = 100
        LUCA = EvolutionaryAlgorithm(population, generations)
        LUCA.initialization()
        #ogCircuitOutput = [[1, 0, 0, 1, 0, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 0]]
        ogCircuitOutput = [[0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0],[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],[0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0]]
        LUCA.selection(ogCircuitOutput)
        running = LUCA.termination(generation)
        generation += 1
        LUCA.crossover()
        LUCA.mutation()
        LUCA.population = LUCA.new_population
        convert_form(LUCA.population)


if __name__ == '__main__':
    main()
