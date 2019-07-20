from states.server_state import server_state
import sys
sys.path.append("..")
from server_data import server_data
import pickle

class adminOptions(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.adminOpts = {
            "Instructions": "I see you are an admin! Welcome! Please choose from the following options",
            "type": "MultipleChoice",
            "1": "Create Election",
            "2": "Edit Election",
            "3": "View Results"}

    def enter(self, data, conn, election, user):
        self.conn = conn
        out = pickle.dumps(self.adminOpts)
        self.conn.sendall(out)
        self.createElection = False
        self.editElection = False
        self.viewResults = False
        return None

    def process(self, data, election, user):
        dict = pickle.loads(data)
        ans = dict["ans"]
        if ans == "1":
            self.createElection = True
        if ans == "2":
            self.editElection = True
        if ans == "3":
            self.viewResults = True


        return (election, user)

    def execute(self, data, election, user):
        if self.createElection:
            return None
        else:
            return True

    def exit(self, data, election, user):
        out = pickle.dumps(self.u)
        self.conn.sendall(out)
        self.conn = None
        return None