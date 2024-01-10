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

    def edit_password(self, name, password):
        self.cursor.execute("UPDATE passwords SET password = :password WHERE name = :name",
                            {"name": name, "password": password})
        self.connect.commit()

    def delete_password(self, name, password):
        self.cursor.execute("DELETE FROM passwords WHERE name = :name AND password = :password",
                            {"name": name, "password": password})
        self.connect.commit()


    def query_database(self):
        # Execute a SELECT query
        self.cursor.execute("SELECT * FROM passwords")

        # Fetch all the rows from the query
        rows = self.cursor.fetchall()

        password_list = []
        for row in rows:
            password_list.append(row)
        return password_list

    def clear_database(self):
        self.connect = sql.connect("passwords.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute("DELETE FROM passwords")

        self.connect.commit()

        