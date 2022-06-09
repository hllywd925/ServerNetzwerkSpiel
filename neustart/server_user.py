import json
import packer
from db_controller import DBController


class ServerUser:
    def __init__(self, server, clientsocket):
        self.online = False
        self.name = None
        self.user_id = None
        self.server = server
        self.clientsocket = clientsocket
        self.db = DBController()

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
                print(f'[DEBUG][USERLIST][DISCONNECT]: {self.server.userlist}')

    def distributor(self, package):
        data = json.loads(package)
        if data['typ'] == 'MSG':
            self.server.broadcast(package)
        if data['typ'] == 'LGIN':
            user_id, data_new, access = self.db.login_check(data['name'], data['data'])
            p = packer.Packer('SERVERLOGIN', user_id, data['name'], data_new)
            p = p.pack()
            self.server.privatcast(self.clientsocket, p)
            if access:
                self.user_id = user_id
                self.name = data['name']
            if not access:
                self.shutdown()
        if data['typ'] == 'RGSTR':
            print(data['data'])
            user_id_new, name_new, passwort_new, data_new, access = self.db.creating_new_user(data['data'])
            p = packer.Packer('SERVERREGISTER', user_id_new, name_new, data_new)
            p = p.pack()
            self.server.privatcast(self.clientsocket, p)
            print(p)
            if access:
                self.user_id = user_id_new
                self.name = name_new
            if not access:
                self.shutdown()

    def wellcome(self):
        pass

    def shutdown(self):
        self.clientsocket.close()
        self.online = False
