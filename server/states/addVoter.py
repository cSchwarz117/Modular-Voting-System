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
class addVoter(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.index = 0
        self.done = False

    def enter(self, data, conn, election, user):
        ret = {}
        ret["Instructions"] = "Pick a username: "
        ret["type"] = "char25"

        instance.send(ret)
        self.userPicked = False
        self.user = ""
        return None

    def process(self, data, elec, user):

        if not self.userPicked:
            self.user = data["ans"]
            ret = {}
            ret["Instructions"] = "Pick a password: "
            ret["type"] = "char25"
            instance.send(ret)
            self.userPicked = True
        else:
            self.password = data["ans"]
            server_data.add_user(self.user, self.password)
            self.done = True
        return elec, user

    def execute(self, data, election, user):
        if self.done:
            return states.adminOptions.adminOptions()
        return None

    def exit(self, data, election, user):
        return None