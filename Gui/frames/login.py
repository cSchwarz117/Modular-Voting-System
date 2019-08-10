import tkinter as tk


class loginF(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="MVS - Login")

        self.usr = tk.StringVar()
        self.pwd = tk.StringVar()
        self.parent = parent

        self.label = tk.Label(self, text='Username').grid(row=2, column=1)

        self.entry1 = tk.Entry(self, textvariable=self.usr).grid(row=2, column=3)

        self.label = tk.Label(self, text='Password').grid(row=4, column=1)

        self.entry2 = tk.Entry(self, textvariable=self.pwd).grid(row=4, column=3)

 #       cred = {'username': self.usr.get(), 'password': self.pwd.get()}

        self.login_button = tk.Button(self, text='Login', command=lambda: self.on_button()).grid(row=6, column=3)


    def on_button(self):
        Uname = self.usr.get()
        pWord = self.pwd.get()
        cred = {'username': Uname, 'password': pWord}
        self.parent.switch_frame(cred)
