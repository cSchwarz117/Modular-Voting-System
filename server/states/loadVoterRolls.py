from states.server_state import server_state
from election import election
from states.createDate import createDate
import states
import states.adminOptions
import sys

sys.path.append("..")
from server_data import server_data
import pickle
import os
from messageInstance import instance
class loadVoterRolls(server_state):

    def __init__(self):
        return None

    def enter(self, data, conn, election, user):
        ret = {}
        ret["Instructions"] = "What is the named of the voter roll file?: "
        ret["type"] = "char25"

        instance.send(ret)
        return None

    def process(self, data, elec, user):

        f = data["ans"]
        cwd = os.getcwd()
        f = cwd + "\\" + f
        file2 = open(f, 'rb')
        new_d = pickle.load(file2)
        file2.close()
        users = new_d["users"]
        voters = new_d["voters"]
        server_data.loadVoterRolls(users, voters)
        print(server_data.get_users())
        return elec, user

    def execute(self, data, election, user):
        return states.adminOptions.adminOptions()

    def exit(self, data, election, user):
        return None