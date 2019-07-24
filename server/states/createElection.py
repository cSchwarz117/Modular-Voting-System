from states.server_state import server_state
from election import election
from states.createDate import createDate
import sys

sys.path.append("..")
from server_data import server_data
import pickle

from messageInstance import instance
class createElection(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.instruction = {
            "Instructions": "It looks like you are creating an election: What would you like to call your election?",
            "type": "char25",}

    def enter(self, data, conn, election, user):
        instance.send(self.instruction)
       # self.conn = conn
       # out = pickle.dumps(self.instruction)
       # self.conn.sendall(out)
        return None

    def process(self, data, elec, user):
        dict = data
        ans = dict["ans"]
        elec = election()
        elec.name = ans
        return (elec, user)

    def execute(self, data, election, user):
        return createDate()

    def exit(self, data, election, user):
        return None