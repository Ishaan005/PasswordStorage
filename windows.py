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

    def view_passwords(self):
        # Implement this function
        self.view = PasswordEntry(self.db.query_database())
        self.view.show()

class ViewWindow(QWidget):
    def __init__(self, passwords):
        super().__init__()
        self.passwords = passwords
        self.setWindowTitle("Your Passwords")

        main_layout = QVBoxLayout()

        for name, password in self.passwords:
            layout = QHBoxLayout()
            layout.addWidget(QLabel(name))
            layout.addWidget(QLabel(password))

            self.edit_button = QPushButton("Edit")
            #self.edit_button.clicked.connect()
            layout.addWidget(self.edit_button)

            delete_button = QPushButton("Delete")
            layout.addWidget(delete_button)

            group_box = QGroupBox()
            group_box.setLayout(layout)

            main_layout.addWidget(group_box)

        self.setLayout(main_layout)

class PasswordEntry(QWidget):
    def __init__(self, passwords):
        super().__init__()

        self.passwords = passwords

        self.setWindowTitle("Password Entry")

        self.layout = QVBoxLayout()


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
            self.view = ViewWindow(passwords=self.passwords)
            self.view.show()
            self.close()
            return True
        else:
            self.prompt.setText("Incorrect password")
            return False

 
        

        