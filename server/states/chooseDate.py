from states.server_state import server_state
from election import election
import sys
import datetime

sys.path.append("..")
from server_data import server_data
import pickle
from messageInstance import instance

class chooseDate(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.chooseStart = False
        self.immediately = False
        self.dateValid = False
        self.instruction = {
            "Instructions": "Please pick a date for the <replace> election to start",
            "type": "date",}

    def enter(self, data, conn, elec, user):
        ret = self.instruction.copy()
        ret["Instructions"].replace("<replace>", elec.name)
        self.conn = conn
        instance.send(ret)
        #out = pickle.dumps(ret)
        #self.conn.sendall(out)
        return None

    def process(self, data, elec, user):
        dict = data
        ans = dict["ans"]
        #validate date
        elec.date = ans
        self.dateValid = True
        return (elec, user)

    def execute(self, data, election, user):
        if self.dateValid:
            return True

    def exit(self, data, election, user):
        return None