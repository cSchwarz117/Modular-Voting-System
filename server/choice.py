class choice(object):
    def __init__(self):
        ans = None

    def clone(self):
        c = choice()
        c.ans = self.ans
        return c