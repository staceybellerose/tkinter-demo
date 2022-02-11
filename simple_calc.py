from tkinter import *
from tkinter import ttk # use themed Tk widgets

class MyWindow:
    def __init__(self, win):
        # variables used in computations
        self.first = StringVar()
        self.second = StringVar()
        self.result = StringVar()
        
        # frame for clean background color
        self.frm = ttk.Frame(master=win)
        self.frm['padding'] = 5

        # label widgets for the entry fields
        self.lbl1 = ttk.Label(master=self.frm, text='Y')
        self.lbl2 = ttk.Label(master=self.frm, text='X')
        self.lbl3 = ttk.Label(master=self.frm, text='=')
        self.lbl4 = ttk.Label(master=self.frm, text="Enter integers into X and Y,\nthen select an operation.")

        # entry field widgets, linked to computation variables
        self.t1 = ttk.Entry(master=self.frm, textvariable=self.first)
        self.t2 = ttk.Entry(master=self.frm, textvariable=self.second)
        self.t3 = ttk.Entry(master=self.frm, textvariable=self.result)

        # button widgets to trigger computations
        self.btn1 = ttk.Button(master=self.frm, width=3, text='+', command=self.add)
        self.btn2 = ttk.Button(master=self.frm, width=3, text="\N{MINUS SIGN}", command=self.sub)
        self.btn3 = ttk.Button(master=self.frm, width=3, text="\N{MULTIPLICATION SIGN}", command=self.mult)
        self.btn4 = ttk.Button(master=self.frm, width=3, text="\N{DIVISION SIGN}")
        self.btn4.bind('<Button-1>', self.div) # explicit binding of mouse button 1 press to trigger a command

        # place all the widgets
        self.lbl4.grid(row=0, column=0, columnspan=2, sticky="sw")
        self.lbl1.grid(row=1, column=0)
        self.lbl2.grid(row=2, column=0)
        self.lbl3.grid(row=3, column=0)
        
        self.t1.grid(row=1, column=1, sticky="ew")
        self.t2.grid(row=2, column=1, sticky="ew")
        self.t3.grid(row=3, column=1, sticky="ew")
        
        self.btn1.grid(row=3, column=2)
        self.btn2.grid(row=2, column=2)
        self.btn3.grid(row=1, column=2)
        self.btn4.grid(row=0, column=2, sticky="s")

        self.frm.grid(row=0, column=0, sticky="nesw")
        win.columnconfigure(0, weight=1)
        win.rowconfigure(0, weight=1)
        self.frm.columnconfigure(1, weight=1)
        self.frm.rowconfigure(0, weight=1)

    def add(self):
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        # setting the `result` variable will trigger the entry field t3 to automatically update
        self.result.set(int(num1+num2))

    def sub(self):
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        self.result.set(int(num1-num2))

    def mult(self):
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        self.result.set(int(num1*num2))

    def div(self):
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        self.result.set(int(num1/num2))

window = Tk()
mywin = MyWindow(window)
window.title('Simple Calculator')
window.eval('tk::PlaceWindow . center') # approximately center the window on the screen
window.mainloop()

