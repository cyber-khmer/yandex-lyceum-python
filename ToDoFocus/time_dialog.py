from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTimeEdit
from PyQt6.QtCore import QTime, Qt


class TimeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Время напоминания")
        self.setFixedSize(280, 160)
        self.selected_time = None

        layout = QVBoxLayout()

        label = QLabel("Во сколько напомнить?")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QTime.currentTime())

        buttons_layout = QHBoxLayout()

        btn_ok = QPushButton("ОК")
        btn_skip = QPushButton("Пропустить")

        btn_ok.clicked.connect(self.accept_time)
        btn_skip.clicked.connect(self.skip_time)

        buttons_layout.addWidget(btn_ok)
        buttons_layout.addWidget(btn_skip)

        layout.addWidget(label)
        layout.addWidget(self.time_edit)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def accept_time(self):
        self.selected_time = self.time_edit.time().toString("HH:mm")
        self.accept()

    def skip_time(self):
        self.selected_time = None
        self.accept()
