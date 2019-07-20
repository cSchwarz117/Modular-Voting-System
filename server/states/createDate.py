from server_state import server_state
from election import election
import sys

sys.path.append("..")
from server_data import server_data
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

    def enter(self, conn, elec, user):
        ret = self.instruction.copy()
        ret["Instructions"].replace("<replace>", elec.name)
        self.conn = conn
        out = pickle.dumps(ret)
        self.conn.sendall(out)
        return None

    def process(self, data, elec, user):
        dict = pickle.loads(data)
        ans = dict["ans"]
        if ans == "2":
            self.chooseStart = True
        if ans == "1":
            self.immediately = True
        return (elec, user)

    def execute(self, data, election, user):
        if self.chooseStart:

        return True

    def exit(self, data, election, user):
        out = pickle.dumps(self.u)
        self.conn.sendall(out)
        self.conn = None
        return None