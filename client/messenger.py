import socket
import pickle

class message():

#    def __init__(self, s):
#        self.sock = s

    def send(self, cred):

        out = pickle.dumps(cred)
        self.sock.sendall(out)


    def recv(self):
        data = self.sock.recv(1024)
        data = pickle.loads(data)
        return data
