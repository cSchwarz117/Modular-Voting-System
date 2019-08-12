import tkinter as tk

class StrArrayF(tk.Frame):

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.labels = []
        self.entries = []
        self.ans = {}
        tk.Label(self, text=data['Instructions']).grid(row=0, column=0)

        self.num = tk.IntVar()

        self.label = tk.Label(self, text='How many options are there?').grid(row=2, column=0)

        self.entry1 = tk.Entry(self, textvariable=self.num).grid(row=3, column=0)

        self.Ok1_button = tk.Button(self, text='ok', command=lambda: self.on_button()).grid(row=4, column=0)

    def on_button(self):
        ch = self.num.get()
        for widget in tk.Frame.winfo_children(self):
            widget.destroy()

        for i in range(int(ch)):
            self.ans[i] = (tk.StringVar())
            self.labels.append(tk.Label(self, text=i).grid(row=i+5, column=0))
            self.entries.append(tk.Entry(self, textvariable=self.ans[i]).grid(row=i+5, column=1))
        self.Ok2_button =  tk.Button(self, text='ok', command=lambda: self.on_button2()).grid(row=ch, column=1)

    def on_button2(self):
        cred = {}

        for x in self.ans:
            entry = self.ans[x].get()
            print(entry)
            cred[x] = entry
            self.parent.switch_frame(cred)
#    def StrArray(self, data):
#        print(data['Instructions'])
#        x = input('How many options do you want?')
#        cred = {}
#        for i in range(int(x)):
#            cred[i] = input("Option: ")
#        return cred