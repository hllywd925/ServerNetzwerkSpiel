import socket
from threading import Thread


class Network:
    def __init__(self, parent):
        self.server = '127.0.0.1'
        self.port = 5555
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.parent = parent

    def connect(self):
        try:
            self.serversocket.connect((self.server, self.port))

            new_thread = Thread(target=self.receiving, args=())
            new_thread.start()

        except OSError as e:
            print(e)

    def receiving(self):
        while True:
            data_from_server = self.serversocket.recv(1024)
            data_from_server = data_from_server.decode()
            self.parent.denigma(data_from_server)

    def sending(self, data):
        data_to_server = data.encode()
        self.serversocket.send(data_to_server)
