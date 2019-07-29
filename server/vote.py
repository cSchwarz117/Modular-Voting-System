class vote (object):
    def __init__(self):
        #a list of rankings and choices
        self.votes = []
        self.userName = None
        self.curIndex = 0
        return None

    def add_vote(self, v):
        self.votes.append(v)

    def clone(self):
        v = vote()
        v.userName = self.userName
        v.curIndex = self.curIndex
        v.votes = []
        for i in range (len(self.votes)):
            v.votes.append(self.votes[i].clone())
        return v

