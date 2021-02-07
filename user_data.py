# This file contains all the user api keys and other data
import sqlite3


class UserData:
    def __init__(self):
        self.conn = sqlite3.connect('data/api_data.db')

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE")