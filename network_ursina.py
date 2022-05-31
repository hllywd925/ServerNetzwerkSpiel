import socket
import threading
import pickle
from ursina import *
from server_ursina import Server
from log_writer import log


class NetworkManager(Entity):
    def __init__(self):
        super().__init__(
            origin=(-.5, .5, 0),
            parent=camera.ui)

        self.server = '127.0.0.1'
        self.port = 5555
        self.client_socket = None
        self.recv_data = None
        # Threads
        self.local_server = None
        self.inc_thread = None

        self.b1 = Button('Host (Server + Client)',
                         parent=self,
                         color=color.black66,
                         scale=(1, .1),
                         position=(0, .1, 0),
                         on_click=self.host_a_game)

        self.b2 = Button('Client',
                         parent=self,
                         color=color.black66,
                         scale=(.5, .1),
                         position=(-.25, 0, 0),
                         on_click=self.connect_to_server)

        self.i1 = InputField(text=self.server ,parent=self, x=.25, scale=(.5, .1))
        self.b3 = Button('Server Only)',
                         parent=self,
                         color=color.black66,
                         scale=(1, .1),
                         position=(0, -.1, 0),
                         on_click=self.server_only)

    def host_a_game(self):  # hostet ein lokales Spiel
        print('host a game')
        self.local_server = threading.Thread(target=self.server_only, args=())
        self.local_server.start()
        self.connect_to_server()

    def connect_to_server(self):
        self.server = self.i1.text
        print('Suche nach Server...')
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.server, self.port))
        except socket.error as e:
            print(e)
            print('Kein Server gefunden')
            return
        print('Server gefunden')
        self.inc_thread = threading.Thread(target=self.receive_data, args=())
        self.inc_thread.start()
        self.disable()

    def server_only(self):
        s = Server()
        s.awake()
        s.adding_clients()

    def send_data(self, data):
        print('before send')
        print(data.name)
        print(data.typ)
        print(data.x)
        data_send = pickle.dumps(data)
        print(data_send)
        self.client_socket.send(data_send)

    def receive_data(self):
        while True:
            print('after receive')
            recv_data = self.client_socket.recv(4096)
            print(recv_data)
            data = pickle.loads(recv_data)
            print(f'data inc {data.typ}')
            log(data)
