from states.server_state import server_state
from states.createMultipleChoice import createMultipleChoice
from states.createRankedChoice import createRankedChoice
from states.createChoiceW import createChoiceW
import states
import states.createMultipleChoice
from election import election
import sys

sys.path.append("..")
from server_data import server_data
import pickle


class createQuestion(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.createMultipleChoice = False
        self.createRankedChoice = False
        self.createChoiceW = False
        self.instruction = {
            "Instructions": "It looks like your <replace> election has <blank> questions and starts <date>: Would you like to add another question?",
            "type": "MultipleChoice",
            "1": "Yes, let's add a multiple choice",
            "2": "Yes, let's add a ranked choice",
            "3": "Yes, let's add multiple choice with write in option",
            "4": "I'm finished"}

    def enter(self, data, conn, elec, user):
        ret = self.instruction.copy()
        numQs = len(elec.voteActions)
        numQsStr = "%d"%numQs

        ret["Instructions"] = ret["Instructions"].replace("<replace>", elec.name)
        ret["Instructions"] = ret["Instructions"].replace("<blank>", numQsStr)
        if elec.start is None:
            start = "Immediately"
        else:
            start = elec.date.strftime("on %Y-%m-%d %H:%M")
        ret["Instructions"] = ret["Instructions"].replace("<date>", start)
        self.conn = conn
        out = pickle.dumps(ret)
        self.conn.sendall(out)
        return None

    def process(self, data, elec, user):
        dict = data
        ans = dict["ans"]
        if ans == "2":
            self.createRankedChoice = True
        if ans == "1":
            self.createMultipleChoice = True
        if ans == "3":
            self.createChoiceW = True
        return (elec, user)

    def execute(self, data, election, user):
        if self.createRankedChoice:
            return createRankedChoice()
        if self.createMultipleChoice:
            return states.createMultipleChoice.createMultipleChoice()
        if self.createChoiceW:
            return createChoiceW()
        return None

    def exit(self, data, election, user):
        return None