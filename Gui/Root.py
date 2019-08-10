import tkinter as tk
from frames.login import loginF
from frames.StartPage import start
from messageInstance import instance
import socket

class root(tk.Tk, instance):
    def __init__(self, sock):
        tk.Tk.__init__(self)
        self.sock = sock
        self.instance = instance(sock)
        self.geometry('300x300')
        self._frame = start(self)
        self._frame.pack()
 #       s = 'start'
 #       data = {'type': s}
 #       self.switch_frame(data)

    def switch_frame(self, data):
        print(data)
        self.instance.send(data)
        data = self.instance.rec()
        print(data)
        frame_class = self.typeCheck(data)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def typeCheck(self, data):
        if data['type'] == 'MultipleChoice':
            return start
        if data['type'] == 'start':
            print('here')
            return start
        if data['type'] == 'RankedChoice':
            return

        if data['type'] == 'date':
            return
        if data['type'] == 'char25':
            return
        if data['type'] == 'PasswordFail':
            return
        if data['type'] == 'UsernameFail':
            return
        if data['type'] == 'StrArray':
            return
        if data['type'] == 'logoff':
            return True
        else:
            print('Data Type error')
            return

    def login(self):
        new_frame = loginF(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def exit(self):
        exit(0)


HOST = '127.0.0.1' # The server's hostname of IP address
PORT = 65432       #  The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    app = root(s)
    app.mainloop()