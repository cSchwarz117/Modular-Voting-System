from states.server_state import server_state
class reviewBallot(server_state):
    def __init__(self):
       return None

    def __init__(self):
        self.ret = {}
        self.conn = None

    def enter(self, data, conn, election, user):
        q = self.getVote(election, 0)
        instance.send(q)
        return None

    def getVote(self, election, index):
        q = election.voteActions[index].get_vote()
        if election.voteActions[index].multipleChoice:
            self.choice = True
        return q