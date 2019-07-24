from states.server_state import server_state
from election import election
import sys

sys.path.append("..")
from server_data import server_data
from states.chooseDate import chooseDate
from states.createQuestion import createQuestion
from messageInstance import instance
import pickle


class createDate(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.chooseStart = False
        self.immediately = False
        self.instruction = {
            "Instructions": "It looks like your election is called <replace>: When would you like your election to start?",
            "type": "MultipleChoice",
            "1": "Immediately",
            "2": "Choose Date"}

    def enter(self, data, conn, elec, user):
        ret = self.instruction.copy()
        ret["Instructions"] = ret["Instructions"].replace("<replace>", elec.name)
        instance.send(ret)
       # self.conn = conn
       # out = pickle.dumps(ret)
       # self.conn.sendall(out)
        return None

    def process(self, data, elec, user):
        dict = data
        ans = dict["ans"]
        if ans == "2":
            self.chooseStart = True
        if ans == "1":
            self.immediately = True
        return (elec, user)

    def execute(self, data, elec, user):
        if self.chooseStart:
            return chooseDate()
        if self.immediately:
            return createQuestion()
        return True

    def exit(self, data, election, user):
        return None