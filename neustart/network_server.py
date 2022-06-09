import socket
import threading
from server_user import ServerUser


class Server(threading.Thread):
    def __init__(self):
        super().__init__()
        self.online = True
        self.address = '127.0.0.1'
        self.port = 5555
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.userlist = []

    def awake(self):
        self.serversocket.bind((self.address, self.port))
        self.serversocket.listen(0)
        print('Server gestartet...')

        while self.online:
            (clientsocket, addr) = self.serversocket.accept()

            user = ServerUser(self, clientsocket)
            self.userlist.append(user)
            user.online = True

            new_thread = threading.Thread(target=user.incoming_data, args=())
            new_thread.start()

    def broadcast(self, data):
        for user in self.userlist:
            d = data.encode()
            user.clientsocket.send(d)

    def privatcast(self, clientsocket, data):
        d = data.encode()
        clientsocket.send(d)

    def update_userlist(self):
        pass

    def shutdown(self):
        for client in self.userlist:
            client.shutdown()
        self.online = False
        self.serversocket.close()


if __name__ == "__main__":
    s = Server()
    s.awake()
