import json


class Paket:
    def __init__(self, typ, sender, data):
        self.typ = typ
        self.sender = sender
        self.data = data

    def packen(self):
        container = json.dumps(self.__dict__)
        return container
