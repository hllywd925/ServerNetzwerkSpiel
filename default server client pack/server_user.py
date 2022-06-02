class User:
    def __init__(self, name, clientsocket, server):
        super().__init__()
        self.online = True
        self.name = name
        self.number = None
        self.clientsocket = clientsocket
        self.server = server

        self.sep = '#SEP#'
        self.typ_message = 'MSG'
        self.typ_namechange = 'NAME'
        self.typ_user = 'UL'

    def incmsg(self):
        while self.online:
            try:
                print('[SERVER]: Warte auf Nachricht.')
                msg = self.clientsocket.recv(1024)
                msg = msg.decode()
                self.enigma(msg)
                #self.server.userlist_update()

            except ConnectionResetError:
                for idx, client in enumerate(self.server.userlist):
                    if client.clientsocket == self.clientsocket:
                        self.server.userlist.pop(idx)
                        self.server.get_userlist()
                        client.shutdown()

    def get_user_number(self):
        for idx, client in enumerate(self.server.userlist):
            if client.clientsocket == self.clientsocket:
                self.number = idx

    def newname(self, name):
        self.name = name

    def enigma(self, inc):
        typ, msg = inc.split(self.sep)
        if typ == self.typ_message:
            print(f'{self.name}: {msg}')
            bc_msg = f'{self.typ_message}{self.sep}{self.name}: {msg}'
            self.server.broadcast(bc_msg)
        if typ == self.typ_namechange:
            oldname = self.name
            self.name = msg
            bc_msg = f'{self.typ_message}{self.sep}{oldname} heißt jetzt {self.name}'
            self.server.broadcast(bc_msg)

    def shutdown(self):
        self.clientsocket.close()
        self.online = False
