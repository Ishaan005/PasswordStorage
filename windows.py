from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()

        self.setWindowTitle("Password Manager")

        self.db = db

        # Create widgets
        self.name_label = QLabel("Name: ")
        self.password_label = QLabel("Password: ")
        self.name_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.add_button = QPushButton("Add Password")
        self.view_button = QPushButton("View Passwords")
        self.delete_button = QPushButton("Delete Passwords")

        # Connect buttons to functions
        self.add_button.clicked.connect(self.add_password)
        self.view_button.clicked.connect(self.view_passwords)
        self.delete_button.clicked.connect(self.db.clear_database)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.add_button)
        layout.addWidget(self.view_button)
        layout.addWidget(self.delete_button)

        # Set the layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def add_password(self):
        self.db.add_password(self.name_entry.text(), self.password_entry.text())

    #View Password#
    def view_passwords(self):
        """self.view = PasswordEntry(self.db)
        self.view.show()"""

        self.password_entry_window = PasswordEntry(self.show_view_window)
        self.password_entry_window.show()

    def show_view_window(self):
        self.view = ViewWindow(self.db)
        self.view.show()
    #View Password - End#

class ViewWindow(QWidget):
    def __init__(self, db):
        super().__init__()

        self.db = db
        self.passwords = self.db.query_database()

        self.setWindowTitle("Your Passwords")

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.populate_passwords()

    def populate_passwords(self):
        for i in reversed(range(self.main_layout.count())):
            self.widgetToRemove = self.main_layout.itemAt(i).widget()
            self.main_layout.removeWidget(self.widgetToRemove)
            self.widgetToRemove.setParent(None)

        for name, password in self.passwords:
            layout = QHBoxLayout()
            layout.addWidget(QLabel(name))
            layout.addWidget(QLabel(password))

            self.edit_window = EditWindow(self.db, name, self)
            self.edit_button = QPushButton("Edit")
            self.edit_button.clicked.connect(self.edit_window.show)
            layout.addWidget(self.edit_button)
            self.edit_window.close()

            self.delete_button = QPushButton("Delete")
            self.delete_button.clicked.connect(lambda: self.delete_password(name, password))
            layout.addWidget(self.delete_button)

            group_box = QGroupBox()
            group_box.setLayout(layout)

            self.main_layout.addWidget(group_box)

    def refresh(self):
        self.passwords = self.db.query_database()
        self.populate_passwords()

    def delete_password(self, name, password):
        self.db.delete_password(name, password)
        self.refresh()
        

class EditWindow(QWidget):
    def __init__(self, db, name, view_window):
        super().__init__()

        self.db = db
        self.name = name
        self.view_window = view_window

        self.setWindowTitle("Edit Password")

        self.layout = QVBoxLayout()

        self.prompt = QLabel("Enter your new password: ")
        self.new_password_entry = QLineEdit()
        self.enter_button = QPushButton("Enter")

        self.enter_button.clicked.connect(self.edit_password)

        self.layout.addWidget(self.prompt)
        self.layout.addWidget(self.new_password_entry)
        self.layout.addWidget(self.enter_button)

        self.setLayout(self.layout)

    def edit_password(self):
        self.db.edit_password(self.name, self.new_password_entry.text())
        self.view_window.refresh()

class PasswordEntry(QWidget):
    def __init__(self, on_correct_password):
        super().__init__()

        self.setWindowTitle("Password Entry")

        self.layout = QVBoxLayout()

        self.on_correct_password = on_correct_password

        self.prompt = QLabel("Enter your password: ")
        self.password_entry = QLineEdit()  
        self.enter_button = QPushButton("Enter")

        self.enter_button.clicked.connect(self.give_access)

        self.layout.addWidget(self.prompt)
        self.layout.addWidget(self.password_entry)
        self.layout.addWidget(self.enter_button)

        self.setLayout(self.layout)


    def give_access(self):
        password = "1234"
        if self.password_entry.text() == password:
            self.prompt.setText("Correct password")
            self.on_correct_password()
            self.close()
            return True
        else:
            self.prompt.setText("Incorrect password")
            return False

 
        

        