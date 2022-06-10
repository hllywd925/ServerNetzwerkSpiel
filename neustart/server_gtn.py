import random
import time


class GuessTheNumber:
    def __init__(self, server, player):
        self.server = server
        self.run = False
        self.player = player  # liste mit Spieler wird vom Server übergeben (alle Angemeldeten)
        self.guesses = 0

    def start(self):
        needed = len(self.player)
        print(needed)
        print(self.guesses)
        while True:
            print('spiel läuft')  # der gamethread, hier gehts weiter
            if self.guesses == needed:
                print(needed)
                print(self.guesses)
                for g in self.player:
                    print(g.name, ': ', g.guess)
                break
            time.sleep(2)
        print(needed)
        print(self.guesses)
        for g in self.player:
            print(g.name, ': ', g.guess)
            g.guess = None
        self.server.end_gtn()

    def who_is_the_winner(self):
        pass
