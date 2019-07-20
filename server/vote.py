class vote (object):
    def __init__(self):
        #a list of rankings and choices
        self.votes = []
        self.userName = None
        return None

    def add_vote(self, v):
        self.votes.append(v)
