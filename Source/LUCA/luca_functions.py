import numpy as np
from CVS_.CVS_gate_class import Gate
from CVS_.CVS_circuit_creation import Output_to_Input


def define_input_cgp(cgp0, cgp1):
    output = [cgp0, cgp1]
    output[0] += 1
    return output


def define_output_cgp(cgp0, cgp1):
    output = [cgp0, cgp1]
    output[0] += 1
    return output


def define_cgp(cgp0, cgp1, row):
    output = [cgp0, cgp1]
    if cgp0 == row - 1:
        output[1] += 1
        output[0] = 0
    else:
        output[0] += 1
    return output


def create_gate(cgp):
    if cgp[1] == 0:
        val = np.random.randint(2, 8)
    else:
        val = np.random.randint(2, 9)
    gate = Gate(val)
    gate.cgp_id = cgp
    return gate


def connect_gates(gates, circuit, ports, output_list, dummy_list):
    dummy_id = dummy_list[0].gate_id
    for g in gates:
        if g.inputnum == 2:
            input_1 = g.inputs[0]
            input_2 = g.inputs[1]
            output_1 = g.outputs[0]
            connect_2_input_gates(input_1, input_2, output_1, circuit, ports, g, output_list, dummy_id)
        else:
            input_1 = g.inputs[0]
            output_1 = g.outputs[0]
            connect_1_input_gates(input_1, output_1, circuit, ports, g, output_list, dummy_id)


def connect_2_input_gates(input_1, input_2, output_1, circuit, ports, g, output_list, dummy_id):
    incomplete = 1
    outcheck = 1
    check = 1
    check2 = 1
    full_flag = False
    while incomplete:
        if not output_1.mated_to and full_flag is False:
            while outcheck:
                outval = np.random.randint(g.gate_id, ports)
                inpcheck, num_in = check_connecting_input(circuit, outval)
                checkval = check_output_cgp(outval, g, circuit)
                fullcheck = check_inputs_full(circuit, outval, ports, output_list)
                if fullcheck == 0 or fullcheck is None:
                    outcheck = 0
                    full_flag = True
                    #Output_to_Input(circuit, g.gate_id, dummy_id)
                elif checkval == 1 or inpcheck == num_in:
                    outcheck = 1
                else:
                    Output_to_Input(circuit, g.gate_id, outval)
                    outcheck = 0
        elif not input_1.mated_to:  # if input1 is empty
            while check:
                val = np.random.randint(0, g.gate_id)
                check = check_input_cgp(val, g, circuit)
            Output_to_Input(circuit, val, g.gate_id)
        elif not input_2.mated_to:
            other_input = input_1.mated_to[0]
            while check2:
                connect_check = 1
                while connect_check:
                    val = np.random.randint(0, g.gate_id)
                    if val != other_input:
                        connect_check = 0
                check2 = check_input_cgp(val, g, circuit)
            Output_to_Input(circuit, val, g.gate_id)
            incomplete = 0
        else:
            incomplete = 0


def connect_1_input_gates(input_1, output_1, circuit, ports, g, output_list, dummy_id):
    incomplete = 1
    outcheck = 1
    check = 1
    full_flag = False
    while incomplete:
        if not output_1.mated_to and full_flag is False:
            while outcheck:
                outval = np.random.randint(g.gate_id, ports)
                inpcheck, num_in = check_connecting_input(circuit, outval)
                checkval = check_output_cgp(outval, g, circuit)
                fullcheck = check_inputs_full(circuit, outval, ports, output_list)
                if fullcheck == 0 or fullcheck is None:
                    outcheck = 0
                    full_flag = True
                    #Output_to_Input(circuit, g.gate_id, dummy_id)
                elif checkval == 1 or inpcheck == num_in:
                    outcheck = 1
                else:
                    Output_to_Input(circuit, g.gate_id, outval)
                    outcheck = 0
        elif not input_1.mated_to:  # if input1 is empty
            while check:
                val = np.random.randint(0, g.gate_id)
                check = check_input_cgp(val, g, circuit)
            Output_to_Input(circuit, val, g.gate_id)
            incomplete = 0
        else:
            incomplete = 0


def check_input_cgp(value, gate, circuit):
    for i in circuit:
        if i.gate_id == value:
            if i.cgp_id[1] < gate.cgp_id[1]:
                return 0
            else:
                return 1


def check_output_cgp(value, gate, circuit):
    for i in circuit:
        if i.gate_id == value:
            if i.cgp_id[1] == gate.cgp_id[1] + 1:
                return 0
            else:
                return 1


def check_connecting_input(circuit, val):
    counter = 0
    for g in circuit:
        if g.gate_id == val:
            num_in = g.inputnum
            for i in g.inputs:
                if len(i.mated_to) == 1:
                    counter += 1
            return counter, num_in


def check_inputs_full(circuit, val, ports, output_list):
    cnt = 0
    for gate in circuit:
        if gate.gate_id >= val:
            if gate.type == 99:
                pass
            else:
                for i in gate.inputs:
                    if not i.mated_to:
                        cnt += 1
    return cnt


def next_generation(self):
    for i in range(self.pop_size):
        parent1 = self.accept_reject()
        parent2 = self.accept_reject()
        child = parent1.crossover(parent2)
        child.mutate()
        self.newpop.append(child)
    return self.newpop


def accept_reject(self):
    while True:
        index = np.random.randint(0, self.pop_size)
        partner = self.population[index]
        val = np.random.randint(0, 8)
        if val < partner.fitness:
            return partner
