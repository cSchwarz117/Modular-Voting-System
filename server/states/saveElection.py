from states.server_state import server_state
import states
import states.adminOptions
import sys

sys.path.append("..")
from server_data import server_data
import pickle
import os

from messageInstance import instance


class saveElection(server_state):

    def __init__(self):
        return None

    def enter(self, data, conn, election, user):
        ret = {}
        ret["Instructions"] = "What would you like to save the election file as?: "
        ret["type"] = "char25"

        instance.send(ret)
        return None

    def process(self, data, elec, user):
        z = {}
        z["votes"] = elec.getVotes()
        z["voteActions"] = elec.getVoteActions()
        z["userObjs"] = server_data.get_user_objs()
        f = data["ans"]
        cwd = os.getcwd()
        f = cwd + f
        afile = open(f)
        pickle.dump(z, afile)
        afile.close()
        return elec, user

    def execute(self, data, election, user):
        return states.adminOptions.adminOptions()

    def exit(self, data, election, user):
        return None