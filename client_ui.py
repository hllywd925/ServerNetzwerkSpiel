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
        tab_login = [[sg.Push(), sg.Text('FADKS', font=('Arial', 30), pad=20), sg.Push()],
                     [sg.Push(), sg.Text('Name:'), sg.Input(key='-NAME-', size=(25, 0), focus=True)],
                     [sg.Push(), sg.Text('Passwort:'), sg.Input(key='-PW-', size=(25, 0))],
                     [sg.Push(), sg.Text('', key='-LOGINFO-'), sg.Push()],
                     [sg.Push(), sg.Button('Connect', bind_return_key=True), sg.Push()]]

        tab_reg = [[sg.Push(), sg.Text('FADKS', font=('Arial', 30), pad=20), sg.Push()],
                   [sg.Push(), sg.Text('Name:'), sg.Input(key='-NAME-', size=(25, 0), focus=True)],
                   [sg.Push(), sg.Text('Passwort:'), sg.Input(key='-NPW-', size=(25, 0))],
                   [sg.Push(), sg.Text('Passwort:'), sg.Input(key='-NPWN-', size=(25, 0))],
                   [sg.Push(), sg.Button('Register', bind_return_key=True), sg.Push()]]

        tab_pref = [[sg.Push(), sg.Text('IP:'), sg.Input(key='-IP-', size=(25, 0), default_text='127.0.0.1')],
                    [sg.Push(), sg.Text('Port:'), sg.Input(key='-PORT-', size=(25, 0), default_text='5555')]]

        ww_layout = [[sg.TabGroup([[sg.Tab('Anmelden', tab_login),
                                    sg.Tab('Registrieren', tab_reg),
                                    sg.Tab('Optionen', tab_pref)]],
                                  expand_x=True, expand_y=True)]]

        welcome_window = sg.Window('', ww_layout, keep_on_top=True)

        while True:
            event, values = welcome_window.read()

            if event == 'Connect':
                name = values['-NAME-']
                passwort = str(values['-PW-'])
                self.parent.server = values['-IP-']
                self.parent.port = int(values['-PORT-'])
                self.parent.outmsg('login', (name, passwort))
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
