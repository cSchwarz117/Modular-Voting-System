import tkinter as tk

class multiF(tk.Frame):

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.button = []

        tk.Label(self, text=data['Instructions']).grid(row=0, column=0)

        del data['type']
        del data['Instructions']

 #       i = 1
        for key, val in data.items():
            self.button.append(tk.Button(self, text=val, command=lambda key=key: self.on_click(key)))
            self.button[int(key)-1].grid(column=0, row=int(key)+1)

    def on_click(self, choice):
        cred = {'ans': choice}
        print(cred)
        self.parent.switch_frame(cred)

        pack = {'ans': '1'}

#        self.parent.switch_frame(pack)


 #   def choice(self, data):
 ##       del data['type']
  #      print(data['Instructions'])
  #      del data['Instructions']
  #      for key, val in data.items():
  #          print(key, ": ", val)
  #      select = input()
  #      cred = {"ans": select}
  #      return cred