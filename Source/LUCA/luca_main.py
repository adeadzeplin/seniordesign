import numpy as np
import LUCA.luca_logic
from LUCA.luca_simulation import Simulation
from CVS_ import CVS_main
from CVS_ import CVS_gate_class
from CVS_ import CVS_circuit_creation
from LUCA.luca_circuit import Circuit


def main():
    c = Circuit(9, 2)
    circ_inputs = []
    gates = []
    circ_outputs = []

    for j in range(0, 2):
        input = CVS_gate_class.Gate(0, 0, 1)
        c.circuits.append(input)
        circ_inputs.append(input)
    r, col = 2, 2
    cgp = [0, 0]

    for k in range(0, 4):
        gate = create_gate(cgp)
        print("CGP ID", gate.cgp_id)
        c.circuits.append(gate)
        #gates.append(gate)
        cgp = define_cgp(cgp, r, col)

    for j in range(0, 1):
        output = CVS_gate_class.Gate(0, 1, 0)
        c.circuits.append(output)
        circ_outputs.append(output)

    for g in c.circuits:
        print('CGP GATE', g.cgp_id)

    CVS_circuit_creation.Output_to_Input(c.circuits, 0, 2)
    CVS_circuit_creation.Output_to_Input(c.circuits, 1, 2)
    CVS_circuit_creation.Output_to_Input(c.circuits, 0, 3)
    CVS_circuit_creation.Output_to_Input(c.circuits, 2, 3)
    CVS_circuit_creation.Output_to_Input(c.circuits, 3, 4)

    for i in c.circuits:
        i.g_print()


def create_gate(cgp):
    if cgp[1] == 0:
        val = np.random.randint(2, 8)
    else:
        val = np.random.randint(2, 9)
    gate = CVS_gate_class.Gate(val)
    gate.set_cgp_id(cgp)
    return gate


def define_cgp(cgp, r, c):
    if cgp[0] == r - 1:
        if cgp[1] == c - 1:
            pass
        else:
            cgp[1] += 1
            cgp[0] = 0
    else:
        cgp[0] += 1
    return cgp


if __name__ == '__main__':
    main()








inputs = 2
outputs = 2
pop = 10
rows = 2
columns = 2
gens = 3
LUCA = Simulation(pop, rows, columns, gens, inputs, outputs)
LUCA.create_population()
for i in range(0, pop):
    LUCA.population[i].create_circuit(LUCA.num_circuit_inputs, LUCA.rows)

for generation in range(LUCA.max_generations):
    for i in range(0, pop):
        LUCA.population[i].circuit_sim()
        LUCA.population[i].calc_fitness(luca_logic.half_adder)
        #print(LUCA.population[i].gates, LUCA.population[i].connections)
        #print(LUCA.population[i].fitness, LUCA.population[i].genes)
        if LUCA.population[i].fitness == 8:
            print("Max Fitness:", LUCA.population[i].fitness, 'ON GENERATION', generation)
            print(LUCA.population[i].genes)
            quit()
    LUCA.population = LUCA.next_generation()
    print("Generation:", generation)
