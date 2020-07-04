import tkinter
import time
import threading
import random
import queue
from tkinter import Tk, Label, Button, Checkbutton,IntVar, StringVar,messagebox
from CVS_.CVS_gate_class import GateType
import QLARK.qlark_threading as qt


class QlarkGui:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        # Set up the GUI
        # console = tkinter.Button(master, text='Done', command=endCommand)
        # console.pack(  )
        # Add more GUI stuff here depending on your specific needs
        self.master = master
        master.geometry("900x600+300+100")

        self.initdict = None

        master.title("QLARK STETUP MENU")


        self.labelselect = Label(master, text="Select Truth Table")
        self.labelselect.grid(row=0, column=0)
        # SELECT HALFADDER
        self.set_halfadder = Button(master, text="\nhalf adder\n", width=15, command=self.set_HalfAdderInitQlark)
        self.set_halfadder.grid(row=1, column=0)
        # SELECT FULLADDER
        self.set_fulladder = Button(master, text="\nfull adder\n", width=15, command=self.set_FullAdderInitQlark)
        self.set_fulladder.grid(row=2, column=0)

        # SPACER COLUMN
        self.label0 = Label(master, text="", width=10)
        self.label0.grid(row=0, column=1)

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
        self.looplabel.grid(row=3, column=0)

        #circuit output display
        self.outputlabel = Label(master,text="Circuit Printout:")
        self.outputlabel.grid(row=4, column=5)
        # circuit output display
        self.outputlabel = Label(master, text="Circuit Data goes here")
        self.outputlabel.grid(row=5, column=5)



    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize(  ):
            try:
                msg = self.queue.get(0)
                # Check contents of message and do whatever is needed. As a
                # simple test, print it (in real life, you would
                # suitably update the GUI's display in a richer fashion).
                # print(type(msg))
                if isinstance(msg,int):
                    textdata = f'Cycle Number: {msg}'
                    self.looplabel.configure(text=textdata)
                elif isinstance(msg,str):
                    self.outputlabel.configure(text=msg)

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
            learnflag, qai = qt.Needlethreading(self.initdict,self.queue)
            # textstring = qai.environment.getprintoutstring()
            print("going in")
            textstring = qai.environment.getfancyprintoutstring()
            # print(textstring)
            self.queue.put(textstring)



            if learnflag:
                print(f"The AI Learned on the {whilecounter}th pass of the infiniteLoop")
                break



    def set_HalfAdderInitQlark(self):

        self.set_halfadder.config(relief="sunken")
        self.set_fulladder.config(relief="raised")

        self.initdict = {
                    'truthtable': [[0, 1, 1, 0], [0, 0, 0, 1]],                 # Truthtable
                    'circuitinputs': 2,                                         #
                    'circuitoutputs': 2,                                        #
                    'maxgatenum': 2,                                            # Total num of gates AI is allowed toplace
                    'allowedgatetypes': [GateType.AND.name,GateType.XOR.name],  # For Qlark             please dont touch
                    'maxsteps': 10,                                             # For Qlark             please dont touch
                    'totalthreads': 1,                                          # For Qlark threading   please dont touch
                    'trainingsetspthread': 1,                                    # For Qlark threading   please dont touch
                    'savepath': f'{getrootpath()}halfadder_qtable.pickle'
                }
        self.statuslabel.configure(text=f"Half Adder Selected:\n{self.initdict['truthtable']}")


    def set_FullAdderInitQlark(self):

        self.set_fulladder.config(relief="sunken")
        self.set_halfadder.config(relief="raised")

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
            'savepath': f'{getrootpath()}fulladder_qtable.pickle'
        }
        self.statuslabel.configure(text=f"Full Adder Selected:\n{self.initdict['truthtable']}")


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
    dirs.pop()
    rootpath = ''
    for i in dirs:
        rootpath += i + '/'
    # print(rootpath)
    return rootpath



