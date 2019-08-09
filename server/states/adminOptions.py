from states.server_state import server_state
import states
import states.login_state
import states.viewResults
import states.saveElection
import states.loadElection
import states.saveVoterRolls
import states.loadVoterRolls
import states.addVoter
from states.createElection import createElection
import sys
sys.path.append("..")

from messageInstance import instance
class adminOptions(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.adminOpts = {
            "Instructions": "I see you are an admin! Welcome! Please choose from the following options",
            "type": "MultipleChoice",
            "1": "Create Election",
            "2": "Edit Election",
            "3": "View Results",
            "4": "Add Voter",
            "5": "Log Off",
            "6": "Save Voter Rolls",
            "7": "Save Election",
            "8": "Load Voter Roles",
            "9": "Load Election",}

    def enter(self, data, conn, election, user):
        instance.send(self.adminOpts)
        self.create_election = False
        self.editElection = False
        self.viewResults = False
        self.addVoter = False
        self.logOff = False
        self.saveVoters = False
        self.saveElection = False
        self.loadVoters = False
        self.loadElection = False
        return None

    def process(self, data, election, user):
        dict = data
        ans = dict["ans"]
        if ans == "1":
            self.create_election = True
        if ans == "2":
            self.editElection = True
        if ans == "3":
            self.viewResults = True
        if ans == "4":
            self.addVoter = True
        if ans == "5":
            logoff = {
                "Instructions": "Logged off",
                "type": "logoff"}
            instance.send(logoff)
            self.logOff = True
        if ans =="6":
            self.saveVoters = True
        if ans == "7":
            self.saveElection = True
        if ans == "8":
            self.loadVoters = True
        if ans == "9":
            self.loadElection = True

        return (election, user)

    def execute(self, data, election, user):
        if self.create_election:
            return createElection()
        if self.logOff:
            return states.login_state.login_state()
        if self.viewResults:
            return states.viewResults.viewResults()
        if self.saveVoters:
            return states.saveVoterRolls.saveVoterRolls()
        if self.saveElection:
            return states.saveElection.saveElection()
        if self.loadVoters:
            return states.loadVoterRolls.loadVoterRolls()
        if self.loadElection:
            return states.loadElection.loadElection()
        if self.addVoter:
            return states.addVoter.addVoter()
        else:
            return None

    def exit(self, data, election, user):
        return None