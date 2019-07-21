#!/usr/bin/env python3

import socket
import states
from server_fsm import server_fsm
from states.login_state import login_state
from server_data import server_data
import pickle

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    fsm = server_fsm()
    curState = login_state()
    elec = None
    usr = None
    server_data()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        if not data:
            print("something went wrong")
            exit(1)
        curState.enter(data, conn, elec, usr)
        while True:
            elec, usr = curState.process(data, elec, usr)
            s = curState.execute(data, elec, usr)
            if s is not None:
                curState.exit(data, elec, usr)
                curState = s
                curState.enter(data, conn, elec, usr)

            data = conn.recv(1024)
            if not data:
                print("something went wrong")
                exit(1)




