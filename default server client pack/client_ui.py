import PySimpleGUI as sg


class ClientUI:
    def __init__(self, parent):
        self.parent = parent

        self.layout = [[sg.Multiline(size=(100, 20), key='-OUT-')],
                       [sg.Input(key='-MSG-', do_not_clear=False, focus=True),
                        sg.Button('Send', bind_return_key=True), sg.Cancel()]]

        self.window = sg.Window('Test', self.layout)

    def hauptfenster(self):
        while self.parent.online:
            event, values = self.window.read()

            if event == 'Send':
                msg = values['-MSG-']
                msg = msg.encode()
                self.parent.serversocket.send(msg)

            if event == sg.WIN_CLOSED:
                break

        self.parent.shutdown()
