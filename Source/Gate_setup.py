#  logic.py
#
#  Copyright 2001 by Chris Meyers.
#
#  Define classes for Connector, Logic Circuit, Gate
#


class Connector:
    # Connectors are inputs and outputs. Only outputs should connect
    # to inputs. Be careful NOT to have circular references
    # As an output is changed it propagates the change to its connected inputs
    #
    def __init__(self, owner, name, activates=0, monitor=0):
        self.value = None
        self.owner = owner
        self.name = name
        self.monitor = monitor
        self.connects = []
        self.activates = activates  # If true change kicks evaluate function

    def connect(self, inputs):
        if not isinstance(inputs, list):
            inputs = [inputs]
        for input in inputs:
            self.connects.append(input)

    def set(self, value):
        if self.value == value:
            return  # Ignore if no change
        self.value = value
        if self.activates:
            self.owner.evaluate()
        if self.monitor:
            print("Connector {0}-{1} set to {2}".format(self.owner.name,
                                                        self.name,
                                                        self.value))
        for con in self.connects:
            con.set(value)


class LC:
    # Logic Circuits have names and an evaluation function defined in child
    # classes. They will also contain a set of inputs and outputs.
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        return


class Not(LC):  # Inverter. Input A. Output B.
    def __init__(self, name):
        LC.__init__(self, name)
        self.A = Connector(self, 'A', activates=1)
        self.B = Connector(self, 'B')

    def evaluate(self):
        self.B.set(not self.A.value)


class Gate2(LC):  # two input gates. Inputs A and B. Output C.
    def __init__(self, name):
        LC.__init__(self, name)
        self.A = Connector(self, 'A', activates=1)
        self.B = Connector(self, 'B', activates=1)
        self.C = Connector(self, 'C')


class And(Gate2):  # two input AND Gate
    def __init__(self, name):
        Gate2.__init__(self, name)

    def evaluate(self):
        self.C.set(self.A.value and self.B.value)


class Or(Gate2):  # two input OR gate.
    def __init__(self, name):
        Gate2.__init__(self, name)

    def evaluate(self):
        self.C.set(self.A.value or self.B.value)

#inA = 1
#inB = 1

#a = And('A1')
#a.C.monitor = 1
#a.A.set(inA)

#n = Not('N1')
#a.C.connect(n.A)
#n.B.monitor = 1
#a.B.set(inB)