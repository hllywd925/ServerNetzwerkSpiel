class User:
    def __init__(self, name, clientsocket, server):
        super().__init__()
        self.name = name
        self.number = None
        self.clientsocket = clientsocket
        self.server = server

        self.online = True

    def incmsg(self):
        while self.online:
            print('[SERVER]: Warte auf Nachricht.')
            msg = self.clientsocket.recv(1024)
            msg = msg.decode()
            bc_msg = str(f'{self.name}: {msg}')
            print(bc_msg)
            self.server.broadcast(bc_msg)

    def shutdown(self):
        self.online = False
        self.clientsocket.close()