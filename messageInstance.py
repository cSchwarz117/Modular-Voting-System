from messenger import message
class instance():
    global Messenger
    def __init__(self, sock):
        global Messenger
        Messenger = message()
        Messenger.sock = sock
        return None

    @staticmethod
    def send(data):
        global Messenger
        Messenger.send(data)

    @staticmethod
    def rec():
        global Messenger
        return Messenger.recv()
