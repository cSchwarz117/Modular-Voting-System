import tkinter as tk

class char25F(tk.Frame):

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        tk.Label(self, text=data['Instructions']).grid(row=0, column=0)

        del data['type']
        del data['Instructions']

        self.inp = tk.StringVar()

        self.entry1 = tk.Entry(self, textvariable=self.inp).grid(row=1, column=0)

        self.button = tk.Button(self, text='OK', command=lambda: self.on_button()).grid(row=2, column=0)

    def on_button(self):
        inp1 = self.inp.get()

        cred = {'ans': inp1}
        self.parent.switch_frame(cred)

#    def char25(self, data):
#        print(data['Instructions'])
#        select = input()
#        ans = {"ans": select}
#        return ans