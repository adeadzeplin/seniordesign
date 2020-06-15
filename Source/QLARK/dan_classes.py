
import numpy as np
import enum


class GateType(enum.Enum):
    # Circuit ID's
    CIRCUIT_INPUT = 0
    CIRCUIT_OUTPUT = 1
    #Gate ID's
    NOT = 2
    NAND = 3
    NOR = 4
    AND = 5
    OR = 6
    XOR = 7

    GATE_NONE = None

def RandGateType():
    return GetGateType(np.random.randint(2, 5))

def GetGateType(some_int):

    if some_int == 2:
        return GateType.NOT
    elif some_int == 3:
        return GateType.NAND
    elif some_int == 4:
        return GateType.NOR
    elif some_int == 5:
        return GateType.AND
    elif some_int == 6:
        return GateType.OR
    elif some_int == 6:
        return GateType.XOR

    else:
        exit(f"ATTEMPTED TO PICK INVALID GATE TYPE: {some_int}")


class GateCost(enum.Enum):
    #GateCosts
    COST_CORRECT = 1000
    Cost_COMPLETE = 100
    COST_CONNECT = 10
    COST_NOT = -8
    COST_NAND = -4
    COST_NOR = -4
    COST_AND = -6
    COST_OR = -6
    COST_XOR = -8
    COST_INCORRECT = -150
    COST_ILEGAL = -1000


class ConnectorType(enum.IntEnum):
    #type of connector
    INPUT = 0
    OUTPUT = 1
class Connector:
    _id =0
    def __init__(self, host, type):
        self._ID = Connector._id
        Connector._id += 1
        self.host = host #host gate ID
        self.type = type #input 0 or output 1
        self.mated_to = []

    def connect(self,anotherconnector):
        self.mated_to.append(anotherconnector._ID)
        # self.c_print()

    def c_print(self):
        print(f"        hostGate_Id: {self.host},   connector_id: {self._ID},    Mated_to Connector IDs: {self.mated_to},     portType: {self.type.name}")




class Gate:
    gate_idcounter = 0
    def __init__(self, type = None, input_num = 2, output_num = 1):
        if type == None:
            exit("YOU TRIED TO MAKE A GATE OF NONE TYPE DIPSHIT")
        if type == GateType.NOT:
            input_num = 1
        self.gate_id = self.gate_idcounter  #jargan integer
        Gate.gate_idcounter += 1
        self.type = type        #not,nor,nand
        self.inputs = []
        self.outputs =[]
        self.create_ports(input_num,output_num)

    def create_ports(self,in_num,out_num):
        for i in range(0,in_num):
            self.inputs.append(Connector(self.gate_id, ConnectorType.INPUT))
        for i in range(0,out_num):
            self.outputs.append(Connector(self.gate_id, ConnectorType.OUTPUT))

    def connect_to_(self,anothergate):
        # print(f"\nAttempting to connect gate: {self.gate_id} to gate: {anothergate.gate_id}")

        for i in self.outputs:
            for x in i.mated_to:
                for j in anothergate.inputs:
                    if x == j._ID:
                        # print(f"We all ready got {j._ID} in da bag")

                        return GateCost.COST_ILEGAL

        if self != anothergate:
            for j in anothergate.inputs:
                if len(j.mated_to) <= 0: # if theres nothing connected to an input
                    if len(self.outputs) != 0: # if there is anoutput
                        self.outputs[0].connect(j)
                        j.connect(self.outputs[0])
                        return GateCost.COST_CONNECT

        return GateCost.COST_ILEGAL



            # print("picking a random input connector")
            # print(len(anothergate.inputs))
            # try:
            #
            #     rand_index = np.random.randint(len(anothergate.inputs))
            #     self.outputs[0].connect(anothergate.inputs[rand_index])
            #     anothergate.inputs[rand_index].connect(self.outputs[0])
            #     return GateCost.COST_CONNECT
            # except:
            #     # exit(f"123 {anothergate.g_print()}")
            #     return GateCost.COST_ILEGAL







    def g_print(self):
        print(f"\ngate_id: {self.gate_id},    type: {self.type},  numofinputs: {len(self.inputs)},    numofoutputs: {len(self.outputs)}")
        for i in self.inputs:
            i.c_print()
        for i in self.outputs:
            i.c_print()



# # circuit input_class
# class CircuitInput:
#     def __init__(self):
#         self.output = Connector(GateType.CIRCUIT_INPUT, ConnectorType.OUTPUT)

