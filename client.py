import socket
import threading
import json
from client_ui import ClientUI
from paket import Paket


class Client:
    def __init__(self):
        self.online = False
        self.logged_in = False

        self.server = '127.0.0.1'
        self.port = 5555
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.name = None
        self.passwort = None
        self.number = None

        self.ui = ClientUI(self)

    def start(self):
        self.connect()
        self.login()
        self.ui.hauptfenster()

    def connect(self):
        try:
            self.serversocket.connect((self.server, self.port))
            self.online = True

            new_thread = threading.Thread(target=self.incmsg, args=())
            new_thread.start()

        except OSError as e:
            print(e)

    def incmsg(self):
        while self.online:
            ans = self.serversocket.recv(1024)
            self.instantreply()
            ans = ans.decode()
            self.denigma(ans)

    def login(self):
        while not self.logged_in:
            self.ui.willkommensfenster()

    def denigma(self, msg):
        paket = json.loads(msg)
        if paket['typ'] == 'msg':
            sender = paket['sender']
            data = paket['data']
            printmessage = f'[{sender}]: {data}'
            self.ui.window['-OUT-'].print(printmessage)
        if paket['typ'] == 'name':
            self.name = paket['data']
        if paket['typ'] == 'login':
            pass

    def outmsg(self, typ, data):
        msg = Paket(typ, self.name, self.number, data)
        msg = json.dumps(msg.__dict__)
        msg = msg.encode()
        self.serversocket.send(msg)

    def instantreply(self):
        reply = Paket('instantreply', self.name, self.number, '')
        reply = json.dumps(reply.__dict__)
        reply = reply.encode()
        self.serversocket.send(reply)

    def shutdown(self):
        self.ui.window.close()
        self.serversocket.close()
        self.online = False


if __name__ == '__main__':
    c = Client()
    c.start()
