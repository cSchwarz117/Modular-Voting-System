from server_state import server_state
from voteAction import voteAction
from createQuestion import createQuestion
import pickle
class createMultipleChoice(server_state):
    def __init__(self):
        self.ret = {}
        self.conn = None
        self.dictSize = 0

        self.instruction = {
            "Instructions": "Create your multiple choice question.",
            "type": "StrArray",}

    def enter(self, conn, elec, user):
        self.conn = conn
        out = pickle.dumps(self.instruction)
        conn.sendall(out)
        return None

    def process(self, data, elec, user):
        dict = pickle.loads(data)
        self.dictSize = len(dict)
        if self.dictSize < 3:
            ins = {
            "Instructions": "Not enough info! Required: Instructions and at least two options! \nCreate your multiple choice question.",
            "type": "StrArray",}
            out = pickle.dumps(ins)
            self.conn.sendall(out)
            return (elec, user)

        vAction = voteAction()
        vAction.multipleChoice = True
        vAction.instructions = dict["0"]
        for i in range(1, self.dictSize):
            vAction.options.append(dict["%d"%i])
        elec.voteActions.append(vAction)
        return (elec, user)

    def execute(self, data, election, user):
        if self.dictSize < 3:
            return None
        return createQuestion()

    def exit(self, data, election, user):
        return None