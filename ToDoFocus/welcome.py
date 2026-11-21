from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QWidget
from main_window import MainWindow
from storage import save_data


class Verification(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.nextButton.clicked.connect(self.check)

    def check(self):
        if not self.lineEdit_2.text().strip() or not self.lineEdit.text().strip():
            self.error = Error(self)
            self.error.show()
            self.hide()
            return

        save_data({
            "user": {"name": self.lineEdit_2.text(), "surname": self.lineEdit.text()},
            "tasks": {}
        })

        self.hide()
        self.main_window = MainWindow(self.lineEdit_2.text(), self.lineEdit.text())
        self.main_window.show()


class Error(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        uic.loadUi('untitled_1.ui', self)
        self.errorButton.clicked.connect(self.try_again)
        self.parent_window = parent_window

    def closeEvent(self, event):
        self.parent_window.show()
        super().closeEvent(event)

    def try_again(self):
        self.close()
