from database import Database
from windows import MainWindow
from PyQt6.QtWidgets import QApplication

def main():
    db = Database()
    db.create_database()

    # Create a Qt application
    app = QApplication([])

    # Create and show the main window
    window = MainWindow(db)
    window.show()

    # Run the application
    app.exec()
    db.connect.close()

if __name__ == "__main__":
    main()  