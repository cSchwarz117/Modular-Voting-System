import tkinter
import socket
from windows.mainMenu import Mm
#from windows.login import log
#main = tkinter.Tk()
#main.title("MVS")
#login = log()
#login.enter()
#login.mainloop()
#dirt = login.show()
#print(dirt)

#main.mainloop()
#
#main.title("MVS GUI")

#label = tkinter.Label(main, text=").pack()

#main.mainloop()

HOST = '127.0.0.1' # The server's hostname of IP address
PORT = 65432       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    root = Mm(s)
    root.menuLoop()
 #   root.mainloop()

 #   root.wm_geometry("400x400")
 #   dirt = Mm(root, s) # .pack(fill='both', expand=True)
 #   dirt.logIn()
  #  dirt.mainloop()


