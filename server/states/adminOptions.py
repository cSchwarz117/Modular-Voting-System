from states.server_state import server_state
import states
import states.login_state
from server_data import server_data
from states.createElection import createElection
import sys
sys.path.append("..")
import pickle

from messageInstance import instance
class adminOptions(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.adminOpts = {
            "Instructions": "I see you are an admin! Welcome! Please choose from the following options",
            "type": "MultipleChoice",
            "1": "Create Election",
            "2": "Edit Election",
            "3": "View Results",
            "4": "Log Off"}

    def enter(self, data, conn, election, user):
       # self.conn = conn
       # out = pickle.dumps(self.adminOpts)
       # self.conn.sendall(out)
        instance.send(self.adminOpts)
        self.create_election = False
        self.editElection = False
        self.viewResults = False
        self.logOff = False
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
        if ans == "4":
            logoff = {
                "Instructions": "Logged off",
                "type": "logoff"}
            instance.send(logoff)
            self.logOff = True

        return (election, user)

    def execute(self, data, election, user):
        if self.create_election:
            return createElection()
        if self.logOff:
            return states.login_state.login_state()
        else:
            return None

    def exit(self, data, election, user):
        return None