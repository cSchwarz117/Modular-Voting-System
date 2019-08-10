import tkinter as tk


class start(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Welcome to MVS").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Login",
                  command=lambda: master.login()).pack()
        tk.Button(self, text="Exit",
                  command=lambda: master.exit()).pack()