from database import Database
from windows import MainWindow
from PyQt6.QtWidgets import QApplication

def main():
    db = Database()
    db.create_database()

    # Create a Qt application
    app = QApplication([])

    css = """
        QWidget {
            font-size: 14px;
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            cursor: pointer;
        }
        QPushButton:hover {
            background-color: white; 
            color: black; 
            border: 2px solid #4CAF50;
        }
        QLabel {
            color: #333;
        }
    """

    # Apply the CSS
    app.setStyleSheet(css)

    # Create and show the main window
    window = MainWindow(db)
    window.show()

    # Run the application
    app.exec()
    db.connect.close()

if __name__ == "__main__":
    main()  