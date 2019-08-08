import tkinter
from windows.login import logIn
from messageInstance import instance
from windows.multChoice import multChoice



class Mm(tkinter.Tk, instance):

    def __init__(self, sock):
        tkinter.Tk.__init__(self)
        #self.root = tkinter.Toplevel()
        self.wm_geometry("400x200")
        self.title("MVS")
        self.sock = sock
        self.log = logIn(self)
 #       self.choice = multChoice(self)
        self.instance = instance(sock)
  #      self.var = tkinter.Toplevel(self)

    def logIn(self):
#        log = logIn(self)
        cred = self.log.show()
        self.instance.send(cred)
        inst = self.instance.rec()
        return inst

    def menuLoop(self):
        while True:
            opt = False
            while opt is False:
                opt = self.logIn()
            while opt['type'] != 'logoff':
                print(opt)
                inp = self.typeCheck(opt)
                print(inp)
                self.instance.send(inp)
                opt = self.instance.rec()

    def typeCheck(self, data):
        if data['type'] == 'MultipleChoice':
            return self.choice(data)

        if data['type'] == 'date':
            return self.date(data)
        if data['type'] == 'char25':
            return self.char25(data)
        if data['type'] == 'PasswordFail':
            return self.pFail(data)
        if data['type'] == 'UsernameFail':
            return self.uFail(data)
        if data['type'] == 'StrArray':
            return self.StrArray(data)
        if data['type'] == 'logoff':
            print(data['Instructions'])
            return True
        else:
            print('Data Type error')
            return

    def choice(self, data):
        ch = multChoice(self)
        cred = ch.show()
#        print(cred)
        return cred