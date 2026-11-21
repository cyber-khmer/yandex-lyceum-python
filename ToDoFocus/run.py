import sys
from PyQt6.QtWidgets import QApplication
from welcome import Verification
from storage import load_data
from main_window import MainWindow


app = QApplication(sys.argv)

with open("style.qss", "r", encoding="utf-8") as f:
    app.setStyleSheet(f.read())

data = load_data()
if data and 'user' in data:
    name = data['user']['name']
    surname = data['user']['surname']

    window = MainWindow(name, surname)
else:
    window = Verification()

window.show()
sys.exit(app.exec())
