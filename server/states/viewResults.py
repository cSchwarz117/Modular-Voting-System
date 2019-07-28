from states.server_state import server_state
from election import election
from states.createDate import createDate
import states
import states.adminOptions
import sys

sys.path.append("..")
from server_data import server_data
import pickle

from messageInstance import instance
class viewResults(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.index = 0
        self.done = False

    def enter(self, data, conn, election, user):
        instructions = election.getResults(self.index)
        ret = {}
        ret["Instructions"] = instructions
        ret["type"] = "MultipleChoice"
        ret["1"] = "Next"
        ret["2"] = "Done"

        instance.send(ret)
        self.index += 1
        return None

    def process(self, data, elec, user):

        if self.index < len(elec.voteActions) and data["ans"] == 1:
            instructions = election.getResults(self.index)
            ret = {}
            ret["Instructions"] = instructions
            ret["type"] = "MultipleChoice"
            ret["1"] = "Next"
            ret["2"] = "Done"
            instance.send(ret)
            self.index += 1
        else:
            self.done = True
        return elec, user

    def execute(self, data, election, user):
        if self.done:
            return states.adminOptions.adminOptions()
        return None

    def exit(self, data, election, user):
        return None