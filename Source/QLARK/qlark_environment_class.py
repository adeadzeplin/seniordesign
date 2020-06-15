from qlark_logicgates_class import *

def square(val):
    return val * val

class BootLeg_Logic:
    def __init__(self,C_IN_CT = 2,C_OUT_CT = 1, MAX_GATE_NUM= 1,NUM_OF_GATE_TYPES= 1):
        # Circuit constants
        self.CIRCUIT_INPUTS_COUNT = C_IN_CT
        self.CIRCUIT_OUTPUTS_COUNT = C_OUT_CT
        self.MAX_GATE_NUM = MAX_GATE_NUM  # Max num of gates the ai can place
        self.NUM_OF_GATE_TYPES = NUM_OF_GATE_TYPES

        # Circuit Variables
        self.list_of_gates = []

        # Total Number of Actions posible that the AI can Take
        self.ACTION_SPACE = square(self.MAX_GATE_NUM + self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT) + self.NUM_OF_GATE_TYPES

    def reset(self):
        self.reset_circuit()
        self.create_circuit_inputs()
        self.create_circuit_outputs()
        if np.random.random()>= 0:
            self.list_of_gates.append(Gate(GateType.NAND))

    def getstate(self):
        return self.get_Logic_state()

    def takeaction(self, act):
        return self.actionf(act)


    def checkwin(self):
        if self.checkciruitcompletion():
            return True
        else:
            return False
    def checklose(self, reward):
        if reward == GateCost.COST_ILEGAL:
            return True
        else:
            return False

    def printout(self):
        for gate in self.list_of_gates:
            gate.g_print()

    def getspecialreward(self, reward):
        # print("fuckyeah")
        if self.checkciruitcompletion():
            if len(self.list_of_gates) == (self.MAX_GATE_NUM + self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT):
                print("fuckyeah")
                new_q = reward.value + GateCost.Cost_COMPLETE.value + GateCost.COST_CORRECT.value
                return new_q
            else:
                new_q = reward.value + GateCost.Cost_COMPLETE.value + GateCost.COST_INCORRECT.value
                return new_q
        else:
            return exit("THIS SHOUDN'T HAVE HAPPENED")

    def checkciruitcompletion(self):
        for gate in self.list_of_gates:
            for port in gate.inputs:
                if len(port.mated_to) == 0:
                    return False
            for port in gate.outputs:
                if len(port.mated_to) == 0:
                    return False
        print("Circuit COMPLETE")
        return True

    def get_Logic_state(self):
        state_id = []
        temp = []
        temp.append(self.MAX_GATE_NUM)
        temp.append(len(self.list_of_gates)-(self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT))
        temp.append(self.NUM_OF_GATE_TYPES)
        state_id.append('/'.join([str(x) for x in temp]))
        for gate in self.list_of_gates:
            output_list = []
            gate.append_attributes_to_list(output_list)

            # https: // datascience.stackexchange.com / questions / 55785 / q - table - creation - and -update -
            # for -dynamic - action - space
            # # This state to state_id conversion should be a re-usable function
            # state_id = '/'.join([str(x) for x in state])
            # # Example state_id is '20/12/56/9/76/30'
            state_id.append('/'.join([str(x) for x in output_list]))
            # I stole this ^^^^^^^^^^^ line of code
        state_id.sort()
        state_id = tuple(state_id)
        return state_id





    def reset_circuit(self):
        for i in range(len(self.list_of_gates)):
            self.list_of_gates.pop()
        Connector._id = 0
        Gate.gate_idcounter = 0

    def create_circuit_inputs(self):
        for i in range(self.CIRCUIT_INPUTS_COUNT):
            self.list_of_gates.append(Gate(GateType.CIRCUIT_INPUT, 0, 1))

    def create_circuit_outputs(self):
        for i in range(self.CIRCUIT_OUTPUTS_COUNT):
            self.list_of_gates.append(Gate(GateType.CIRCUIT_OUTPUT, 1, 0))

    def OutputOfAtoInputofB(self, a, b):

        try:
            temp = self.list_of_gates[a].check_if_connection_available(self.list_of_gates[b])
        except:
            return GateCost.COST_ILEGAL

        if temp == None or temp == False:
            return GateCost.COST_ILEGAL
        else:
            # print("burhp")
            connectora, connectorb = self.list_of_gates[a].check_if_connection_available(self.list_of_gates[b])
            self.list_of_gates[a].connect_to_(self.list_of_gates[b], connectora, connectorb)
            return GateCost.COST_CONNECT





            # try:
            #     self.list_of_gates[a].check_if_connection_available(b)
            #     return self.list_of_gates[a].connect_to_(self.list_of_gates[b])
            # except:
            #     return GateCost.COST_ILEGAL



    def actionf(self,action):
        if action < self.NUM_OF_GATE_TYPES:
            temp = len(self.list_of_gates) - (self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT)
            if temp < self.MAX_GATE_NUM:
                if action == 0:
                    self.list_of_gates.append(Gate(GateType.NAND))
                    return GateCost.COST_NAND
                elif action == 1:
                    self.list_of_gates.append(Gate(GateType.NOT))
                    return GateCost.COST_NOT
                elif action == 3:
                    self.list_of_gates.append(Gate(GateType.NOR))
                    return GateCost.COST_NOR
                elif action == 4:
                    self.list_of_gates.append(Gate(GateType.AND))
                    return GateCost.COST_AND
                elif action == 5:
                    self.list_of_gates.append(Gate(GateType.OR))
                    return GateCost.COST_OR
                elif action == 6:
                    self.list_of_gates.append(Gate(GateType.XOR))
                    return GateCost.COST_XOR
                else:
                    return GateCost.COST_ILEGAL
            else:
                return GateCost.COST_ILEGAL
        else:
            action -= self.NUM_OF_GATE_TYPES
            # These values are calculated in order to map a 1D vector to a set of combinational outputs
            mod = (action % (self.MAX_GATE_NUM + self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT))
            div = (action // (self.MAX_GATE_NUM + self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT))

            return self.OutputOfAtoInputofB( div, mod)





