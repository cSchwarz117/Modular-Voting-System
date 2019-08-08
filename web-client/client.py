import socket
import sys
sys.path.append('../')
from messageInstance import instance

class pyClient:


    def conn(self, HOST, PORT):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

#           terminal = menu_interface(s)
#         terminal.menuLoop()


