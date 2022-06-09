from client_ui import ClientUI
from network_client import Network
import packer
import json


class ClientUser:
    def __init__(self):
        self.ui = ClientUI(self)
        self.network = Network(self)
        self.user_id = None
        self.name = None

    def user_command(self, command):
        # hier werden die User Befehle an die entsprechenden Methoden weitergeleitet
        if command in ['//help', '//h']:
            self.ui.print_to_window('[TO BE IMPLEMENTED]: Liste Usercommands')
        if command in ['//connect', '//c', '//con']:
            self.network.connecting()
        if command == '//x':
            self.shutdown()
        if command == '//ul':  # fordert Liste der aktuell User die online sind an
            pass

    def packer(self, typ, data):  # hier werden die raus gehenden JSON gepackt und an den Server gesendet
        p = packer.Packer(typ, self.user_id, self.name, data)
        p = p.pack()
        self.network.outgoing_data(p)

    def distributor(self, package):  # hier werden die rein kommenden JSON entpackt und weitergeleitet
        data = json.loads(package)
        d_typ, d_user_id, d_name, d_data = data['typ'], data['user_id'], data['name'], data['data']
        if d_typ == 'WLCM':
            self.ui.print_to_window(d_data)
        if d_typ == 'MSG':
            self.ui.print_to_window(f'[{d_name}][{d_user_id}]: {d_data}')
        pass

    def shutdown(self):
        self.network.serversocket.close()
        self.network.online = False


if __name__ == "__main__":
    client = ClientUser()
    client.ui.hauptfenster()
