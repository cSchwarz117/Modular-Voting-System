from server_state import server_state
import sys
sys.path.append("..")
from server_data import server_data
import pickle

class startBallot(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.adminOpts = {
            "Instructions": "Welcome to the election, <user>, what would you like to do?",
            "type": "MultipleChoice",
            "1": "Review ballot",
            "2": "Start ballot",
            "3": "Continue ballot"}

    def enter(self, conn, election, user):
        self.conn = conn
        out = pickle.dumps(self.adminOpts)
        self.conn.sendall(out)
        self.review = False
        self.start = False
        self.continueB = False
        return None

    def process(self, data, election, user):
        dict = pickle.loads(data)
        ans = dict["ans"]
        if ans == "1":
            self.review = True
        if ans == "2":
            self.start = True
        if ans == "3":
            self.continueB = True


        return (election, user)

    def execute(self, data, election, user):
        if self.review:
            return None
        else:
            return True

    def exit(self, data, election, user):
        out = pickle.dumps(self.u)
        self.conn.sendall(out)
        self.conn = None
        return None