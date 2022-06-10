import random


class GuessTheNumber:
    def __init__(self, server, player):
        self.server = server
        self.run = False
        self.player = player  # liste mit Spieler wird vom Server übergeben (alle Angemeldeten)
        self.guesses = 0

    def waiting_for_guesses(self):
        needed = len(self.player)

    def start(self):
        while True:
            print('spiel läuft')  # der gamethread, hier gehts weiter

    def who_is_the_winner(self):
        pass
