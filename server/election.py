from states.server_state import server_state

class election(server_state):
    def __init__(self):
        self.start = None
        self.name = None
        self.voteActions = []
        self.end = None
        self.votes = []
