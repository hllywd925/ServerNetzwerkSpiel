import socket
import threading
from client_ui import ClientUI


class Client:
    def __init__(self):
        self.online = True

        self.server = '127.0.0.1'
        self.port = 5555
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.name = 'Lelek'
        self.number = None

        self.ui = ClientUI(self)

    def connect(self):
        self.serversocket.connect((self.server, self.port))

        name = self.name.encode()
        self.serversocket.send(name)

        new_thread = threading.Thread(target=self.incoming_msg, args=())
        new_thread.start()

        self.ui.hauptfenster()

    def incoming_msg(self):
        while self.online:
            ans = self.serversocket.recv(1024)
            ans = ans.decode()
            self.ui.window['-OUT-'].print(ans)

    def shutdown(self):
        self.ui.window.close()
        self.serversocket.close()
        self.online = False


c = Client()
c.connect()
