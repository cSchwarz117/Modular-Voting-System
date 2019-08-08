import tkinter


class logIn(tkinter.Toplevel):

    def __init__(self, parent):
        tkinter.Toplevel.__init__(self)
        self.parent = parent
        self.title("MVS - Login")
        self.geometry('250x150')

        self.usr = tkinter.StringVar()
        self.pwd = tkinter.StringVar()

        self.label = tkinter.Label(self, text='Username').grid(row=2, column=1)

        self.entry = tkinter.Entry(self, textvariable=self.usr).grid(row=2, column=3)

        self.label = tkinter.Label(self, text='Password').grid(row=4, column=1)

        self.entry = tkinter.Entry(self, textvariable=self.pwd).grid(row=4, column=3)

        self.login_button = tkinter.Button(self, text='Login', command=self.on_login).grid(row=6, column=3)

#        self.entry.bind("<Return>", self.on_login)
        self.attributes("-topmost", True)

    def on_login(self, event=None):
        self.destroy()
 #       self.parent.show()

    def show(self):
#        self.wm_deiconify()
        self.mainloop()
#        self.entry.focus_force()
#        self.wait_window()
        usrN = self.usr.get()
        pwrd = self.pwd.get()
        cred = {"username": usrN, "password": pwrd}
        return cred




  #      self.mainloop()
