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
                tetten = 'popel'

            if event == sg.WIN_CLOSED:
                break

        self.parent.shutdown()
