class ServerUser:
    def __init__(self, server, clientsocket):
        self.name = None
        self.user_id = None
        self.server = server
        self.cliensocket = clientsocket

    def incoming_data(self):
        while True:
            try:
                data = self.cliensocket.recv(1024)
                data = data.encode()
                self.server.broadcast(data)

            except ConnectionResetError:
                self.cliensocket.close()
                pass
