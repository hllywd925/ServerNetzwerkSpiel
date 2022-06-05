from tinydb import TinyDB, Query
import json
import random


class DBController:
    def __init__(self):
        self.db = TinyDB('user_db.json')
        self.User = Query()

    def insert(self):
        self.db.insert({'number': 250989, 'name': 'max', 'passwort': '1', 'status': True})

    def read(self):
        pass

    def check_name(self, name):
        result = self.db.search(self.User.name == str(name))
        if result:
            return print('Name bereits vergeben')
        else:
            return name

    def giving_user_number(self):
        while True:
            number = random.randrange(100001, 999999)
            result = self.db.search(self.User.number == number)
            if result:
                result = None
            if not result:
                break
        return number

    def creating_new_user(self, name, passwort):
        number = self.giving_user_number()
        self.db.insert({
            'number': number,
            'name': str(name),
            'passwort': str(passwort),
            'status': True
        })
        pass


if __name__ == '__main__':
    d = DBController()
    d.check_name('max')
