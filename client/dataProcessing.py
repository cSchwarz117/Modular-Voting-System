import socket
import pickle

class data_processing():

#    def __init__(self, s):
#        self.sock = s

    def login(self):
        usr = input('Please enter your Username: ')
        pwd = input('Please enter your Password: ')

        cred = {"username": usr, "password": pwd}
        out = pickle.dumps(cred)
        self.sock.sendall(out)
        data = self.sock.recv(1024)
        data = pickle.loads(data)
        print('Recieved', repr(data))
