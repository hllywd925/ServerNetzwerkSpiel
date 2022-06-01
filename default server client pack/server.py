import socket
import threading
from server_user import User


class Server(threading.Thread):
    def __init__(self):
        super().__init__()

        self.online = True

        self.server = '127.0.0.1'
        self.port = 5555

        self.userlist = []

        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def awake(self):
        self.serversocket.bind((self.server, self.port))
        self.serversocket.listen(0)
        print('Server gestartet...')

        while self.online:
            (clientsocket, adress) = self.serversocket.accept()
            print('Connected to: ', adress, clientsocket)

            name = clientsocket.recv(1024)
            name_fin = name.decode()
            user = User(name_fin, clientsocket, self)
            self.userlist.append(user)
            print(f'[SERVER]: {self.userlist}')

            new_thread = threading.Thread(target=user.incmsg, args=())
            new_thread.start()

    def broadcast(self, msg):
        out_msg = msg.encode()
        for u in self.userlist:
            u.clientsocket.send(out_msg)

    def shutdown(self):
        self.online = False
        self.serversocket.close()


s = Server()
s.awake()
