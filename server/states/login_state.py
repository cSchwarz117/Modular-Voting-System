from states.server_state import server_state
import states
import states.adminOptions
import states.voterOptions
from server_data import server_data

class login_state(server_state):

    def __init__(self):
        self.ret = {}
        self.conn = None
        self.loggedIn = False

    def enter(self, data, conn, election, user):
        self.conn = conn
        self.loggedIn = False
        self.admin = False
        self.voter = False
        self.wrongUser = False
        self.wrongPassword = False
        return None

    def process(self, data, election, user):
        dict = data
        pswd = dict["password"]
        usr = dict["username"]
        users = server_data.get_users()
        userObjs = server_data.get_user_objs()
        if usr in users.keys():
            if pswd == users[usr]:
                if usr in server_data.get_admins():
                    user = userObjs[usr]
                    self.admin = True
                else:
                    user = userObjs[usr]
                    self.voter = True
            else:
                ret = server_data.get_incorrectpass()
        else:
            ret = server_data.get_incorrectuser()

        return election, user

    def execute(self, data, election, user):
        if self.admin:
            return states.adminOptions.adminOptions()
        if self.voter:
            return states.voterOptions.voterOptions()
        else:
            return None

    def exit(self, data, election, user):
        return None