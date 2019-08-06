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
        if va.choiceAndWriteIn:
            return self.getResultMultOrWriteIn(va, index)

    def getResultMultOrWriteIn(self, voteAct, index):
        instruction = voteAct.instructions

        votes = []
        for i in range(len(voteAct.options)):
            votes.append(0)

        writeIns = {}
        for i in range(len(self.votes)):
            t = self.votes[i].votes[index].ans
            if t.isdigit():
                c = int(t)
                votes[c] += 1
            else:
                found = False
                for key, value in writeIns.items():
                    if key == t:
                        writeIns[key] += 1
                        found = True
                        break

                if not found:
                    writeIns[t] = 1

        results = []
        for i in range(len(voteAct.options)):
            s = "%d" % votes[i]
            results.append(voteAct.options[i] + ": " + s)

        for key, value in writeIns.items():
            s = "%d" % value
            results.append(key + ": " + s)

        for i in range(len(results)):
            instruction += "\n" + results[i]

        return instruction


    def getResultMult(self, voteAct, index):
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

    def getResultRank(self, voteAct, index):
        instruction = voteAct.instructions

        voters = []
        for i in range(len(self.votes)):
            voters.append(self.votes[i].clone())

        highestIndex, highestScore = self.getHighest(voteAct, index, voters)

        while highestScore < .5:
            highestIndex, highestScore = self.getHighest(voteAct, index, voters)
            lowestIndex = self.getLowest(voteAct, index, voters)
            self.removeLowest(lowestIndex, index, voters)

        return instruction + "\n" + voteAct.options[highestIndex]

    def removeLowest(self, lowestIndex, index, voters):
        for i in range(len(voters)):
            s = "%d" % lowestIndex
            voters[i].votes[index].ranking = voters[i].votes[index].ranking.replace(s, "")
            voters[i].votes[index].ranking = voters[i].votes[index].ranking.replace(" ", "")
            voters[i].votes[index].ranking = voters[i].votes[index].ranking.replace(",,", ",")
        return voters

    def getLowest(self, voteAct, index):
        votes = []
        for i in range(len(voteAct.options)):
            votes.append(0)

        for i in range(len(self.votes)):
            ranking = self.votes[i].votes[index].rankings
            r = ranking.split(",")
            best = int(r[0])
            votes[best] += 1

        lowestIndex = 0
        lowestScore = votes[lowestIndex]
        for i in range(len(voteAct.options)):
            if votes[i] < lowestScore:
                lowestScore = votes[i]
                lowestIndex = i

        return lowestIndex

    def getHighest(self, voteAct, index, voters):
        votes = []
        for i in range(len(voteAct.options)):
            votes.append(0)

        for i in range(len(voters)):
            ranking = voters.votes[index].rankings
            r = ranking.split(",")
            best = int(r[0])
            votes[best] += 1

        highestIndex = 0
        highestScore = votes[highestIndex]
        for i in range(len(voteAct.options)):
            if votes[i] > highestIndex:
                highestScore = votes[i]
                highestIndex = i

        return highestIndex, float(highestScore)/float(len(voters))



