#!/usr/bin/env python3

import socket
import pickle

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
users = {
    "Jane": "123",
    "Joe": "abc",
    "Fred": "spacepirate",
    "Anne": "netflix"
    }

admins = []
voters = []

admins.append("Anne")
voters.append("Jane")
voters.append("Fred")
voters.append("Joe")

adminopts = {
	"Instructions": "I see you are an admin! Welcome! Please choose from the following options",
    "type" : "MultipleChoice" ,
    "1" : "Create Election",
    "2" : "Edit Election",
	"3" : "View Results"
}

voteropts = {
	"Instructions": "I see you are a voter, please choose from the following options",
    "type" : "MultipleChoice" ,
    "1" : "Candidate A",
    "2" : "Candidate B",
}

incorrectpass = {
	"Instructions": "Password Incorrect",
    "type" : "PasswordFail" ,
}

incorrectuser = {
	"Instructions": "Username Incorrect",
    "type" : "UsernameFail" ,
}
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            dict = pickle.loads(data)
            pswd = dict["password"]
            usr = dict["username"]
            ret = {}
            if usr in users.keys():
                if pswd == users[usr]:
                    if usr in admins:
                        ret = adminopts
                    else:
                        ret = voteropts
                    out = pickle.dumps(ret)
                    conn.sendall(out)
                    break
                else:
                    ret = incorrectpass
            else:
                ret = incorrectuser
            out = pickle.dumps(ret)
            conn.sendall(out)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            dict = pickle.loads(data)
            #not sure what to do here
            print(dict)
