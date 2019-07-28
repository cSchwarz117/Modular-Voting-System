from states.server_state import server_state

class election(server_state):
    def __init__(self):
        self.start = None
        self.name = None
        self.voteActions = []
        self.end = None
        self.votes = []


    def getResults(self, index):
        va = self.voteActions[index]
        if va.multipleChoice:
            return self.getResultMult(va, index)

    def getResultMult(self, voteAct, index):
        dict = {}
        instruction = voteAct.instructions

        votes = []
        for i in range(len(voteAct.options)):
            votes.append(0)


        for i in range(len(self.votes)):
            c = int(self.votes[i].votes[index].ans)
            votes[c] += 1

        results = []
        for i in range(len(voteAct.options)):
            s = "%d" % votes[i]
            results.append(voteAct.options[i] + ": " + s)

        for i in range(len(results)):
            instruction += "\n" + results[i]

        return instruction


