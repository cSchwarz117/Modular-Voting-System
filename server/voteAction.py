class voteAction(server_state):
    def __init__(self):
        self.multipleChoice = False
        self.rank = False
        self.fill = False
        self.options = []
        self.blank = None
        self.instructions = None