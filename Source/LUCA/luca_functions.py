import numpy as np
from CVS_.CVS_gate_class import Gate, Connector
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
    if cgp[1] == 1:
        val = np.random.randint(2, 8)
    else:
        val = np.random.randint(2, 9)
    gate = Gate(val)
    gate.cgp_id = cgp
    return gate


def connect_gates(gates, circuit, ports, output_list):
    for g in gates:
        if g.inputnum == 2:
            input_1 = g.inputs[0]
            input_2 = g.inputs[1]
            output_1 = g.outputs[0]
            connect_2_input_gates(input_1, input_2, output_1, circuit, ports, g, output_list)
        else:
            input_1 = g.inputs[0]
            output_1 = g.outputs[0]
            connect_1_input_gates(input_1, output_1, circuit, ports, g, output_list)


def connect_2_input_gates(input_1, input_2, output_1, circuit, ports, g, output_list):
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
                fullcheck = check_inputs_full(circuit, g.gate_id, ports, output_list)
                if fullcheck == 0 or fullcheck is None:
                    outcheck = 0
                    full_flag = True
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
            check2 = 1
            while check2:
                connect_check = 1
                while connect_check:
                    val = np.random.randint(0, g.gate_id)
                    other_host_id = find_host_id(other_input, circuit)
                    if val != other_host_id:
                        connect_check = 0
                check2 = check_input_cgp(val, g, circuit)
            Output_to_Input(circuit, val, g.gate_id)
            incomplete = 0
        else:
            incomplete = 0


def connect_1_input_gates(input_1, output_1, circuit, ports, g, output_list):
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
                fullcheck = check_inputs_full(circuit, g.gate_id, ports, output_list)
                if fullcheck == 0 or fullcheck is None:
                    outcheck = 0
                    full_flag = True
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


def find_host_id(connector_id, circuit):
    for k in circuit:
        for j in k.outputs:
            if connector_id == j.get_id():
                other_host_id = j.host
                return other_host_id


def check_input_cgp(value, gate, circuit):
    for i in circuit:
        if i.gate_id == value:
            if i.cgp_id[1] == gate.cgp_id[1] - 1:
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


def connect_gates_d(gates, circuit, ports, output_list, dummy_list):
    dummy_id = dummy_list[0].gate_id

    for g in gates:
        if g.inputnum == 2:
            input_1 = g.inputs[0]
            input_2 = g.inputs[1]
            output_1 = g.outputs[0]
            connect_2d_input_gates(input_1, input_2, output_1, circuit, ports, g, output_list, dummy_id)
        else:
            input_1 = g.inputs[0]
            output_1 = g.outputs[0]
            connect_1d_input_gates(input_1, output_1, circuit, ports, g, output_list, dummy_id)


def connect_2d_input_gates(input_1, input_2, output_1, circuit, ports, g, output_list, dummy_id):
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
                fullcheck = check_inputs_full(circuit, g.gate_id, ports, output_list)
                if fullcheck == 0 or fullcheck is None:
                    outcheck = 0
                    full_flag = True
                    Output_to_Input(circuit, g.gate_id, dummy_id)
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
            check2 = 1
            while check2:
                connect_check = 1
                while connect_check:
                    val = np.random.randint(0, g.gate_id)
                    other_host_id = find_host_id(other_input, circuit)
                    if val != other_host_id:
                        connect_check = 0
                check2 = check_input_cgp(val, g, circuit)
            Output_to_Input(circuit, val, g.gate_id)
            incomplete = 0
        else:
            incomplete = 0


def connect_1d_input_gates(input_1, output_1, circuit, ports, g, output_list, dummy_id):
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
                fullcheck = check_inputs_full(circuit, g.gate_id, ports, output_list)
                if fullcheck == 0 or fullcheck is None:
                    outcheck = 0
                    full_flag = True
                    Output_to_Input(circuit, g.gate_id, dummy_id)
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


def create_genes(circuit):
    gene = []
    for gate in circuit:
        temp = []
        if gate.type == 0:
            pass
        else:
            for i in gate.inputs:
                val = find_host_id(i.mated_to[0], circuit)
                temp.append(val)
            temp.append(gate.gate_id)
            temp.append(gate.type)
            gene.append(temp)
    return gene


def accept_reject(population_size, population):
    while True:
        index = np.random.randint(0, population_size)
        partner = population[index]
        val = np.random.uniform(0, 1)
        if val < partner.fitness:
            return partner


def create_child(child, parent1, parent2):
    split_point = np.random.randint(1, (len(parent1.genes) - 1))
    for i in range(len(parent1.genes)):
        if i > split_point:
            child.genes.append(parent2.genes[i])
        else:
            child.genes.append(parent1.genes[i])

def convert_form(population):
    for i in population:
        Gate.gate_id_counter = 0
        Connector.id = 0
        for k in range(i.num_inputs):
            inp = Gate(0, 0, 1)
            i.stan_circuit.append(inp)
            i.input_list.append(inp)
        for j in range(len(i.genes)):
            type = i.genes[j][-1]
            if type == 1:
                out = Gate(1, 1, 0)
                i.stan_circuit.append(out)
                i.output_list.append(out)
            elif type == 99:
                dummy = Gate(type, (i.num_rows - i.num_outputs), 0)
                i.stan_circuit.append(dummy)
                i.dummy_list.append(dummy)
            else:
                gate = Gate(type)
                i.stan_circuit.append(gate)
                i.gate_list.append(gate)
        for k in range(len(i.genes)):
            if len(i.genes[k]) == 4:
                Output_to_Input(i.stan_circuit, i.genes[k][0], i.genes[k][2])
                Output_to_Input(i.stan_circuit, i.genes[k][1], i.genes[k][2])

            else:
                Output_to_Input(i.stan_circuit, i.genes[k][0], i.genes[k][1])
