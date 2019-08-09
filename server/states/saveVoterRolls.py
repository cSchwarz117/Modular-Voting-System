from states.server_state import server_state
import states
import states.adminOptions
import sys
import os
sys.path.append("..")
from server_data import server_data
import pickle

from messageInstance import instance


class saveVoterRolls(server_state):

    def __init__(self):
        return None

    def enter(self, data, conn, election, user):
        ret = {}
        ret["Instructions"] = "What would you like to save the voter roll file as?: "
        ret["type"] = "char25"

        instance.send(ret)
        return None

    def process(self, data, elec, user):
        z = {}
        z["users"] = server_data.get_users()
        z["voters"] = server_data.get_voters()
        f = data["ans"]
        cwd = os.getcwd()
        f = cwd + "\\" + f
        afile = open(f, 'ab')
        pickle.dump(z, afile)
        afile.close()
        return elec, user

    def execute(self, data, election, user):
        return states.adminOptions.adminOptions()

    def exit(self, data, election, user):
        return None