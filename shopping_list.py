from tkinter import *
from tkinter import ttk # use themed Tk widgets

class MyWindow:
    def __init__(self, win):
        self.choices = ['apples', 'oranges', 'bread', 'milk', 'chicken', 'fish', 'eggs', 'salt', 'pepper']
        self.choicesvar = StringVar(value=self.choices)
        self.selected = []
        self.selectedvar = StringVar(value=self.selected)

        self.main = ttk.Frame(win, padding=10)
        self.lbox1 = Listbox(self.main, listvariable=self.choicesvar, selectmode=EXTENDED)
        self.lbox2 = Listbox(self.main, listvariable=self.selectedvar, selectmode=EXTENDED)

        self.lbl1 = ttk.Label(self.main, text='Options')
        self.lbl2 = ttk.Label(self.main, text='Buy Now')

        self.btn_frm = ttk.Frame(self.main, padding=10)
        self.btn1 = ttk.Button(self.btn_frm, width=3, text="\N{RIGHTWARDS ARROW}")
        self.btn2 = ttk.Button(self.btn_frm, width=3, text="\N{RIGHTWARDS PAIRED ARROWS}", command=self.add_all)
        self.btn3 = ttk.Button(self.btn_frm, width=3, text="\N{LEFTWARDS PAIRED ARROWS}", command=self.remove_all)
        self.btn4 = ttk.Button(self.btn_frm, width=3, text="\N{LEFTWARDS ARROW}")

        self.btn1.bind("<Button-1>", lambda e: self.add(self.lbox1.curselection()))
        self.lbox1.bind("<Double-1>", lambda e: self.add(self.lbox1.curselection()))
        self.btn4.bind("<Button-1>", lambda e: self.remove(self.lbox2.curselection()))
        self.lbox2.bind("<Double-1>", lambda e: self.remove(self.lbox2.curselection()))

        self.btn1.grid(column=0, row=0)
        self.btn2.grid(column=0, row=1)
        self.btn3.grid(column=0, row=2)
        self.btn4.grid(column=0, row=3)

        self.lbl1.grid(column=0, row=0)
        self.lbl2.grid(column=2, row=0)
        self.lbox1.grid(column=0, row=1, sticky="nesw")
        self.lbox2.grid(column=2, row=1, sticky="nesw")
        self.btn_frm.grid(column=1, row=0, rowspan=2)

        self.main.grid(column=0, row=0, sticky="nesw")

        self.main.columnconfigure(0, weight=1)
        self.main.columnconfigure(2, weight=1)
        self.main.rowconfigure(1, weight=1)

        win.columnconfigure(0, weight=1)
        win.rowconfigure(0, weight=1)

    def add(self, idxs):
        if len(idxs) > 0:
            start_pos = len(self.selected)
            for item in idxs[::-1]:
                self.selected.insert(start_pos, self.choices[int(item)])
                self.choices.remove(self.choices[int(item)])
            self.selectedvar.set(self.selected)
            self.choicesvar.set(self.choices)
            self.lbox1.selection_clear(0, self.lbox1.size() + 1)

    def remove(self, idxs):
        if len(idxs) > 0:
            start_pos = len(self.choices)
            for item in idxs[::-1]:
                self.choices.insert(start_pos, self.selected[int(item)])
                self.selected.remove(self.selected[int(item)])
            self.selectedvar.set(self.selected)
            self.choicesvar.set(self.choices)
            self.lbox2.selection_clear(0, self.lbox2.size() + 1)

    def add_all(self):
        self.add(range(len(self.choices)))

    def remove_all(self):
        self.remove(range(len(self.selected)))

window = Tk()
mywin = MyWindow(window)
window.title('Shopping List')
window.eval('tk::PlaceWindow . center') # approximately center the window on the screen
window.mainloop()
