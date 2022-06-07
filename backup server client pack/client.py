import socket
import threading
from client_ui import ClientUI


class Client:
    def __init__(self):
        self.online = True

        self.server = '127.0.0.1'
        self.port = 5555
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.name = None
        self.number = None

        self.ui = ClientUI(self)

        self.sep = '#SEP#'
        self.typ_message = 'MSG'
        self.typ_namechange = 'NAME'
        self.typ_user = 'UL'

    def connect(self):
        self.serversocket.connect((self.server, self.port))

        new_thread = threading.Thread(target=self.incoming_msg, args=())
        new_thread.start()

        self.ui.hauptfenster()

    def incoming_msg(self):
        while self.online:
            ans = self.serversocket.recv(1024)
            ans = ans.decode()
            self.enigma(ans)

    def outgoing_msg(self, typ, out):
        if self.online:
            msg = str(f'{typ}{self.sep}{out}').encode()
            self.serversocket.send(msg)
        if not self.online:
            pass

    def newname(self, name):
        self.name = name
        self.outgoing_msg(self.typ_namechange, name)

    def enigma(self, inc):
        typ, msg = inc.split(self.sep)
        if typ == self.typ_message:
            self.ui.window['-OUT-'].print(msg)
        if typ == self.typ_namechange:
            print('das sollte hier nicht ankommen')
        if typ == self.typ_user:
            self.ui.window['-LIST-'].update(msg)

    def shutdown(self):
        self.ui.window.close()
        self.serversocket.close()
        self.online = False


c = Client()
c.connect()