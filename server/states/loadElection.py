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
import os
class loadElection(server_state):

    def __init__(self):
        return None
    
    def enter(self, data, conn, election, user):
        ret = {}
        ret["Instructions"] = "What is the name of the election file?: "
        ret["type"] = "char25"

        instance.send(ret)
        return None

    def process(self, data, elec, user):

        f = data["ans"]
        cwd = os.getcwd()
        f = cwd + f
        file2 = open(f)
        new_d = pickle.load(file2)
        file2.close()
        elec.setVotes(new_d["votes"])
        elec.setVoteActions(new_d["voteActions"])
        server_data.set_user_objs(new_d["userObjs"])

        return elec, user

    def execute(self, data, election, user):
        return states.adminOptions.adminOptions()

    def exit(self, data, election, user):
        return None