import socket
import threading
from server_user import User
from db_controller import DBController


class Server(threading.Thread):
    def __init__(self):
        super().__init__()
        self.online = True
        self.server = '127.0.0.1'
        self.port = 5555
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.db_c = DBController()
        self.userlist = []

    def awake(self):
        self.serversocket.bind((self.server, self.port))
        self.serversocket.listen(0)
        print('Server gestartet...')

        while self.online:
            (clientsocket, adress) = self.serversocket.accept()
            print('Connected to: ', adress, clientsocket)

            user = User(None, clientsocket, self)
            self.userlist.append(user)
            user.get_user_number()

            new_thread = threading.Thread(target=user.incmsg, args=())
            new_thread.start()

    def broadcast(self, msg):
        out_msg = msg.encode()
        for u in self.userlist:
            u.clientsocket.send(out_msg)

    def privatcast(self, clientsocket, msg):
        out = msg.encode()
        clientsocket.send(out)

    def get_userlist(self):
        for client in self.userlist:
            client.get_user_number()

    def shutdown(self):
        for client in self.userlist:
            client.shutdown()
        self.online = False
        self.serversocket.close()


if __name__ == '__main__':
    s = Server()
    s.awake()
