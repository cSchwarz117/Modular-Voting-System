class ranking(object):
    def __init__(self):
        rankings = []

    def clone(self):
        r = ranking()
        r.rankings = self.rankings
        return r
