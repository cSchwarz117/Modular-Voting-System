from messanger import message


class menu_interface(message):

    def __init__(self, sock):
        self.sock = sock

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
            inst = self.recv()
#            print(inst)


        if user_input == "2":
            exit(0)
 #       else:
 #           print("Invalid Input!")