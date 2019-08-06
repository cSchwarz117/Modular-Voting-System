class parser():

    def typeCheck(self, data):
        if data['type'] == 'MultipleChoice':
            return self.choice(data)
        if data['type'] == 'RankedChoice':
            return self.rank(data)

        if data['type'] == 'date':
            return self.date(data)
        if data['type'] == 'char25':
            return self.char25(data)
        if data['type'] == 'PasswordFail':
            return self.pFail(data)
        if data['type'] == 'UsernameFail':
            return self.uFail(data)
        if data['type'] == 'StrArray':
            return self.StrArray(data)
        if data['type'] == 'logoff':
            print(data['Instructions'])
            return True
        else:
            print('Data Type error')
            return


    def rank(self, data):
        del data['type']
        print(data['Instructions'])
        del data['Instructions']
        for key, val in data.items():
            print(key, ": ", val)
        print("Ranked Choice voting: Of these options, which is your top choice?")
        for key, val in data.items():
            print(key, ": ", val)
        select = input()
        ret = select
        del data[select]
        index = 0
        while len(data) > 0:
            index += 1
            print("Ranked Choice voting: Of these remaining options, which is your top choice?")
            for key, val in data.items():
                print(key, ": ", val)
            select = input()
            ret += "," + select
            del data[select]

        return {"ans": ret}




    def StrArray(self, data):
        print(data['Instructions'])
        x = input('How many options do you want?')
        cred = {}
        for i in range(int(x)):
            cred[i] = input("Option: ")
        return cred

    def date(self, data):
        return None


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