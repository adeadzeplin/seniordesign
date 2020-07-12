import tkinter
import time
import threading
import random
import queue
from tkinter import Tk, Label, Button, Checkbutton, IntVar, StringVar, messagebox, OptionMenu, Entry
from CVS_.CVS_gate_class import GateType
# from CVS_ import CVS_constants


class LucaGui:
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
        master.title("LUCA MENU")
        self.circuit_type = StringVar(master)
        tablecolum = 0
        self.circuit_type.set("Circuit")
        self.labelselect = Label(master, text="Select Circuit")
        self.labelselect.grid(row=0, column=tablecolum)
        self.circuit_select = OptionMenu(master, self.circuit_type, "Half-Adder", "Full-Adder", "1 Bit Comparator", "2 Bit Comparator")
        self.circuit_select.grid(row=1, column=tablecolum)
        self.num_rows = Entry(master, bd = 5)
        self.num_rows.insert(0, 'Number of Rows')
        self.labelarrayrow = Label(master, text='Define Array Size')
        self.labelarrayrow.grid(row=2, column=tablecolum)
        self.num_rows.grid(row=3, column=tablecolum)
        self.num_cols = Entry(master, bd=5)
        self.num_cols.insert(0, 'Number of Columns')
        self.labelarraycol = Label(master, text='Define Array Size')
        self.labelarraycol.grid(row=4, column=tablecolum)
        self.num_cols.grid(row=5, column=tablecolum)
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
        # Run Luca button
        self.runqlark_button = Button(master, text="\nRun Luca\n", width=15, command=self.checkforcircuit)
        self.runqlark_button.grid(row=1, column=2)
        # Status Update
        self.statuslabel = Label(master, text="no truthtable selected")
        self.statuslabel.grid(row=2, column=2)

        #loop counter display
        self.looplabel = Label(master,text="Generation: 1")
        self.looplabel.grid(row=0, column=5)

        #circuit output labe0l ------------
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
                if isinstance(msg, int):
                    textdata = f'Generation: {msg}'
                    self.looplabel.configure(text=textdata)
                elif isinstance(msg,str):
                    self.circuitoutputlabel.configure(text=msg)
                    self.circuitmetricslabel.configure(text='No Metrics for this circuit')
                elif isinstance(msg, dict):
                    # ("Correct Circuit", textgoodcircuitstring,metrics)
                    # metric_dict = {
                    #     "CircuitStatus": "Correct Circuit",
                    #     "CircuitPrintout": textgoodcircuitstring,
                    #     "PercentCorrect": metrics[0],
                    #     "PowerConsumed": metrics[1],
                    #     "TimeDelay": metrics[2],
                    #     "TransistorCount": metrics[3]
                    # }
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

    def runLuca(self):
        print("RUNLICA")
        print(self.num_rows.get())

    def checkforcircuit(self):
        if self.circuit_type.get() == None or self.circuit_type.get() == 'Circuit':

            self.statuslabel.configure(text="You MUST Select a truth table")
            pass
        else:
            print(self.circuit_type.get())
            self.thread = threading.Thread(target=self.runLuca())
            self.thread.start()

    def set_nonemetric(self):
        if self.initdict == None:
            self.statuslabel.configure(text="You MUST Select a truth table First")
        else:
            self.set_transistor.config(relief="raised")
            self.set_power.config(relief="raised")
            self.set_delay.config(relief="raised")
            self.set_none.config(relief="sunken")
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
            self.selectstatuslabel.configure(text=f"Selected Metric:\n {self.initdict['optimizemetric']}")



class ThreadedLucaClient:
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
        self.gui = LucaGui(master, self.queue, self.endApplication)

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



