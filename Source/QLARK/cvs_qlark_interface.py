import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import CVS_.CVS_gate_class as cvs
import CVS_.CVS_metrics as CVS_metrics
import CVS_.CVS_circuit_calculations as CVS_circuit_calculations
import CVS_.CVS_parser as CVS_parser
import pickle
import enum
style.use("ggplot")

class CircuitStatus(enum.Enum):
    Valid = 0
    Broken = 1
    Completed = 2
    Correct = 3

class AIRewards(enum.IntEnum):
    PlaceGate = 1000
    ConnectGate = 1000
    CircuitBroken = 0
    CircuitCompleted = 10000
    CircuitCorrect  = 200000000


def square(val):
    return val * val

class QlarkCircuitInterface():
    def __init__(self,DESIRED_LOGIC,C_IN_CT = 2,C_OUT_CT = 1, MAX_GATE_NUM= 1,ALLOWED_GATE_TYPES= 'list',OPTIMIZE_METRIC= None):
        # Circuit constants
        self.CIRCUIT_INPUTS_COUNT = C_IN_CT
        self.CIRCUIT_OUTPUTS_COUNT = C_OUT_CT
        self.MAX_GATE_NUM = MAX_GATE_NUM  # Max num of gates the ai can place
        self.MAX_GATE_TYPES = 7
        self.ALLOWED_GATE_TYPES = ALLOWED_GATE_TYPES
        self.DESIRED_LOGIC = DESIRED_LOGIC
        self.TRANSISTOR_BUDGET = 20
        self.OPTIMIZE_METRIC = OPTIMIZE_METRIC

        # Circuit Variables
        self.list_of_gates = []
        self.most_resent_successful_circuit = []
        self.circuitstatus = CircuitStatus.Valid
        self.circuitlogic = 0

        # Circuit Metrics
        self.percentsame = None
        self.metrics = None
        self.circuitlogic = None


        # Total Number of Actions posible that the AI can Take
        self.ACTION_SPACE = square(self.MAX_GATE_NUM + self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT) + len(self.ALLOWED_GATE_TYPES)

        self.recursion_depthCounter = 0
        self.recursion_error_flag = False

    def scancirc(self,scanedorder,gate_id,list_gates):
        # print(scanedorder)
        self.recursion_depthCounter += 1

        gate = None
        for i in list_gates:
            # print((i.gate_id , gate_id))
            if i.gate_id == gate_id:
                scanedorder.append((i.gate_id, i.type.name))
                gate = i
                break
        if gate == None:
            print('fuck')
        if self.recursion_depthCounter >= 100:
            # print("recursive termination")
            self.recursion_error_flag = True
            return 'there was a circuit loop that caused a recursive error'
        # check if the gate has any inputs
        if len(gate.inputs) > 0:
            for inputport in gate.inputs:
                #check if input port has connections
                if len(inputport.mated_to)>0:
                    for ngate in list_gates:
                        for outputport in ngate.outputs:
                            for matched_id in outputport.mated_to:
                                if matched_id == inputport._ID:
                                    self.scancirc(scanedorder,ngate.gate_id,list_gates)
                                    break

        return scanedorder


    def getfancyprintoutstring(self,listogates):

        arrow = ' -> '
        superlist = []
        self.recursion_error_flag = False
        for gate in listogates:
            megalist = []
            if gate.type == cvs.GateType.circuitOutput:
                # megalist.append(self.scancirc(megalist,gate.gate_id))
                superlist.append(self.scancirc(megalist,gate.gate_id,listogates))
                if self.recursion_error_flag == True:
                    return 'there was a circuit loop that caused a recursive error'

        self.recursion_depthCounter = 0

        print(superlist)
        theprintout = ''
        for logicout in superlist:
            if isinstance(logicout,str):
                theprintout += logicout
            else:
                for line in reversed(logicout):
                    if line[1] == cvs.GateType.circuitOutput.name:
                        theprintout += f"CircOUT:{line[0]}"
                    elif line[1] == cvs.GateType.circuitInput.name:
                        theprintout += f"CircIN:{line[0]}{arrow}"
                    else:
                        theprintout += f"{line[1]}:{line[0]}{arrow}"
                theprintout+="\n"

        return theprintout

    def getprintoutstring(self):
        string =''

        for gate in self.list_of_gates:

            string += f"\ngate_id: {gate.gate_id},    type: {gate.type.name},  numofinputs: {len(gate.inputs)},    numofoutputs: {len(gate.outputs)}"
        return string

    def printout(self):
        for gate in self.list_of_gates:
            gate.g_print()

    def parseLogic(self):
        # intial circuit connection check
        Circuit_Errors = CVS_circuit_calculations.circuit_connection_check(self.list_of_gates)

        if Circuit_Errors == None:
            CVS_parser.runParser(self.list_of_gates, self.DESIRED_LOGIC)
        else:
             print(Circuit_Errors)
    def getparsermetrics(self,list):
        self.percentsame, self.metrics,self.circuitlogic = CVS_parser.ParserMetrics(list,self.DESIRED_LOGIC)
        return (self.percentsame,self.metrics[0],self.metrics[1],self.metrics[2],self.circuitlogic)

    def checkforpoopchute(self):

        for gatea in self.list_of_gates:
            for gateb in self.list_of_gates:
                if gatea == gateb:
                    continue

                if gatea.type == cvs.GateType.circuitInput:
                    if gateb.type == cvs.GateType.circuitOutput:
                        for porta in gatea.outputs:
                            for matea in porta.mated_to:
                                for portb in gateb.inputs:
                                    if matea == portb._ID:
                                        # print("INVALID CIRCUIT CONFIG IDENTIFIED")
                                        self.breakcircuit()
                                        return



    def checkciruitcompletion(self):
        for gate in self.list_of_gates:
            for port in gate.inputs:

                if len(port.mated_to) > 1:
                    self.breakcircuit()
                    return False
                if len(port.mated_to) == 0:
                    return False
            for port in gate.outputs:
                if len(port.mated_to) == 0:
                    return False
        return True

    def getcorrectreward(self):
        self.getparsermetrics(self.list_of_gates)

        if self.OPTIMIZE_METRIC == 'Transistor':
            return AIRewards.CircuitCorrect - self.metrics[2]*AIRewards.CircuitCompleted
        elif self.OPTIMIZE_METRIC == 'Power':
            return AIRewards.CircuitCorrect - self.metrics[0]*AIRewards.CircuitCompleted
        elif self.OPTIMIZE_METRIC == 'Delay':
            return AIRewards.CircuitCorrect - self.metrics[1]*AIRewards.CircuitCompleted
        else:
            # print("bruh moment")
            return AIRewards.CircuitCorrect




    def getspecialreward(self):
        if self.circuitstatus == CircuitStatus.Broken:
            return AIRewards.CircuitBroken
        elif self.circuitstatus == CircuitStatus.Completed:
            aireward_calc = self.circuitlogic * AIRewards.CircuitCompleted

            return aireward_calc

        elif self.circuitstatus == CircuitStatus.Correct:
            return self.getcorrectreward()
        exit("INVALID SPECIAL REWARDVALUE")

    def getcircuitstatus(self):
        self.checkforpoopchute()     # Checks circuits for any straight passthrout for circuit in -> circuit out

        circuit_completion_flag = self.checkciruitcompletion()


        # print(Circuit_Errors)

        if self.circuitstatus == CircuitStatus.Broken:
            return CircuitStatus.Broken
        self.circuitlogic = 0
        if circuit_completion_flag:
            Circuit_Errors = CVS_circuit_calculations.circuit_connection_check(self.list_of_gates)
            if Circuit_Errors == None:
                self.circuitlogic = CVS_parser.runParserMuted(self.list_of_gates, self.DESIRED_LOGIC)

            else:
                return self.circuitstatus

            if self.circuitlogic == 1.0:
                self.circuitstatus = CircuitStatus.Correct

            else:
                self.circuitstatus = CircuitStatus.Completed

        return self.circuitstatus



    def breakcircuit(self):
        self.circuitstatus = CircuitStatus.Broken

    def placegate(self,val):
        temp = len(self.list_of_gates) - (self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT)
        if temp < self.MAX_GATE_NUM:

            if val == 0 and cvs.GateType.AND.name in self.ALLOWED_GATE_TYPES:
                self.list_of_gates.append(cvs.Gate(cvs.GateType.AND))
                # self.update_transistorcount(CVS_metrics.GateTransCost.AND)
            elif val == 1 and cvs.GateType.NOT.name in self.ALLOWED_GATE_TYPES:
                self.list_of_gates.append(cvs.Gate(cvs.GateType.NOT))
                # self.update_transistorcount(CVS_metrics.GateTransCost.NOT)
            elif val == 3 and cvs.GateType.NOR.name in self.ALLOWED_GATE_TYPES:
                self.list_of_gates.append(cvs.Gate(cvs.GateType.NOR))
                # self.update_transistorcount(CVS_metrics.GateTransCost.NOR)
            elif val == 4 and cvs.GateType.NAND.name in self.ALLOWED_GATE_TYPES:
                self.list_of_gates.append(cvs.Gate(cvs.GateType.NAND))
                # self.update_transistorcount(CVS_metrics.GateTransCost.NAND)
            elif val == 5 and cvs.GateType.OR.name in self.ALLOWED_GATE_TYPES:
                self.list_of_gates.append(cvs.Gate(cvs.GateType.OR))
                # self.update_transistorcount(CVS_metrics.GateTransCost.OR)
            elif val == 6 and cvs.GateType.XOR.name in self.ALLOWED_GATE_TYPES:
                self.list_of_gates.append(cvs.Gate(cvs.GateType.XOR))
                # self.update_transistorcount(CVS_metrics.GateTransCost.XOR)
            elif val == 7 and cvs.GateType.XNOR.name in self.ALLOWED_GATE_TYPES:
                self.list_of_gates.append(cvs.Gate(cvs.GateType.XNOR))
            else:
                self.breakcircuit()
                return AIRewards.CircuitBroken
            return AIRewards.PlaceGate

    def OutputOfAtoInputofB(self, a, b):

        connectora, connectorb = self.list_of_gates[a].check_if_connection_available(self.list_of_gates[b])
        self.list_of_gates[a].cvs.connect_to_(self.list_of_gates[b], connectora, connectorb)
        return AIRewards.ConnectGate



    def attempt_action(self,action):
        if action <= self.MAX_GATE_TYPES:
            temp = len(self.list_of_gates) - (self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT)
            #   check if there is space to add another gate
            if temp < self.MAX_GATE_NUM:
                return self.placegate(action)
            else:
                self.breakcircuit()
                return AIRewards.CircuitBroken

        else:
            action -=  self.MAX_GATE_TYPES
            # These values are calculated in order to map a 1D vector to a set of combinational outputs
            mod = (action % (self.MAX_GATE_NUM + self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT))
            div = (action // (self.MAX_GATE_NUM + self.CIRCUIT_INPUTS_COUNT + self.CIRCUIT_OUTPUTS_COUNT))
            if div < len(self.list_of_gates) and mod < len(self.list_of_gates):



                self.list_of_gates[div].gateConnect(self.list_of_gates[mod])
                return AIRewards.ConnectGate
            else:
                return AIRewards.CircuitBroken

    def reset_environment(self):
        self.reset_circuit()
        self.circuitstatus = CircuitStatus.Valid
        self.create_circuit_inputs()
        self.create_circuit_outputs()
        # self.list_of_gates.append(cvs.Gate(cvs.GateType.XOR))
        # self.list_of_gates.append(cvs.Gate(cvs.GateType.XOR))
        # self.list_of_gates.append(cvs.Gate(cvs.GateType.AND))
        # self.list_of_gates.append(cvs.Gate(cvs.GateType.AND))
        # self.list_of_gates.append(cvs.Gate(cvs.GateType.OR))




    def create_circuit_inputs(self):
        for i in range(self.CIRCUIT_INPUTS_COUNT):
            self.list_of_gates.append(cvs.Gate(cvs.GateType.circuitInput, 0, 1))

    def create_circuit_outputs(self):
        for i in range(self.CIRCUIT_OUTPUTS_COUNT):
            self.list_of_gates.append(cvs.Gate(cvs.GateType.circuitOutput, 1, 0))

    def reset_circuit(self):
        for i in range(len(self.list_of_gates)):
            self.list_of_gates.pop()
        cvs.Connector.id = 0
        cvs.Gate.gate_id_counter = 0

    def get_state(self):

        temp = []
        #
        # for i in self.DESIRED_LOGIC:
        #     for j in i:
        #         temp.append(j)
        # temp.append(self.ACTION_SPACE)


        for i in self.list_of_gates:
            temp.append('|')


            for x in i.inputs:
                # temp.append(x._ID)
                # temp.append(x.type.value)


                for n in x.mated_to:
                    n_mate_break_flag = False
                    for j in self.list_of_gates:
                        if i == j:
                            continue
                        for w in j.outputs:
                            if n == w._ID:
                                n_mate_break_flag = True
                                temp.append(j.type.name)
                                temp.append(j.gate_id)
                                temp.append(w._ID)
                                # temp.append('->')
                                temp.append(x._ID)
                                break

                        if n_mate_break_flag == True:
                            break

            temp.append(i.type.name)
            temp.append(i.gate_id)

            for x in i.outputs:
                # temp.append(y._ID)
                # temp.append(y.type.value)
                for n in x.mated_to:
                    n_mate_break_flag = False
                    for j in self.list_of_gates:
                        if i == j:
                            continue
                        for w in j.inputs:
                            if n == w._ID:
                                n_mate_break_flag = True
                                temp.append(x._ID)
                                temp.append(w._ID)
                                temp.append(j.type.name)
                                temp.append(j.gate_id)
                                break

                        if n_mate_break_flag == True:
                            break
            temp.append('|')
        state_id = ''.join([str(x) for x in temp])
        # state_id = int(state_id)
        return state_id
