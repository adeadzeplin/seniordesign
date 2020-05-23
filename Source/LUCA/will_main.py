import numpy as np
import will
import will_logic
import func


class Simulation:
    def __init__(self, pop, gen, col,  row):
        self.pop_size = pop
        self.columns = col
        self.rows = row
        self.num_gates = self.columns * self.rows
        self.num_parents = self.pop_size * 0.40
        self.num_offspring = self.pop_size * 0.60
        self.num_generations = gen
        self.population = []
        self.circuit_size = (self.num_gates * 4) + 2
        self.num_circuit_inputs = 2


def main(run_sim):
    while run_sim:
        LUCA = Simulation(pop=30, gen=1000, col=2, row=2)
        population = func.initial_population(LUCA.pop_size, LUCA.num_circuit_inputs, LUCA.rows, LUCA.num_gates)
        for generation in range(LUCA.num_generations):
            tt = will_logic.circuit_sim(population, LUCA.pop_size, LUCA.circuit_size)
            print("----------------------------")
            print("Generation:", generation)
            fitness = will.calc_fitness(tt, LUCA.pop_size, will_logic.half_adder)
            print("Fitness Scores\n", fitness)
            avg = np.mean(fitness)
            print("Average Fitness", avg)
            max_fit = max(fitness)
            if max_fit == 8:
                solution = np.where(fitness == 8)
                print("----------------------------")
                print("Solution found on Generation:", generation)
                for s in solution:
                    for i in s:
                        print("\tProposed circuit is:", population[i])
                        run_sim = False
                break
            parents = will.selection(fitness, population, int(LUCA.num_parents), LUCA.circuit_size)
            offspring = will.crossover(parents, int(LUCA.num_offspring), LUCA.circuit_size)
            mutated_offspring = will.mutation(offspring)
            population = will.next_generation(parents, mutated_offspring)
            if generation == LUCA.num_generations - 1:
                print("----------------------------")
                print("End of Simulation")
                print("\tMax Fitness found:", max(fitness))
                print("----------------------------")
                run_sim = False


if __name__ == '__main__':
    main(run_sim=1)
