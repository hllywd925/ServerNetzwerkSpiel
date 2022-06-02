import socket
from _thread import *
import pickle
from server_user import User

server = '127.0.0.1'
port = 5555

userlist = []
viewer = []

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((server, port))
serversocket.listen(0)


def broadcast(msg):
    print(msg)
    out_msg = msg
    for u in userlist:
        u.cs.send(pickle.dumps(out_msg))


def threaded_client(clientsocket, current):
    while True:
        msg = pickle.loads(clientsocket.recv(1024))
        bc_msg = str(f'{userlist[current].name}: {msg}')
        broadcast(bc_msg)


current_user = 0
while True:
    (clientsocket, adress) = serversocket.accept()
    print('Connected to: ', adress, clientsocket)

    name = pickle.loads(clientsocket.recv(1024))
    user = User(name, current_user, clientsocket)
    userlist.append(user)

    print(f'{userlist[current_user].name} connected')

    if name != 'Zuschauer':
        start_new_thread(threaded_client, (clientsocket, current_user))
    current_user += 1

clientsocket.close()
serversocket.colse()
