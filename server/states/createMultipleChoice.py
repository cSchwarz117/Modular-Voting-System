from states.server_state import server_state

import sys
sys.path.append("..")
from voteAction import voteAction

import states
import states.createQuestion
from messageInstance import instance
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
        instance.send(self.instruction)
       # self.conn = conn
       # out = pickle.dumps(self.instruction)
       # conn.sendall(out)
        return None

    def process(self, data, elec, user):
        q = data

        if self.vAction.instructions is None:
            self.vAction.instructions = q["ans"]
            ins = {
                "Instructions": "Your Question: \n <replace> \n Give at least two options for this multiple choice question.",
                "type": "StrArray", }
            ins["Instructions"] = ins["Instructions"].replace("<replace>", self.vAction.instructions)
            instance.send(ins)
            #out = pickle.dumps(ins)
            #self.conn.sendall(out)
            return elec, user
        else:
            if len(q) < 2:
                ins = {
                    "Instructions": "Not enough info! Required: at least two options!",
                    "type": "StrArray", }
                instance.send(ins)
                #out = pickle.dumps(ins)
                #self.conn.sendall(out)
                return elec, user
            size = len(q)
            for i in range(size):
                self.vAction.options.append(q[i])

            elec.voteActions.append(self.vAction)

        return elec, user

    def execute(self, data, election, user):
        if self.vAction.instructions is not None:
            if len(self.vAction.options) >= 2:
                return states.createQuestion.createQuestion()
        return None

    def exit(self, data, election, user):
        return None