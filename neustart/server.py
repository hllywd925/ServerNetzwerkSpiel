import socket
from threading import Thread
from server_user import ServerUser


class Server:
    def __init__(self):
        self.address = '127.0.0.1'
        self.port = 5555
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.userlist = []

    def awake(self):
        self.serversocket.bind((self.address, self.port))
        self.serversocket.listen()
        self.connecting_clients()

    def connecting_clients(self):
        while True:
            (clientsocket, addr) = self.serversocket.accept()
            print(f'Connected to: {addr} {clientsocket}')

            user = ServerUser(self, clientsocket)
            self.userlist.append(user)

            new_thread = Thread(target=user.incoming_data(), args=())
            new_thread.start()

    def broadcast(self, data):
        for user in self.userlist:
            user.clientsocket.send(data)
