import socket
#import pickle
from menu import menu_interface


HOST = '127.0.0.1' # The server's hostname of IP address
PORT = 65432       #  The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    terminal = menu_interface(s)
    terminal.menuLoop()

#    data = s.recv(1024)

#print('Recieved', repr(data))

