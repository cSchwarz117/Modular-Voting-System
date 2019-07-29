
class voteAction(object):
    def __init__(self):
        self.multipleChoice = False
        self.choiceAndWriteIn = False
        self.rank = False
        self.fill = False
        self.options = []
        self.blank = None
        self.instructions = None

    def get_vote(self):
        if self.multipleChoice:
            dict = {}
            dict["Instructions"] = self.instructions
            for i in range(len(self.options)):
                dict["%d" % i] = self.options[i]

            dict["type"] = "MultipleChoice"
            return dict

        if self.choiceAndWriteIn:
            dict = {}
            dict["Instructions"] = self.instructions
            for i in range(len(self.options)):
                dict["%d" % i] = self.options[i]

            dict["type"] = "MultipleChoice"
            dict["%d" % len(self.options)] = "Write in"
            return dict

        if self.rank:
            dict = {}
            dict["Instructions"] = self.instructions
            for i in range(len(self.options)):
                dict["%d" % i] = self.options[i]

            dict["type"] = "RankedChoice"
            return dict
