from states.server_state import server_state

import states
import states.voterOptions
from messageInstance import instance
class reviewBallot(server_state):
    def __init__(self):
       return None

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.finished = False
        self.currentIndex = 0
        self.genericInstructions = {
            "Instructions": "Ballot Review: \n <review>",
            "type": "MultipleChoice",
            "1": "Next",
            "2": "I'm finished"
        }

    def enter(self, data, conn, election, user):
        if len(election.voteActions) > self.currentIndex and len(user.ballot.votes) > self.currentIndex:
            q = election.voteActions[self.currentIndex].instructions
            ans = user.ballot.votes[self.currentIndex].ans
            if ans.isdigit():
                i = int(user.ballot.votes[self.currentIndex].ans)
                ans = election.voteActions[self.currentIndex].options[i]
            q += "\n Your Answer: " + ans
            ret = self.genericInstructions.copy()
            ret["Instructions"] = ret["Instructions"].replace("<review>", q)
            instance.send(ret)
            self.currentIndex += 1
        return None

    def process(self, data, elec, user):
        ans = data["ans"]


        if ans == "1" and len(elec.voteActions) > self.currentIndex and len(user.ballot.votes) > self.currentIndex:
            q = elec.voteActions[self.currentIndex].instructions
            ans = user.ballot.votes[self.currentIndex].ans
            if ans.isdigit():
                i = int(user.ballot.votes[self.currentIndex].ans)
                ans = elec.voteActions[self.currentIndex].options[i]
            q += "\n Your Answer: " + ans
            ret = self.genericInstructions.copy()
            ret["Instructions"] = ret["Instructions"].replace("<review>", q)
            instance.send(ret)
            self.currentIndex += 1
        else:
            self.finished = True
        return elec, user

    def execute(self, data, election, user):
        if self.finished:
            return states.voterOptions.voterOptions()
        return None

