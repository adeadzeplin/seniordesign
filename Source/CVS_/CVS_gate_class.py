import enum


class ConnectorType(enum.IntEnum):
    # type of connector
    INPUT = 0
    OUTPUT = 1


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
    gate_id_counter = 0

    def __init__(self, type=None , inputNum=2, outputNum=1):

        self.gate_id = Gate.gate_id_counter
        Gate.gate_id_counter += 1
        self.type = type
        if self.type == 4 or self.type == 8:
            inputNum = 1
        self.inputs = []
        self.outputs = []
        self.makePorts(inputNum, outputNum)
        self.tableOutput = []

    def makePorts(self, inPorts, outPorts):  # creates / connects inputs and outputs only
        for i in range(0, inPorts):
            self.inputs.append(Connector(self.gate_id, ConnectorType.INPUT))
        for i in range(0, outPorts):
            self.outputs.append(Connector(self.gate_id, ConnectorType.OUTPUT))

    def gateConnect(self, anothergate):

        for i in self.outputs:
            for x in i.mated_to:
                for j in anothergate.inputs:
                    if x == j._ID:
                        # print(f"We all ready got {j._ID} in da bag")
                        return "gateConnect issue"

        if self != anothergate:
            for j in anothergate.inputs:
                if len(j.mated_to) <= 0: # if theres nothing connected to an input
                    if len(self.outputs) != 0: # if there is anoutput
                        #print(self.outputs[0]._ID, j._ID)
                        self.outputs[0].connect(j)
                        j.connect(self.outputs[0])
                        return


    def g_print(self):
        print(
            f"\ngate_id: {self.gate_id},    type: {self.type},  numofinputs: {len(self.inputs)},    numofoutputs: {len(self.outputs)}")
        for i in self.inputs:
            i.c_print()
        for i in self.outputs:
            i.c_print()
