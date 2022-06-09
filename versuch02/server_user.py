import json
from paket import Paket

class User:
    def __init__(self, name, clientsocket, server):
        super().__init__()
        self.online = True
        self.name = name
        self.user_id = None
        self.number = None
        self.clientsocket = clientsocket
        self.server = server

    def incmsg(self):
        while self.online:
            try:
                msg = self.clientsocket.recv(1024)
                msg = msg.decode()
                self.jsondebug(msg)
                self.denigma(msg)

            except ConnectionResetError:
                for idx, client in enumerate(self.server.userlist):
                    if client.clientsocket == self.clientsocket:
                        self.server.userlist.pop(idx)
                        self.server.get_userlist()
                        client.shutdown()

    def denigma(self, msg):
        paket = json.loads(msg)
        if paket['typ'] == 'msg':
            self.server.broadcast(msg)
        if paket['typ'] == 'name':
            self.name = paket['data']
            self.server.privatcast(self.clientsocket, msg)
        if paket['typ'] == 'instantreply':
            pass
        if paket['typ'] == 'login':
            self.login_procedure(paket)

    def login_procedure(self, paket):
        name = paket['data'][0]
        passwort = paket['data'][1]
        user_name, user_id, msg = self.server.db_c.check_login(name, passwort)
        ans = Paket('login', user_name, user_id, msg)
        ans = json.dumps(ans.__dict__)
        self.server.privatcast(self.clientsocket, ans)

    def get_user_number(self):
        for idx, client in enumerate(self.server.userlist):
            if client.clientsocket == self.clientsocket:
                self.number = idx

    def usernames(self):
        names = []
        for user in self.server.userlist:
            names.append(user.name)
        return names

    def jsondebug(self, msg):
        paket = json.loads(msg)
        typ = paket['typ']
        sender = paket['sender']
        user_id = paket['user_id']
        data = paket['data']
        print(f'[{typ}] [{sender}] [{user_id}]: [{data}]')

    def shutdown(self):
        self.clientsocket.close()
        self.online = False
