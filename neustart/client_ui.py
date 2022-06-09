import PySimpleGUI as Sg


class ClientUI:
    def __init__(self, parent):
        self.parent = parent

        self.menu_def = [['&Datei', ['&Adresse']], ['&Verbindung', ['&Verbinden', '&Trennen']]]
        self.layout = [[Sg.Menu(self.menu_def)],
                       [Sg.Multiline(size=(80, 20), key='-OUT-')],
                       [Sg.Input(key='-MSG-', do_not_clear=False, focus=True), Sg.Button('Send', bind_return_key=True)]]
        self.window = Sg.Window('Chatserver', self.layout)

    def hauptfenster(self):
        while True:
            event, values = self.window.read()

            if event == 'Send':
                msg = values['-MSG-']
                if msg[0] and msg[1] == '/':
                    self.user_command(msg)
                else:
                    self.parent.packer('MSG', msg)

            if event == 'Adresse':


                self.adressfenster()

            if event == 'Verbinden':
                self.verbindungsfenster()

            if event == 'Trennen':
                self.parent.shutdown()

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
        if command in ['//connect', '//c', '//con']:
            self.parent.network.connecting()
        if command == '//x':
            self.parent.shutdown()
        if command == '//ul':  # fordert Liste der aktuell User die online sind an
            pass

    def adressfenster(self):
        layout = [[Sg.Push(),Sg.Text('IP-Adresse'), Sg.Input(key='-ADDR-', default_text='127.0.0.1')],
                  [Sg.Push(),Sg.Text('Port'), Sg.Input(key='-PORT-', default_text=5555)],
                  [Sg.Button('OK', key='-OKADDR-', bind_return_key=True)]]

        window = Sg.Window('', layout, no_titlebar=True, keep_on_top=True)

        while True:
            event, values = window.read()

            if event == '-OKADDR-':
                self.parent.network.server = values['-ADDR-']
                self.parent.network.port = values['-PORT-']
                window.close()

    def verbindungsfenster(self):
        layout = [[Sg.Push(), Sg.Text('Login'), Sg.Input(key='-LOGIN-', default_text='Max')],
                  [Sg.Push(), Sg.Text('Passwort'), Sg.Input(key='-PASSWORD-', default_text='1')],
                  [Sg.Button('Verbinden', key='-VERBINDEN-', bind_return_key=True, focus=True)]]

        v_window = Sg.Window('', layout, no_titlebar=True, keep_on_top=True)

        while True:
            event, values = v_window.read()

            if event == '-VERBINDEN-':
                self.parent.user_command('//c')
                break

        v_window.close()


if __name__ == "__main__":
    c = ClientUI(None)
    c.hauptfenster()
