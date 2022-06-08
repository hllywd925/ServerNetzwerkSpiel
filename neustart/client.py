import socket
from threading import Thread


class Client:
    def __init__(self):
        self.server = '127.0.0.1'
        self.port = 5555
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connecting(self):
        try:
            self.serversocket.connect((self.server, self.port))

            new_thread = Thread(target=self.incoming_data, args=())
            new_thread.start()

        except OSError as e:
            print(e)

    def incoming_data(self):
        while True:
            package = self.serversocket.recv(1024)
            package = package.decode()