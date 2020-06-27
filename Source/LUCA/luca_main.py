import numpy as np
from LUCA.luca_evolutionary_algorithm import EvolutionaryAlgorithm
from CVS_.CVS_gate_class import Gate, Connector
from LUCA.luca_circuit import *
from LUCA.luca_functions import connect_gates
from CVS_.CVS_circuit_calculations import circuit_connection_check
from CVS_.CVS_parser import runParser


def main():
    population = 1
    generations = 100
    LUCA = EvolutionaryAlgorithm(population, generations)
    LUCA.initialization()
    ogCircuitOutput = [[0, 1, 1, 0], [0, 0, 0, 1]]
    for p in LUCA.population:
        Gate.gate_id_counter = 0
        Connector.id = 0
        p.create_circuit_inputs()
        p.create_circuit_gates()
        p.create_circuit_outputs()
        p.create_dummy_gate()
        connect_gates(p.gate_list, p.stan_circuit, p.num_ports, p.output_list, p.dummy_list)
        for i in p.stan_circuit:
            i.g_print()
    for i in LUCA.population:
        Circuit_Errors = circuit_connection_check(i.stan_circuit)
        if Circuit_Errors == None:
            i.fitness = runParser(i.stan_circuit, ogCircuitOutput)
            print(i.fitness)
        else:
            print("Error: ", Circuit_Errors)

if __name__ == '__main__':
    main()
