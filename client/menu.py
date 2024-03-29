import sys
sys.path.append("..")
from messageInstance import instance
from dataParse import parser


class menu_interface(instance, parser):

    def __init__(self, sock):
        self.sock = sock
        instance(sock)

    def logIn(self, user_input=""):
        print("*****Welcome to MVS*****")
        print("1. Login")
        print("2. Exit")
        print(" ")
        if user_input == "":
            user_input = input()

        if user_input == "1":
            usr = input('Please enter your Username: ')
            pwd = input('Please enter your Password: ')
            cred = {"username": usr, "password": pwd}
            self.send(cred)
            inst = self.rec()
            return inst

        if user_input == "2":
            exit(0)

    def menuLoop(self):

        while True:
            opt = False
            while opt is False:
                opt = self.logIn()
            while opt['type'] != 'logoff':
                inp = self.typeCheck(opt)
                self.send(inp)
#               print(inp)
                opt = self.rec()
 #              print(opt)



