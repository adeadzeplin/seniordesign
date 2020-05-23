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
    Cost_COMPLETE = 150
    COST_CONNECT = 10
    COST_NOT = -6
    COST_NAND = -4
    COST_NOR = -4
    COST_AND = -6
    COST_OR = -6
    COST_XOR = -8
    COST_INCORRECT = -100
    COST_ILEGAL = -100


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

    def c_print(self):
        print(f"        hostGate_Id: {self.host},   connector_id: {self._ID},    Mated_to Connector IDs: {self.mated_to},     portType: {self.type.name}")

    def append_attributes_to_list(self, biglist):
        biglist.append(self._ID)
        biglist.append(self.host)
        biglist.append(self.type)
        for mate in self.mated_to:
            biglist.append(mate)




class Gate:
    gate_idcounter = 0
    def __init__(self, type = None, input_num = 2, output_num = 1):
        if type == None:
            exit("YOU TRIED TO MAKE A GATE OF NONE TYPE DIPSHIT")
        if type == GateType.NOT:
            input_num = 1
        self.gate_id = Gate.gate_idcounter  #jargan integer
        Gate.gate_idcounter += 1
        self.type = type        #not,nor,nand
        self.inputs = []
        self.outputs =[]
        self.create_ports(input_num,output_num)

    def append_attributes_to_list(self, biglist):
        biglist.append(self.gate_id)
        biglist.append(self.type)
        for i in self.inputs:
            i.append_attributes_to_list(biglist)
        for i in self.outputs:
            i.append_attributes_to_list(biglist)

    def create_ports(self,in_num,out_num):
        for i in range(0,in_num):
            self.inputs.append(Connector(self.gate_id, ConnectorType.INPUT))
        for i in range(0,out_num):
            self.outputs.append(Connector(self.gate_id, ConnectorType.OUTPUT))

    def check_if_connection_available(a,b):

        # both of the gates are circuit input types
        if a.type == GateType.CIRCUIT_INPUT or b.type == GateType.CIRCUIT_INPUT:
            if a.type == GateType.CIRCUIT_OUTPUT or b.type == GateType.CIRCUIT_OUTPUT:
                return False
        if a == b:
            return False
        # a connector in A has B
        for out in a.outputs:
            for inp in b.inputs:
                if out.type != ConnectorType.OUTPUT or inp.type != ConnectorType.INPUT:
                    return False
                if len(inp.mated_to) > 0: # if an input is already mated to
                    # BAD
                    return False
                else:
                    for x in out.mated_to:
                        for y in inp.mated_to:
                            if x == inp.mated_to or y == out.mated_to:
                                # connection already exists
                                return False

                conectorout = out
                conectorin = inp

                #this only returns if there is NOTHING wrong at all
                return (conectorout,conectorin)




    def connect_to_(self,anothergate,cona,conb):
        # print(f"\nAttempting to connect gate: {self.gate_id} to gate: {anothergate.gate_id}")
        for x, o in enumerate(self.outputs):
            for y, i in enumerate(anothergate.inputs):

                if o == cona:
                    if i == conb:
                        self.outputs[x].connect(anothergate.inputs[y])
                        anothergate.inputs[y].connect(self.outputs[x])


        # for i in self.outputs:
        #     for x in i.mated_to:
        #         for j in anothergate.inputs:
        #             if x == j._ID or len(j.mated_to) > 0:
        #                 # print(f"We all ready got {j._ID} in da bag")
        #
        #                 return GateCost.COST_ILEGAL
        #
        # if self != anothergate:
        #     for j in anothergate.inputs:
        #         if len(j.mated_to) < 1:
        #             if len(self.outputs) != 0:
        #
        #                 if j.type == ConnectorType.INPUT:
        #                     if len(self.j.mated_to) > 0:
        #                         print("fuck")
        #                         return GateCost.COST_ILEGAL
        #
        #
        #                 self.outputs[0].connect(j)
        #                 j.connect(self.outputs[0])
        #                 return GateCost.COST_CONNECT
        #     # print("picking a random input connector")
        #     # print(len(anothergate.inputs))
        #     try:
        #
        #         rand_index = np.random.randint(len(anothergate.inputs))
        #         self.outputs[0].connect(anothergate.inputs[rand_index])
        #         anothergate.inputs[rand_index].connect(self.outputs[0])
        #         return GateCost.COST_CONNECT
        #     except:
        #         # exit(f"123 {anothergate.g_print()}")
        #         return GateCost.COST_ILEGAL







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

