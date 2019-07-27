class vote (object):
    def __init__(self):
        #a list of rankings and choices
        self.votes = []
        self.userName = None
        self.curIndex = 0
        return None

    def add_vote(self, v):
        self.votes.append(v)
