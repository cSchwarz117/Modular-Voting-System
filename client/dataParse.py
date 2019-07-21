class parser():

    def typeCheck(self, data):
        if data['type'] == 'MultipleChoice':
            return self.choice(data)

        if data['type'] == 'date':
            return self.date(data)
        if data['type'] == 'char25':
            return self.char25(data)
        if data['type'] == 'PasswordFail':
            return self.pFail(data)
        if data['type'] == 'UsernameFail':
            return self.uFail(data)
        else:
            print('Data Type error')
            return

        return

    def choice(self, data):
        del data['type']
        print(data['Instructions'])
        del data['Instructions']
        for key, val in data.items():
            print(key, ": ", val)
        select = input()
        cred = {"ans": select}
        return cred

    def date(self, data):
        print(data['Instructions'])
        select = input()
        ans = {"ans": select}
        return ans

    def char25(self, data):
        print(data['Instructions'])
        select = input()
        ans = {"ans": select}
        return ans

    def pFail(self, data):
        print(data['Instructions'])
        return False

    def uFail(self, data):
        print(data['Instructions'])
        return False