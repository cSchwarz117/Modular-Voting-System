import tkinter


class multChoice(tkinter.Toplevel):

    def __init__(self, parent):
        tkinter.Toplevel.__init__(self)
        self.parent = parent
        self.title("MVS")
        self.geometry('400x400')

 #       self.inst = data['Instructions']
 #       del data['type']
 #       del data['Instructions']
        self.choice = tkinter.StringVar()

        self.label = tkinter.Label(self, text='cat').grid(row=2, column=1)

        self.entry = tkinter.Entry(self, textvariable=self.choice).grid(row=2, column=3)

        self.enter_button = tkinter.Button(self, text='OK', command=self.on_choice).grid(row=6, column=3)

    def on_choice(self, event=None):
        self.destroy()

    def show(self):
        self.mainloop()
        choice = self.choice.get()
        return choice

