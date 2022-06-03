import json


class Testdata:
    def __init__(self, typ, sender, data):
        self.typ = typ
        self.sender = sender
        self.data = data


userlist = ['Tim', 'Jan', 'Max']

t1 = Testdata('userlist', userlist, 'server')
t2 = Testdata('message', 'Hello there.', 'User')

# packen zum senden
j1 = json.dumps(t1.__dict__)
j2 = json.dumps(t2.__dict__)

# entpacken zum verarbeiten
d1 = json.loads(j1)
d2 = json.loads(j2)

werner = [d1, d2]

for i in werner:
    if i['typ'] == 'userlist':
        print('userliste wird bearbeitet')

    if i['typ'] == 'message':
        print(i['data'])
