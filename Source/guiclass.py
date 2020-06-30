from tkinter import Tk, Label, Button
from QLARK.qlark_main import qlarklearn
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("AI CIRCUIT DESIGN")

        self.label = Label(master, text="pick a bot to start learning")
        self.label.pack()

        self.qlarkrun_button = Button(master, text="Run Qlark", command=self.runQlark)
        self.qlarkrun_button.pack()

        self.cvsrun_button = Button(master, text="Run CVS", command=self.yeet)
        self.cvsrun_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    def runQlark(self):
        desired_truthtable = [[0, 1, 1, 0], [0, 0, 0, 1]]  # Half Adder circuit Truth Table
        qlarklearn(desired_truthtable)

    def yeet(self):
        print("Will can figure this part out")

