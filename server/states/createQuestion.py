from server_state import server_state
from election import election
import sys

sys.path.append("..")
from server_data import server_data
import pickle


class createQuestion(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.chooseStart = False
        self.immediately = False
        self.instruction = {
            "Instructions": "It looks like your <replace> election has <blank> questions and starts <date>: Would you like to add another question?",
            "type": "MultipleChoice",
            "1": "Yes, let's add a multiple choice",
            "2": "Yes, let's add a ranked choice",
            "3": "Yes, let's add multiple choice with write in option",
            "4": "I'm finished"}

    def enter(self, conn, elec, user):
        ret = self.instruction.copy()
        ret["Instructions"].replace("<replace>", elec.name)
        ret["Instructions"].replace("<blank>", "%d" % len(elec.voteActions))
        if elec.date != None:
            ret["Instructions"].replace("<date>", elec.date.strftime("on %Y-%m-%d %H:%M"))
        else:
            ret["Instructions"].replace("<date>", elec.date.strftime("immediately"))
        self.conn = conn
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