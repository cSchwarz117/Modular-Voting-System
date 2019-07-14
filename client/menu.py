from dataProcessing import data_processing


class menu_interface(data_processing):

    def __init__(self, sock=""):
        if sock == "":
            return print("No Connection!")
        self.sock = sock

    def start_menu(self, user_input=""):
        print("*****Welcome to MVS*****")
        print("1. Login")
        print("2. Register")
        print("3. Forgot Username/Password")
        print("4. Exit")
        print(" ")
        if user_input == "":
            user_input = input()

        if user_input == "1":
            self.login_menu()
        if user_input == "2":
            self.register_menu()
        if user_input == "3":
            self.forgot_menu()
        if user_input == "4":
            return
        else:
            print("Invalid Input!")
        self.start_menu("")

    def login_menu(self, user_input=""):
        print("*****Login Menu*****")
        print("1. Admin login")
        print("2. Voter login")
        print("3. Go back")
        if user_input == "":
            user_input = input()

        if user_input == "1":
            self.login()
        if user_input == "2":
            return
        if user_input == "3":
            self.start_menu("")
        else:
            print("Invalid Input!")
        self.login_menu("")

    def register_menu(self):
        return

    def forgot_menu(self):
        return
