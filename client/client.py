#Code goes here

import socket
import pickle

HOST = '127.0.0.1' # The server's hostname of IP address
PORT = 65432       #  The port used by the server

usr = input('Please enter your Username: ')
pwd = input('Please enter your Password: ')

cred = {"username": usr, "password": pwd}
#outfile = open('cred', 'wb')
#pickle.dump(cred, outfile)
#outfile.close()

out = pickle.dumps(cred)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(out)
    data = s.recv(1024)

data = pickle.loads(data)

print('Recieved', repr(data))

