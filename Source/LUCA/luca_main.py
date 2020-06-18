import luca_logic
from luca_simulation import Simulation


pop = 4
rows = 2
columns = 2
gens = 100
LUCA = Simulation(pop, rows, columns, gens)
LUCA.create_population()
for generation in range(LUCA.max_generations):
    for i in range(0, pop):
        LUCA.population[i].create_circuit(LUCA.num_circuit_inputs, LUCA.rows)
        LUCA.population[i].circuit_sim()
        LUCA.population[i].calc_fitness(luca_logic.half_adder)
        LUCA.population = LUCA.next_generation()
        if LUCA.population[i].fitness == 8:
            print("Max Fitness:", LUCA.population[i].fitness, 'ON GENERATION', generation)
            print(LUCA.population[i].genes)
            quit()
    print("Generation:", generation)
