import tkinter
import time
import threading
import random
import queue
from tkinter import Tk, Label, Button, Checkbutton,IntVar, StringVar,messagebox
from CVS_.CVS_gate_class import GateType
import QLARK.qlark_threading as qt
from QLARK.cvs_qlark_interface import CircuitStatus
from CVS_ import CVS_constants

class QlarkGui:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        # Set up the GUI
        # console = tkinter.Button(master, text='Done', command=endCommand)
        # console.pack(  )
        # Add more GUI stuff here depending on your specific needs
        self.master = master
        # master.geometry("1000x600+300+100")

        self.initdict = None
        self.optmetric = None
        master.title("QLARK STETUP MENU")

        tablecolum = 0
        self.labelselect = Label(master, text="Select Truth Table")
        self.labelselect.grid(row=0, column=tablecolum)
        # SELECT HALFADDER
        self.set_halfadder = Button(master, text="\nhalf adder\n", width=15, command=self.set_HalfAdderInitQlark)
        self.set_halfadder.grid(row=1, column=tablecolum)
        # SELECT FULLADDER
        self.set_fulladder = Button(master, text="\nfull adder\n", width=15, command=self.set_FullAdderInitQlark)
        self.set_fulladder.grid(row=2, column=tablecolum)

        # OPTIMIZE METRIC COLUMN ------------
        metriccolum = 1
        self.label0 = Label(master, text="Select Optimize Metric")
        self.label0.grid(row=0, column=metriccolum)

        # SELECT Transistor
        self.set_transistor = Button(master, text="\nTransistor\n", width=10, command=self.set_transistormetric)
        self.set_transistor.grid(row=1, column=metriccolum)
        # SELECT Power
        self.set_power = Button(master, text="\nPower\n", width=10, command=self.set_powermetric)
        self.set_power.grid(row=2, column=metriccolum)
        # SELECT Delay
        self.set_delay = Button(master, text="\nDelay\n", width=10, command=self.set_delaymetric)
        self.set_delay.grid(row=3, column=metriccolum)

        # SELECT None
        self.set_none = Button(master, text="\nNone\n", width=10, command=self.set_nonemetric)
        self.set_none.grid(row=4, column=metriccolum)
        self.set_none.config(relief="sunken")
        # Status Update
        self.selectstatuslabel = Label(master, text="no metric selected")
        self.selectstatuslabel.grid(row=3, column=2)
        # -----------------------------------

        # Run label
        self.runlabel = Label(master, text="Run AI Until it learns")
        self.runlabel.grid(row=0, column=2)
        # Run Qlark button
        self.runqlark_button = Button(master, text="\nRun Qlark\n", width=15, command=self.checkfortruth)
        self.runqlark_button.grid(row=1, column=2)
        # Status Update
        self.statuslabel = Label(master, text="no truthtable selected")
        self.statuslabel.grid(row=2, column=2)

        #loop counter display
        self.looplabel = Label(master,text="Cycle Number: Na")
        self.looplabel.grid(row=5, column=0)

        #circuit output label ------------
        self.circuitlabel = Label(master,text="Circuit Printout:")
        self.circuitlabel.grid(row=4, column=5)
        # circuit output display
        self.circuitoutputlabel = Label(master, text="Current Circuit Data goes here")
        self.circuitoutputlabel.grid(row=5, column=5)

        self.circuitmetricslabel = Label(master, text="")
        self.circuitmetricslabel.grid(row=6, column=5)

        #--------------------------------
        # SPACER COLUMN
        self.label1 = Label(master, text="", width=10)
        self.label1.grid(row=0, column=6)

        # correct circuit ------------
        self.recentcorrectcircuitlabel= Label(master, text="Correct Circuit Printout:")
        self.recentcorrectcircuitlabel.grid(row=4, column=7)

        # correct circuit printout
        self.correctcircuitoutputlabel = Label(master, text="Correct Circuit Data goes here")
        self.correctcircuitoutputlabel.grid(row=5, column=7)

        # correct circuit metrics
        self.correctmetricsdatalabel = Label(master, text="")
        self.correctmetricsdatalabel.grid(row=6, column=7)
        # ---------------------------

        # SELECT 2bit Comparator
        self.set_2bitComparator = Button(master, text="\n2 bit comparator\n", width=15, command=self.set_2bitComparatorInitQlark)
        self.set_2bitComparator.grid(row=3, column=tablecolum)


    def metricmessage(self,dict):
        # "Power(uA) | Delay(ns) | Transistors "
        metricmessage =  f'Truthtable'
        metricmessage +='\n__________________________________\n'
        metricmessage +=f'{dict["CircuitLogic"]}\n\n'

        metricmessage += 'Metrics\n'
        metricmessage +=  '________________________________\n'
        metricmessage += f'Percent Correct:    {dict["PercentCorrect"]}\n'
        metricmessage += f'Power Consumed(uA): {dict["PowerConsumed"]}\n'
        metricmessage += f'Time Delay(ns):     {dict["TimeDelay"]}\n'
        metricmessage += f'TransistorCount:    {dict["TransistorCount"]}\n'
        return metricmessage

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize(  ):
            try:
                msg = self.queue.get(0)
                if isinstance(msg,int):
                    textdata = f'Cycle Number: {msg}'
                    self.looplabel.configure(text=textdata)
                elif isinstance(msg,str):
                    self.circuitoutputlabel.configure(text=msg)
                    self.circuitmetricslabel.configure(text='No Metrics for this circuit')
                elif isinstance(msg, dict):

                    if msg["CircuitStatus"] == "Correct Circuit":
                        self.correctcircuitoutputlabel.configure(text=msg["CircuitPrintout"])
                        self.correctmetricsdatalabel.configure(text=self.metricmessage(msg))
                    elif msg["CircuitStatus"] == "Complete Circuit":
                        self.circuitoutputlabel.configure(text=msg["CircuitPrintout"])
                        self.circuitmetricslabel.configure(text=self.metricmessage(msg))
                    else:
                        print("UNIDENTIFIED DICT")

            except queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass


    def checkfortruth(self):
        if self.initdict == None:

            self.statuslabel.configure(text="You MUST Select a truth table")
            pass
        else:
            print(self.initdict)
            self.thread = threading.Thread(target=self.runQlark)
            self.thread.start()


    def runQlark(self):
        whilecounter = 0

        while 1:
            whilecounter += 1
            self.queue.put(whilecounter)

            print(f"{whilecounter}th pass of the infiniteLoop")
            learnflag, qai = qt.notthreading(self.initdict)

            if qai.success_flag:
                textgoodcircuitstring = qai.environment.getfancyprintoutstring(qai.environment.most_resent_successful_circuit)
                metrics = qai.environment.getparsermetrics(qai.environment.most_resent_successful_circuit)
                # (percentsame, metrics[0], metrics[1], metrics[2])
                # "Power(uA) | Delay(ns) | Transistors "
                metric_dict = {
                    "CircuitStatus":"Correct Circuit",
                    "CircuitPrintout":textgoodcircuitstring,
                    "PercentCorrect":metrics[0],
                    "PowerConsumed":metrics[1],
                    "TimeDelay":metrics[2],
                    "TransistorCount":metrics[3],
                    "CircuitLogic":metrics[4]

                }
                self.queue.put(metric_dict)

            elif qai.environment.circuitstatus == CircuitStatus.Completed:
                textstring = qai.environment.getfancyprintoutstring(qai.environment.list_of_gates)
                metrics = qai.environment.getparsermetrics(qai.environment.list_of_gates)
                metric_dict = {
                    "CircuitStatus": "Complete Circuit",
                    "CircuitPrintout": textstring,
                    "PercentCorrect": metrics[0],
                    "PowerConsumed": metrics[1],
                    "TimeDelay": metrics[2],
                    "TransistorCount": metrics[3],
                    "CircuitLogic":metrics[4]
                }
                self.queue.put(metric_dict)
            else:
                textstring = qai.environment.getfancyprintoutstring(qai.environment.list_of_gates)
                self.queue.put(textstring)



            if learnflag:
                print(f"The AI Learned on the {whilecounter}th pass of the infiniteLoop")
                break

    def set_nonemetric(self):
        if self.initdict == None:
            self.statuslabel.configure(text="You MUST Select a truth table First")
        else:
            self.set_transistor.config(relief="raised")
            self.set_power.config(relief="raised")
            self.set_delay.config(relief="raised")
            self.set_none.config(relief="sunken")
            self.optmetric = None
            self.initdict['optimizemetric'] = None
            self.selectstatuslabel.configure(text=f"Selected Metric:\n {self.initdict['optimizemetric']}")

    def set_transistormetric(self):
        if self.initdict == None:
            self.statuslabel.configure(text="You MUST Select a truth table First")
        else:
            self.set_transistor.config(relief="sunken")
            self.set_power.config(relief="raised")
            self.set_delay.config(relief="raised")
            self.set_none.config(relief="raised")
            self.optmetric = 'Transistor'
            self.initdict['optimizemetric'] = 'Transistor'
            self.selectstatuslabel.configure(text=f"Selected Metric:\n {self.initdict['optimizemetric']}")

    def set_powermetric(self):
        if self.initdict == None:
            self.statuslabel.configure(text="You MUST Select a truth table First")
        else:
            self.set_transistor.config(relief="raised")
            self.set_power.config(relief="sunken")
            self.set_delay.config(relief="raised")
            self.set_none.config(relief="raised")
            self.optmetric = 'Power'

            self.initdict['optimizemetric'] = 'Power'
            self.selectstatuslabel.configure(text=f"Selected Metric:\n {self.initdict['optimizemetric']}")

    def set_delaymetric(self):
        if self.initdict == None:
            self.statuslabel.configure(text="You MUST Select a truth table First")
        else:
            self.set_delay.config(relief="sunken")
            self.set_transistor.config(relief="raised")
            self.set_power.config(relief="raised")
            self.set_none.config(relief="raised")
            self.initdict['optimizemetric'] = 'Delay'
            self.optmetric = 'Delay'
            self.selectstatuslabel.configure(text=f"Selected Metric:\n {self.initdict['optimizemetric']}")

    def set_HalfAdderInitQlark(self):
        self.set_2bitComparator.config(relief="raised")
        self.set_halfadder.config(relief="sunken")
        self.set_fulladder.config(relief="raised")

        CVS_constants.INPUTSTOTAL = 2
        CVS_constants.OUTPUTSTOTAL = 2

        self.initdict = {
                    'truthtable': [[0, 1, 1, 0], [0, 0, 0, 1]],                 # Truthtable
                    'circuitinputs': 2,                                         #
                    'circuitoutputs': 2,                                        #
                    'maxgatenum': 3,                                            # Total num of gates AI is allowed toplace
                    'allowedgatetypes': [GateType.AND.name,GateType.XOR.name],  # For Qlark             please dont touch
                    'maxsteps': 10,                                             # For Qlark             please dont touch
                    'totalthreads': 1,                                          # For Qlark threading   please dont touch
                    'trainingsetspthread': 1,                                    # For Qlark threading   please dont touch
                    'savepath': f'{getrootpath()}halfadder_qtable.pickle',
                    'optimizemetric':self.optmetric
                }
        self.statuslabel.configure(text=f"Half Adder Selected:\n{self.initdict['truthtable']}")



    def set_FullAdderInitQlark(self):
        self.set_2bitComparator.config(relief="raised")
        self.set_fulladder.config(relief="sunken")
        self.set_halfadder.config(relief="raised")

        CVS_constants.INPUTSTOTAL = 3
        CVS_constants.OUTPUTSTOTAL = 2

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
            'trainingsetspthread': 1,                    # For Qlark threading   please dont touch
            'savepath': f'{getrootpath()}fulladder_qtable.pickle',
            'optimizemetric': self.optmetric
        }
        self.statuslabel.configure(text=f"Full Adder Selected:\n{self.initdict['truthtable']}")
        self.selectstatuslabel.configure(text=f"Selected Metric:\n {self.initdict['optimizemetric']}")

    def set_2bitComparatorInitQlark(self):
        self.set_2bitComparator.config(relief="sunken")
        self.set_fulladder.config(relief="raised")
        self.set_halfadder.config(relief="raised")

        CVS_constants.INPUTSTOTAL = 4
        CVS_constants.OUTPUTSTOTAL = 3

        self.initdict = {
            'truthtable': [[0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0],[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],[0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0]],  # 2-bit comparator
            'circuitinputs': 4,  #
            'circuitoutputs': 3,  #
            'maxgatenum': 11,  # Total num of gates AI is allowed to place
            'allowedgatetypes': [GateType.AND.name,  # For Qlark             please dont touch
                                 GateType.XOR.name,  # For Qlark             please dont touch
                                 GateType.OR.name,
                                 GateType.NOR.name,
                                 GateType.NAND.name,
                                 GateType.XNOR.name,
                                 GateType.NOT.name
                                 ],  # For Qlark             please dont touch
            'maxsteps': 30,  # For Qlark             please dont touch
            'totalthreads': 1,  # For Qlark threading   please dont touch
            'trainingsetspthread': 1,  # For Qlark threading   please dont touch
            'savepath': f'{getrootpath()}2bitComparator_qtable.pickle',
            'optimizemetric': self.optmetric
        }
        self.statuslabel.configure(text=f"2 bit comparator Selected:\n{self.initdict['truthtable']}")
        self.selectstatuslabel.configure(text=f"Selected Metric:\n {self.initdict['optimizemetric']}")

class ThreadedQlarkClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker (I/O).
        """
        self.master = master

        # Create the queue
        self.queue = queue.Queue(  )

        # Set up the GUI part
        self.gui = QlarkGui(master, self.queue, self.endApplication)

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1
        # self.thread1 = threading.Thread(target=self.workerThread1)
        # self.thread1.start(  )

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodicCall(  )

    def periodicCall(self):
        """
        Check every 200 ms if there is something new in the queue.
        """
        self.gui.processIncoming(  )
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(200, self.periodicCall)

    def workerThread1(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select(  )'. One important thing to remember is that the thread has
        to yield control pretty regularly, by select or otherwise.
        """
        while self.running:
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following two lines with the real
            # thing.
            time.sleep(rand.random(  ) * 1.5)
            msg = rand.random(  )
            self.queue.put(msg)

    def endApplication(self):
        self.running = 0
def getrootpath():
    import os

    ROOT_DIR = os.path.abspath(os.curdir)
    dirs = ROOT_DIR.split('\\')
    if dirs[-1] == 'QLARK':
        dirs.pop()
    rootpath = ''
    for i in dirs:
        rootpath += i + '/'
    # print(rootpath)
    return rootpath



