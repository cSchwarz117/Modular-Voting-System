from states.server_state import server_state
import states
import states.login_state
import sys
import choice
import states.voterOptions
sys.path.append("..")

from messageInstance import instance

class vote_in_elec(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.choice = False
        self.ballotComplete = False

    def enter(self, data, conn, election, user):
        q = self.getVote(election, 0)
        instance.send(q)
        return None

    def getVote(self, election, index):
        q = election.voteActions[index].get_vote()
        if election.voteActions[index].multipleChoice:
            self.choice = True
        return q

    def process(self, data, election, user):

        if self.choice:
            c = choice.choice()
            c.ans = data["ans"]
            user.ballot.add_vote(c)
            self.choice = False

        if len(user.ballot.votes) < len(election.voteActions):
            q = self.getVote(election, len(user.ballot.votes))
            instance.send(q)
        else:
            self.ballotComplete = True

        return election, user

    def execute(self, data, election, user):
        if self.ballotComplete:
            election.votes.append(user.ballot)
            return states.voterOptions.voterOptions()
        else:
            return None

    def exit(self, data, election, user):
        return None