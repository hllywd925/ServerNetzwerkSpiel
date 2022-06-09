from network import Network
import packer


class Client:
    def __init__(self):
        self.n = Network(self)

        self.name = None
        self.user_id = None
        self.online = False

    def denigma(self, data):
        d = packer.Entpacken(data)
        print(d)
        d = d.entpacken()
        print(d)


if __name__ == '__main__':
    c = Client()
    p = packer.Packen('test', 'Max', '1234', ('max', '1111'))
    c.denigma(c)
