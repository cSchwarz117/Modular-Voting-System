from states.server_state import server_state
import states
import states.login_state
import sys
import choice
import ranking
import writeIn
import states.voterOptions
sys.path.append("..")

from messageInstance import instance

class vote_in_elec(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.choice = False
        self.rank = False
        self.voteOrWriteIn = False
        self.ballotComplete = False
        self.writeIn = False

    def enter(self, data, conn, election, user):
        q = self.getVote(election, 0)
        instance.send(q)
        return None

    def getVote(self, election, index):
        q = election.voteActions[index].get_vote()
        if election.voteActions[index].multipleChoice:
            self.choice = True
        if election.voteActions[index].rank:
            self.rank = True
        if election.voteActions[index].choiceAndWriteIn:
            self.voteOrWriteIn = True

        return q

    def process(self, data, election, user):

        if self.choice:
            c = choice.choice()
            c.ans = data["ans"]
            user.ballot.add_vote(c)
            self.choice = False

        if self.rank:
            r = ranking.ranking()
            r.rankings = data["ans"]
            user.ballot.add_vote(r)
            self.rank = False

        if self.writeIn:
            w = writeIn.writeIn()
            w.ans = data["ans"]
            user.ballot.add_vote(w)
            self.writeIn = False

        if self.voteOrWriteIn:
            self.voteOrWriteIn = False
            c = int(data["ans"])
            index = len(user.ballot.votes)
            if c == len(election.voteActions[index].options):
                self.writeIn = True
                write = {
                    "Instructions": "Please write in your choice: ",
                    "type": "char25",
                }
                instance.send(write)
                return election, user
            else:
                c = choice.choice()
                c.ans = data["ans"]
                user.ballot.add_vote(c)

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