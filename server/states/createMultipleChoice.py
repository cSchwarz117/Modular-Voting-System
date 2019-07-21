from states.server_state import server_state
from voteAction import voteAction
import sys
sys.path.append("..")
import states
#from states.createQuestion import createQuestion
import pickle
class createMultipleChoice(server_state):
    def __init__(self):
        self.ret = {}
        self.conn = None
        self.dictSize = 0

        self.instruction = {
            "Instructions": "Create your multiple choice question. What is the question?",
            "type": "char25",}

    def enter(self, data, conn, election, user):
        self.vAction = voteAction()
        self.vAction.multipleChoice = True
        self.conn = conn
        out = pickle.dumps(self.instruction)
        conn.sendall(out)
        return None

    def process(self, data, elec, user):
        q = pickle.loads(data)

        if self.vAction.instructions is None:
            self.vAction.instructions = q["ans"]
            ins = {
                "Instructions": "Your Question: \n <replace> \n Give at least two options for this multiple choice question.",
                "type": "StrArray", }
            ins["Instructions"] = ins["Instructions"].replace("<replace>", self.vAction.instructions)
            out = pickle.dumps(ins)
            self.conn.sendall(out)
            return elec, user
        else:
            if len(q) < 2:
                ins = {
                    "Instructions": "Not enough info! Required: at least two options!",
                    "type": "StrArray", }
                out = pickle.dumps(ins)
                self.conn.sendall(out)
                return elec, user
            size = len(q)
            for i in range(size):
                self.vAction.options.append(q["%d" % i])

            elec.voteActions.append(self.vAction)

        return elec, user

    def execute(self, data, election, user):
        if self.vAction.instructions is not None:
            if len(self.vAction.options) >= 2:
                return states.createQuestion()
        return None

    def exit(self, data, election, user):
        return None