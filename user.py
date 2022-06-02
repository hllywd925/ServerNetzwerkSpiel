import threading
import pickle
import socket


class User:
    def __init__(self, num, name, clientsocket):
        self.num = num
        self.name = name
        self.clientsocket = clientsocket

    def threaded_user(self):
        while True:
            data = self.clientsocket.recv(4096)
            new_data = pickle.loads(data)
