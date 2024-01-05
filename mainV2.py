from tkinter import *
import sqlite3 as sql
from numba import njit
from database_manager import Database


def main():
    db = Database()
    db.create_database()

    #Main window
    root = Tk()
    root.title("Password Manager")

    #Labels
    Label(root, text = "Name: ").grid(row = 0, column = 0, sticky = W)
    Label(root, text = "Password: ").grid(row = 1, column = 0, sticky = W)  

    #Entries
    id_entry = Entry(root)
    id_entry.grid(row = 0, column = 1)
    password_entry = Entry(root)
    password_entry.grid(row = 1, column = 1)

    #Buttons
    add_button = Button(root, text = "Add Password" , command = lambda: db.add_password(id_entry.get(), password_entry.get()))
    add_button.grid(row = 2, column = 0, columnspan = 2)
    view_button = Button(root, text = "View Passwords", command = db.query_database)
    view_button.grid(row = 3, column = 0, columnspan = 2) 
    delete_button = Button(root, text = "Delete Passwords", command = db.clear_database)
    delete_button.grid(row = 4, column = 0, columnspan = 2) 

    root.mainloop()
    db.connect.close()
    
if __name__ == "__main__":
    main()  