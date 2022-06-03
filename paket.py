import json


class Paket:
    def __init__(self, typ, sender, current, data):
        self.typ = typ
        self.sender = sender
        self.current = current
        self.data = data

    def packen(self):
        container = json.dumps(self.__dict__)
        return container
