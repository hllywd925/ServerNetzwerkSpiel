import PySimpleGUI as Sg


class ClientUI:
    def __init__(self, parent):
        self.parent = parent

        self.menu_def = [['&Datei', ['&Adresse']], ['&Verbindung', ['&Verbinden', '&Trennen', '&Registrieren']]]
        self.layout = [[Sg.Menu(self.menu_def)],
                       [Sg.Multiline(size=(80, 20), key='-OUT-')],
                       [Sg.Input(key='-MSG-', do_not_clear=False, focus=True), Sg.Button('Send', bind_return_key=True)]]
        self.window = Sg.Window('Chatserver', self.layout)

    def hauptfenster(self):
        while True:
            event, values = self.window.read()

            if event == 'Send':
                msg = values['-MSG-']
                self.parent.packer('MSG', msg)
                try:
                    if msg[0] and msg[1] == '/':
                        self.user_command(msg)
                except IndexError as e:
                    print(e)
                    self.parent.packer('MSG', msg)

            if event == 'Adresse':
                self.adressfenster()

            if event == 'Verbinden':
                self.verbindungsfenster()

            if event == 'Trennen':
                self.parent.shutdown()

            if event == 'Registrieren':
                self.registrierfenster()

            if event == Sg.WIN_CLOSED:
                break

        self.window.close()
        self.parent.shutdown()

    def print_to_window(self, text):
        self.window['-OUT-'].print(type(text))
        self.window['-OUT-'].print(text)

    def user_command(self, command):  # hier werden Befehle an die entsprechenden Methoden weitergeleitet
        if command in ['//help', '//h']:
            self.print_to_window('[TO BE IMPLEMENTED]: Liste Usercommands')
        if command == '//x':
            self.parent.shutdown()
        if command == '//ul':  # fordert Liste der aktuell User die online sind an
            pass

    def adressfenster(self):
        layout = [[Sg.Push(), Sg.Text('IP-Adresse'), Sg.Input(key='-ADDR-', default_text='127.0.0.1')],
                  [Sg.Push(), Sg.Text('Port'), Sg.Input(key='-PORT-', default_text=5555)],
                  [Sg.Button('OK', key='-OKADDR-', bind_return_key=True)]]

        a_window = Sg.Window('', layout, keep_on_top=True)

        while True:
            event, values = a_window.read()

            if event == '-OKADDR-':
                self.parent.network.server = values['-ADDR-']
                self.parent.network.port = values['-PORT-']
                break

            if event == Sg.WIN_CLOSED:
                break

        a_window.close()

    def verbindungsfenster(self):
        layout = [[Sg.Push(), Sg.Text('Login'), Sg.Input(key='-LOGIN-', default_text='Max')],
                  [Sg.Push(), Sg.Text('Passwort'), Sg.Input(key='-PASSWORT-', default_text='1')],
                  [Sg.Button('Verbinden', key='-VERBINDEN-', bind_return_key=True, focus=True)]]

        v_window = Sg.Window('', layout, keep_on_top=True)

        while True:
            event, values = v_window.read()

            if event == '-VERBINDEN-':
                self.parent.name = values['-LOGIN-']
                self.parent.passwort = values['-PASSWORT-']
                self.parent.network.connecting('log')
                break

            if event == Sg.WIN_CLOSED:
                break

        v_window.close()

    def registrierfenster(self):
        layout = [[Sg.Push(), Sg.Text('Benutzername'), Sg.Input(key='-REGIS-')],
                  [Sg.Push(), Sg.Text('Passwort'), Sg.Input(key='-PASSEINS-')],
                  [Sg.Push(), Sg.Text('Passwort'), Sg.Input(key='-PASSZWEI-')],
                  [Sg.Button('Registrieren', key='-REGISTRIEREN-', bind_return_key=True, focus=True)]]

        r_window = Sg.Window('', layout, keep_on_top=True)

        while True:
            event, values = r_window.read()

            if event == '-REGISTRIEREN-':
                if values['-PASSEINS-'] == values['-PASSZWEI-']:
                    self.parent.name = values['-REGIS-']
                    self.parent.passwort = values['-PASSEINS-']
                    self.parent.network.connecting('reg')
                else:
                    self.window['-OUT-'].print('Registrierung fehlgeschlagen')
                break

            if event == Sg.WIN_CLOSED:
                break

        r_window.close()


if __name__ == "__main__":
    c = ClientUI(None)
    c.hauptfenster()
