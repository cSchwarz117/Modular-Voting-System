from messanger import message
class parser(message):

    def typeCheck(self, data):
        if data['type'] == 'MultipleChoice':
            self.choice(data)
        if data['type'] == 'date':
            self.date()
        if data['type'] == 'char25':
            self.char25()
        if data['type'] == 'PasswordFail':
            self.pFail()
        if data['type'] == 'UsernameFail':
            self.uFail()
        else:
            print('Data Type error')
            return

        return


    def choice(self, data):

        print('here')

    def date(self, data):
        print('here')

    def char25(self, data):
        print('here')

    def pFail(self, data):
        print('here')

    def uFail(self, data):
        print('here')