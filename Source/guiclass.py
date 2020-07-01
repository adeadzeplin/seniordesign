from tkinter import Tk, Label, Button, Checkbutton,IntVar, StringVar
from QLARK.qlark_main import qlarklearn
from CVS_.CVS_gate_class import GateType

class MyFirstGUI:
    def __init__(self, master):
        self.input_truthtable = []
        self.temp = []
        self.master = master

        self.initdict = dict()

        master.title("AI CIRCUIT DESIGN")

        self.label1 = Label(master, text="Bot")
        self.label1.grid(row=0,column=0)
        self.label2 = Label(master, text="Output")
        self.label2.grid(row=0, column=2)

#------Column 0 ----------

        self.qlarkrun_button = Button(master, text=" Run Qlark", command=self.runQlark)
        self.qlarkrun_button.grid(row=1,column=0)

        self.cvsrun_button = Button(master, text=" Run LUCA", command=self.yeet)
        self.cvsrun_button.grid(row=2,column=0)

        self.close_button = Button(master, text="     Close     ", command=master.quit)
        self.close_button.grid(row=3,column=0)

# ------Column 1 ----------

        self.Circuit1 = Checkbutton(master, text="half-adder", command=self.circuit1)
        self.Circuit2 = Checkbutton(master, text="full-adder", command=self.circuit2)
        self.Circuit3 = Checkbutton(master, text="64bit-adder", command=self.circuit3)
        self.Circuit1.grid(row=1,column=1)
        self.Circuit2.grid(row=2,column=1)
        self.Circuit3.grid(row=3,column=1)

# ------Column 2 ----------

        #self.label3 = StringVar(master,"helllo")
        self.label4 = Label(master, text=self.input_truthtable)
        self.label4.grid(row=2,column=2)



    def runQlark(self):
        #self.input_truthtable = [[0, 1, 1, 0], [0, 0, 0, 1]]  # Half Adder circuit Truth Table
        whilecounter = 0

        while True:
            whilecounter += 1
            print(f"{whilecounter}th pass of the infiniteLoop")

            if qlarklearn(self.initdict):
                print(f"The AI Learned on the {whilecounter}th pass of the infiniteLoop")
                break

        #if error return maybe display in window

    def yeet(self):
        print("Will can figure this part out")
        #if error return maybe display in window

    def circuit1(self):

        self.initdict = {
            'truthtable': [[0, 1, 1, 0], [0, 0, 0, 1]],                 # Truthtable
            'circuitinputs': 2,                                         #
            'circuitoutputs': 2,                                        #
            'maxgatenum': 2,                                            # Total num of gates AI is allowed toplace
            'allowedgatetypes': [GateType.AND.name,GateType.XOR.name],  # For Qlark             please dont touch
            'maxsteps': 10,                                             # For Qlark             please dont touch
            'totalthreads': 1,                                          # For Qlark threading   please dont touch
            'trainingsetspthread': 1                                    # For Qlark threading   please dont touch
        }

        label4 = Label(self.master,text=self.initdict['truthtable'])
        label4.grid(row=2,column=2)
    def circuit2(self):

        self.initdict = {
            'truthtable': [[1, 0, 0, 1, 0, 1, 1, 0],[1, 1, 1, 0, 1, 0, 0, 0]],  # Truthtable Full Adder
            'circuitinputs': 3,                         #
            'circuitoutputs': 2,                        #
            'maxgatenum': 6,                            # Total num of gates AI is allowed to place
            'allowedgatetypes': [GateType.AND.name,     # For Qlark             please dont touch
                                 GateType.XOR.name,     # For Qlark             please dont touch
                                 GateType.OR.name],     # For Qlark             please dont touch
            'maxsteps': 15,                             # For Qlark             please dont touch
            'totalthreads': 1,                          # For Qlark threading   please dont touch
            'trainingsetspthread': 6                    # For Qlark threading   please dont touch
        }

        label4 = Label(self.master, text=self.input_truthtable)
        label4.grid(row=2, column=2)
    def circuit3(self):
        self.input_truthtable = []
        label4 = Label(self.master, text=self.input_truthtable)
        label4.grid(row=2, column=2)
