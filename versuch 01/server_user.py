import pickle


class User:
    def __init__(self, name, nummer, cs):
        self.name = name
        self.nummer = nummer
        self.cs = cs
        self.data = None

    def threaded_client(self, clientsocket, current):
        while True:
            data = pickle.loads(clientsocket.recv(4096))
            current.data = data
            print(data)
            if current == 1:
                current.cs.send(pickle.dumps(data))
            else:
                current.cs.send(pickle.dumps(data))