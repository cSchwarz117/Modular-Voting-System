from states.server_state import server_state

from server_data import server_data
from states.createElection import createElection
import sys
sys.path.append("..")
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
        self.create_election = False
        self.editElection = False
        self.viewResults = False
        return None

    def process(self, data, election, user):
        dict = data
        ans = dict["ans"]
        if ans == "1":
            self.create_election = True
        if ans == "2":
            self.editElection = True
        if ans == "3":
            self.viewResults = True


        return (election, user)

    def execute(self, data, election, user):
        if self.create_election:
            return createElection()
        else:
            return None

    def exit(self, data, election, user):
        return None