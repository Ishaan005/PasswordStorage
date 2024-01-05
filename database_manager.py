import sqlite3 as sql

class Database:
    def __init__(self):
        self.connect = sql.connect("passwords.db")
        self.cursor = self.connect.cursor()

    def create_database(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS passwords
                    (name, password)""" )
        self.connect.commit()

    def add_password(self, name, password):
        self.cursor.execute("INSERT INTO passwords VALUES (:name, :password)", 
                            {"name": name, "password": password})
        self.connect.commit()

    def query_database(self):
        # Execute a SELECT query
        self.cursor.execute("SELECT * FROM passwords")

        # Fetch all the rows from the query
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)

    def clear_database(self):
        self.connect = sql.connect("passwords.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute("DELETE FROM passwords")

        self.connect.commit()