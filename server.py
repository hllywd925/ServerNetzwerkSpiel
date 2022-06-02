import socket
import threading
from user import User


class Server:
    def __init__(self):
        self.addr = '127.0.0.1'
        self.port = 5555
        self.serversocket = None
        self.user = []

    def awake(self):
        print('Server wartet...')
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind((self.addr, self.port))
        self.serversocket.listen(0)

    def adding_clients(self):
        current = 0
        while True:
            (clientsocket, address) = self.serversocket.accept()
            player = User(current, None, clientsocket)
            self.user.append(player)

            new_thread = threading.Thread(target=self.user[current].threaded_user, args=())
            new_thread.start()

            current += 1
