import json
import packer


class ServerUser:
    def __init__(self, server, clientsocket):
        self.online = False
        self.logged_in = False
        self.name = None
        self.user_id = None
        self.server = server
        self.clientsocket = clientsocket

    def incoming_data(self):
        while self.online:
            try:
                package = self.clientsocket.recv(1024)
                package = package.decode()
                self.distributor(package)

            except ConnectionResetError:
                self.clientsocket.close()
                for idx, client in enumerate(self.server.userlist):
                    if client.clientsocket == self.clientsocket:
                        self.server.userlist.pop(idx)
                        client.shutdown()
                print(f'[DEBUG][USERLIST]: {self.server.userlist}')

    def distributor(self, package):
        data = json.loads(package)
        if data['typ'] == 'MSG':
            self.server.broadcast(package)
        print(f'{type(data)} {data}')

    def wellcome(self):
        w = packer.Packer('WLCM', 'Server', 'Server', 'Herzlich Willkommen!')
        print(w.pack())
        self.server.privatcast(self.clientsocket, w.pack())

    def shutdown(self):
        self.clientsocket.close()
        self.online = False
