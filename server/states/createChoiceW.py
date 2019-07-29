from states.server_state import server_state

import sys
sys.path.append("..")
from voteAction import voteAction

import states
import states.createQuestion
from messageInstance import instance
class createChoiceW(server_state):
    def __init__(self):
        self.ret = {}
        self.conn = None
        self.dictSize = 0

        self.instruction = {
            "Instructions": "Create your multiple choice question with write in option. What is the question?",
            "type": "char25",}

    def enter(self, data, conn, election, user):
        self.vAction = voteAction()
        self.vAction.choiceAndWriteIn = True
        instance.send(self.instruction)
        self.done = False
        return None

    def process(self, data, elec, user):
        q = data

        if self.vAction.instructions is None:
            self.vAction.instructions = q["ans"]
            ins = {
                "Instructions": "Your Question: \n <replace> \n Give non-write in options for this multiple choice question.",
                "type": "StrArray", }
            ins["Instructions"] = ins["Instructions"].replace("<replace>", self.vAction.instructions)
            instance.send(ins)
            return elec, user
        else:
            size = len(q)
            for i in range(size):
                self.vAction.options.append(q[i])
            elec.voteActions.append(self.vAction)
            self.done = True

        return elec, user

    def execute(self, data, election, user):
        if self.vAction.instructions is not None:
            if self.done:
                return states.createQuestion.createQuestion()
        return None

    def exit(self, data, election, user):
        return None