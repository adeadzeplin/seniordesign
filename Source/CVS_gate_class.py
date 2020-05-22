import enum


class ConnectorType(enum.IntEnum):
    # type of connector
    INPUT = 0
    OUTPUT = 1


class GateType:     #no enum here since i need the numbers, not GateType.Type: # as a return
    # in & outs
    circuitInput = 0
    circuitOutput = 1
    # gates
    AND = 2
    OR = 3
    NOT = 4
    NAND = 5
    NOR = 6
    XOR = 7


class Connector:
    id = 0

    def __init__(self, host, type):
        self._ID = Connector.id
        Connector.id += 1
        self.host = host
        self.type = type
        self.mated_to = []

    def connect(self, anotherconnector):
        self.mated_to.append(anotherconnector._ID)
        #print(str(self.mated_to) + "hello")

    def c_print(self):
        print(f"host ID: {self.host}  connector ID: {self._ID}  Mated connector ID: {self.mated_to} ")


class Gate:
    gate_id = 0

    def __init__(self, type=None, inputNum=2, outputNum=1):
        if type == GateType.NOT:
            self.inputNum = 1
        self.gate_id = self.gate_id
        Gate.gate_id += 1
        self.type = type
        self.inputs = []
        self.outputs = []
        self.makePorts(inputNum, outputNum)

    def makePorts(self, inPorts, outPorts):  # creates / connects inputs and outputs only
        for i in range(0, inPorts):
            self.inputs.append(Connector(self.gate_id, ConnectorType.INPUT))
        for i in range(0, outPorts):
            self.outputs.append(Connector(self.gate_id, ConnectorType.OUTPUT))

    def gateConnect(self, anothergate):
        #print(self.outputs[0]._ID)
        for i in range(len(self.outputs)):
            for j in anothergate.inputs:
                print(self.outputs[i]._ID, j._ID)
                if self.outputs[i]._ID == j._ID:
                    print("hiasd")

        if self != anothergate:
            for j in anothergate.inputs:
                #print(self.outputs[0]._ID, j._ID)
                #print(self.inputs[0]._ID, self.inputs[1]._ID)
                if len(j.mated_to) <= 0:  # if theres nothing connected to an input
                    if len(self.outputs) != 0:  # if there is anoutput
                        self.outputs[0].connect(j)
                        j.connect(self.outputs[0])
                        #print(self.outputs[0]._ID, j._ID)


    def g_print(self):
        print(
            f"\ngate_id: {self.gate_id},    type: {self.type},  numofinputs: {len(self.inputs)},    numofoutputs: {len(self.outputs)}")
        for i in self.inputs:
            i.c_print()
        for i in self.outputs:
            i.c_print()
