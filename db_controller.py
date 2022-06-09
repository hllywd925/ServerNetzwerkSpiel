from tinydb import TinyDB, Query
import json
import random


class DBController:
    def __init__(self):
        self.db = TinyDB('user_db.json')
        self.User = Query()

    def insert(self):
        self.db.insert({'user_id': 250989, 'name': 'max', 'passwort': '1', 'status': True})


if __name__ == '__main__':
    d = DBController()
