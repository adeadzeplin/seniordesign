import luca_logic
from luca_simulation import Simulation
from CVS_ import CVS_main


pop = 10
rows = 2
columns = 2
gens = 100
LUCA = Simulation(pop, rows, columns, gens)
LUCA.create_population()


for generation in range(LUCA.max_generations):
    for i in range(0, pop):
        LUCA.population[i].create_circuit(LUCA.num_circuit_inputs, LUCA.rows)
        #LUCA.population[i].circuit_sim()
        #LUCA.population[i].calc_fitness(luca_logic.half_adder)
        #print(LUCA.population[i].gates, LUCA.population[i].connections)
        LUCA.population[i].fitness = CVS_main.CVS(LUCA.population[i].gates, LUCA.population[i].connections)
        #print(LUCA.population[i].fitness)
        if LUCA.population[i].fitness == 1.0:
            print("Max Fitness:", LUCA.population[i].fitness, 'ON GENERATION', generation)
            print(LUCA.population[i].genes)
            quit()
    LUCA.population = LUCA.next_generation()
    print("Generation:", generation)
