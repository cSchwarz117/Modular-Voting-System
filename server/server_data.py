import sys
import user
class server_data(object):
    global users
    global admins
    global voters
    global adminopts
    global voteropts
    global incorrectuser
    global incorrectpass
    global once
    once = None
    def __init__(self):
        global once
        if once is not None:
            return None
        once = 1
        global userObjs
        userObjs = {
            "Jane": user.user(),
            "Joe": user.user(),
            "Fred": user.user(),
            "Anne": user.user()
        }
        global users
        users = {
            "Jane": "123",
            "Joe": "abc",
            "Fred": "spacepirate",
            "Anne": "netflix"
        }
        global admins
        admins = []
        global voters
        voters = []

        admins.append("Anne")
        voters.append("Jane")
        voters.append("Fred")
        voters.append("Joe")

        global adminopts
        adminopts = {
            "Instructions": "I see you are an admin! Welcome! Please choose from the following options",
            "type": "MultipleChoice",
            "1": "Create Election",
            "2": "Edit Election",
            "3": "View Results"
        }

        global voteropts
        voteropts = {
            "Instructions": "I see you are a voter, please choose from the following options",
            "type": "MultipleChoice",
            "1": "Candidate A",
            "2": "Candidate B",
        }

        global incorrectpass
        incorrectpass = {
            "Instructions": "Password Incorrect",
            "type": "PasswordFail",
        }

        global incorrectuser
        incorrectuser = {
            "Instructions": "Username Incorrect",
            "type": "UsernameFail",}
        return None

    @staticmethod
    def loadVoterRolls(_users, _voters):
        global users
        global voters
        global userObjs
        users = _users
        voters = _voters
        for u in users:
            if not u in userObjs:
                userObjs[u] = user.user()

    @staticmethod
    def getVoterRolls():
        global users
        global voters
        return users, voters

    @staticmethod
    def add_user(u, password):
        global users
        global voters
        global userObjs
        userObjs[u] = user.user()
        users[u] = password
        voters.append(u)

    @staticmethod
    def get_users():
        global users
        return users

    @staticmethod
    def set_user_objs(objs):
        global userObjs
        userObjs = objs

    @staticmethod
    def get_user_objs():
        global userObjs
        return userObjs

    @staticmethod
    def get_admins():
        global admins
        return admins

    @staticmethod
    def get_voters():
        global voters
        return voters


    @staticmethod
    def get_incorrectpass():
        global incorrectpass
        return incorrectpass

    @staticmethod
    def get_incorrectuser():
        global incorrectuser
        return incorrectuser

    @staticmethod
    def get_voteropts():
        global voteropts
        return voteropts

    @staticmethod
    def get_adminopts():
        global adminopts
        return adminopts

