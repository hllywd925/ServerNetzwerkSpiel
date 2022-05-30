import socket
from _thread import *
import PySimpleGUI as sg

server = '127.0.0.1'
port = 5555

# name = str(input('Alias: '))
name = 'LELEK'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
name = name.encode()
s.send(name)

layout = [[sg.Multiline(size=(100, 20), key='-OUT-')],
          [sg.Input(key='-MSG-', do_not_clear=False, focus=True), sg.Button('Send', bind_return_key=True), sg.Cancel()]]

window = sg.Window('Test', layout)


def incoming_msg():
    while True:
        ans = s.recv(1024)
        ans = ans.decode()
        # print(ans)
        window['-OUT-'].print(ans)


start_new_thread(incoming_msg, ())

while True:
    event, values = window.read()
    if event == 'Send':
        msg = values['-MSG-']
        msg = msg.encode()
        s.send(msg)

    if event == sg.WIN_CLOSED:
       break

window.close()