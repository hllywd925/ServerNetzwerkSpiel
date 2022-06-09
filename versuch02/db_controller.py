from tinydb import TinyDB, Query
import json
import random


class DBController:
    def __init__(self):
        self.db = TinyDB('user_db.json')
        self.User = Query()

    def insert(self):
        self.db.insert({'user_id': 250989, 'name': 'max', 'passwort': '1', 'status': True})

    def read(self):
        pass

    def check_login(self, name, passwort):
        user = self.db.search(self.User.name == str(name))
        if user:
            if passwort == user[0]['passwort']:
                print('DEBUG: Name und Passwort OK')
                print(user[0]['name'], user[0]['user_id'], 'ACCESS GRANTED')
                return user[0]['name'], user[0]['user_id'], 'ACCESS GRANTED'
            else:
                return '', '', 'WRONG PASS'
        else:
            print(f'DEBUG: Name falsch')
            return '', '', 'WRONG NAME'

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
        user_id = self.giving_user_number()
        self.db.insert({
            'user_id': user_id,
            'name': str(name),
            'passwort': str(passwort),
            'status': True
        })
        pass


if __name__ == '__main__':
    d = DBController()
    d.creating_new_user('Jan', 1)
