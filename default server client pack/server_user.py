class User:
    def __init__(self, name, clientsocket, server):
        super().__init__()
        self.online = True
        self.name = name
        self.number = None
        self.clientsocket = clientsocket
        self.server = server

    def incmsg(self):
        while self.online:
            try:
                print('[SERVER]: Warte auf Nachricht.')
                msg = self.clientsocket.recv(1024)
                msg = msg.decode()
                bc_msg = str(f'{self.name}: {msg}')
                print(bc_msg)
                self.server.broadcast(bc_msg)

            except ConnectionResetError:
                for idx, client in enumerate(self.server.userlist):
                    self.server.userlist.pop(idx)
                    client.shutdown()
                    self.server.get_userlist()

    def get_user_number(self):
        for idx, client in enumerate(self.server.userlist):
            if client.clientsocket == self.clientsocket:
                self.number = idx

    def shutdown(self):
        self.clientsocket.close()
        self.online = False
