from states.server_state import server_state
import states
import states.login_state
from server_data import server_data
from states.createElection import createElection
import sys
sys.path.append("..")
import pickle
import states
import states.vote_in_elec
import states.reviewBallot
import states.login_state
import states.editBallot
import vote

from messageInstance import instance
class voterOptions(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.voterOpts = {
            "Instructions": "I see you are a voter! Welcome! Please choose from the following options",
            "type": "MultipleChoice",
            "1": "Vote in election",
            "2": "Review Ballot",
            "3": "Edit Ballot",
            "4": "Log Off"}

    def enter(self, data, conn, election, user):
        instance.send(self.voterOpts)
        self.vote_in_election = False
        self.review_ballot = False
        self.edit_ballot = False
        self.logOff = False
        return None

    def process(self, data, election, user):
        dict = data
        ans = dict["ans"]
        if ans == "1":
            user.ballot = vote.vote()
            self.vote_in_election = True
        if ans == "2":
            self.review_ballot = True
        if ans == "3":
            self.edit_ballot = True
        if ans == "4":
            logoff = {
                "Instructions": "Logged off",
                "type": "logoff"}
            instance.send(logoff)
            self.logOff = True

        return election, user

    def execute(self, data, election, user):
        if self.vote_in_election:
            return states.vote_in_elec.vote_in_elec()
        if self.logOff:
            return states.login_state.login_state()
        if self.review_ballot:
            return states.reviewBallot.reviewBallot()
        if self.edit_ballot:
            return states.editBallot.editBallot()
        else:
            return None

    def exit(self, data, election, user):
        return None