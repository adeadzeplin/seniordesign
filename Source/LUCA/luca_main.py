from LUCA.luca_evolutionary_algorithm import EvolutionaryAlgorithm

# 2 AND
# 3 OR
# 4 NOT
# 5 NAND
# 6 NOR
# 7 XOR
# 8 WIRE
# 9 XNOR


def main():
    generation = 1
    running = True
    population = 100
    generations = 10000
    allowed_gate_types = [2, 3, 4, 5, 6, 7, 8, 9]
    inputs = 3
    outputs = 2
    rows = 3
    columns = 3
    LUCA = EvolutionaryAlgorithm(population, generations)
    LUCA.initialization(allowed_gate_types, inputs, outputs, rows, columns)
    while running:
        print('GENERATION', generation)
        if not LUCA.new_population:
            pass
        else:
            LUCA.new_population.clear()
        LUCA.check_children()
        half_adder = [[0, 1, 1, 0], [0, 0, 0, 1]] # 2in 2out
        half_subtractor = [[0,1,1,0], [0,1,0,0]]    #2in 2out
        full_adder = [[0,1,1,0,1,0,0,1], [0,0,0,1,0,1,1,1]]     #3in 2out
        full_subtractor = [[0,1,1,0,1,0,0,1], [0,1,1,1,0,0,0,1]]    #3in 2out
        one_bit_comparator = [[0,1,0,0], [1,0,0,1], [0,0,1,0]]      #2in 3out
        two_bit_comparator = [[0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0],[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],[0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0]]    #4in 3out
        two_bit_multiplier = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0], [0,0,0,0,0,0,1,1,0,1,0,1,0,1,1,0], [0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1]] #4in 4out
        ogCircuitOutput = full_subtractor
        max_fit = LUCA.selection(ogCircuitOutput)
        print(max_fit)
        running = LUCA.termination(generation)
        generation += 1
        LUCA.crossover()
        #LUCA.mutation(allowed_gate_types)
        LUCA.test_mutation(allowed_gate_types)
        LUCA.check_children()
        LUCA.update_population()
        for j in range(len(LUCA.new_population)):
            LUCA.population[j] = LUCA.new_population[j]

if __name__ == '__main__':
    main()
