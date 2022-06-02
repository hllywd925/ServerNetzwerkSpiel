import socket
import threading
import pickle
from ursina import *
from server_user import User


class Server(Entity):
    def __init__(self):
        super().__init__()

        self.server = '127.0.0.1'
        self.port = 5555
        self.serversocket = None

        self.players = [User('Tim', 0, None), User('Max', 1, None)]
        self.current_player = 0

    def awake(self):
        print('Starte Server...')
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.serversocket.bind((self.server, self.port))
        self.serversocket.listen(0)

    def adding_clients(self):
        while True:
            (clientsocket, adress) = self.serversocket.accept()
            print('Connected to: ', adress, clientsocket)

            self.players[self.current_player].cs = clientsocket

            new_thread = threading.Thread(target=self.players[self.current_player].threaded_client,
                                          args=(clientsocket, self.players[self.current_player]))
            new_thread.start()

            self.current_player += 1

    def threaded_client(self, clientsocket, current):
        while True:
            data = pickle.loads(clientsocket.recv(4096))
            self.players[current].data = data
            print(data)
            if current == 1:
                self.players[0].cs.send(pickle.dumps(data))
            else:
                self.players[1].cs.send(pickle.dumps(data))
