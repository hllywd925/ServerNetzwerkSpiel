import socket
import threading
import json
from client_ui import ClientUI
from paket import Paket


class Client:
    def __init__(self):
        self.online = True

        self.server = '127.0.0.1'
        self.port = 5555
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.name = None
        self.number = None

        self.ui = ClientUI(self)

    def connect(self):
        self.serversocket.connect((self.server, self.port))

        new_thread = threading.Thread(target=self.incmsg, args=())
        new_thread.start()

        # self.ui.namensfenster()
        self.ui.hauptfenster()

    def incmsg(self):
        while self.online:
            ans = self.serversocket.recv(1024)
            ans = ans.decode()
            self.denigma(ans)

    def denigma(self, msg):
        paket = json.loads(msg)
        if paket['typ'] == 'msg':
            sender = paket['sender']
            data = paket['data']
            printmessage = f'[{sender}]: {data}'
            self.ui.window['-OUT-'].print(printmessage)
        if paket['typ'] == 'name':
            self.name = paket['data']

    def outmsg(self, typ, data):
        msg = Paket(typ, self.name, data)
        msg = json.dumps(msg.__dict__)
        msg = msg.encode()
        self.serversocket.send(msg)

    def shutdown(self):
        self.ui.window.close()
        self.serversocket.close()
        self.online = False


c = Client()
c.connect()
