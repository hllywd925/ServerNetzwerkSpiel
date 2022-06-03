import PySimpleGUI as sg


class ClientUI:
    def __init__(self, parent):
        self.parent = parent

        self.layout = [[sg.Multiline(size=(60, 20), key='-OUT-'),
                        sg.Listbox(values=[], size=(15, 20), key='-LIST-', no_scrollbar=True)],
                       [sg.Input(key='-MSG-', do_not_clear=False, focus=True),
                        sg.Button('Send', bind_return_key=True), sg.Button('Neuer Name'), sg.Button('Testliste'),
                        sg.Button('TESTValues')]]
        self.window = sg.Window('Chatserver', self.layout)
        self.window_run = False

    def willkommensfenster(self):
        welcome_window_layout = [
                                [sg.Text('Willkommen im ITF Chat.')],
                                [sg.Text('Name:'), sg.Input(key='-NAME-')],
                                [sg.Text('IP:'), sg.Input(key='-IP-', default_text='127.0.0.1'),
                                 sg.Text('Port:'), sg.Input(key='-PORT-', default_text='5555')],
                                [sg.Button('Connect', bind_return_key=True)]
                                ]
        welcome_window = sg.Window('', welcome_window_layout, keep_on_top=True)

        while True:
            event, values = welcome_window.read()

            if event == 'Connect':
                self.parent.name = values['-NAME-']
                self.parent.server = values['-IP-']
                self.parent.port = int(values['-PORT-'])
                self.parent.connect()
                break

            if event == sg.WIN_CLOSED:
                break

        welcome_window.close()

    def namensfenster(self):
        name_window_layout = [[sg.Text('Bitte Namen eintippen')],
                              [sg.Input(key='-NAME-', focus=True)],
                              [sg.Button('Bestätigen', bind_return_key=True)]]
        name_window = sg.Window('', name_window_layout, no_titlebar=True, keep_on_top=True)

        while True:
            event, values = name_window.read()

            if event == 'Bestätigen':
                if values['-NAME-']:
                    name = values['-NAME-']
                    self.parent.outmsg('name', name)
                    break

        name_window.close()

    def hauptfenster(self):
        self.window_run = True
        while self.parent.online:
            event, values = self.window.read()

            if event == 'Send':
                msg = values['-MSG-']
                self.parent.outmsg('msg', msg)

            if event == 'Neuer Name':
                self.namensfenster()

            if event == 'Testliste':
                pass

            if event == 'TESTValues':
                for i in range(100):
                    self.parent.outmsg('msg', 'STRESSTEST')

            if event == sg.WIN_CLOSED:
                break

        self.parent.shutdown()


if __name__ == '__main__':
    c = ClientUI('test')
    c.willkommensfenster()
