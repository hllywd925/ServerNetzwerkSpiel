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


"""
Datentypen:
msg = Nachricht eines Spielers
name = Änderung des Usernames
instantreply = antwort an server ob Nachricht empfangen wurde
userid = Übergabe der UserID
create_user = 
error_login = fehler beim Login
"""

if __name__ == '__main__':
    p = Paket('test', 'Max', '1234', ('max', '1111'))

    c = p.packen()
    print(c)
    d = json.loads(c)
    print(d['data'][1])
