from PyQt6.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox, QLabel
from PyQt6.QtCore import Qt, QTimer, QDateTime
from PyQt6.QtGui import QColor, QIcon, QShortcut, QKeySequence, QPixmap
from PyQt6 import uic
from storage import load_data, save_data
from time_dialog import TimeDialog


class MainWindow(QMainWindow):
    def __init__(self, name, surname):
        super().__init__()
        uic.loadUi('head.ui', self)

        self.data = load_data()
        if self.data:
            self.all_tasks = self.data.get('tasks', {})
        else:
            self.all_tasks = {}

        self.name = name
        self.surname = surname
        self.date = None

        self.pushButton.setIcon(QIcon("icons/plus.svg"))
        self.pushButton.setText("")
        self.pushButton_2.setIcon(QIcon("icons/trash.svg"))
        self.pushButton_2.setText("")
        self.shortcut_delete = QShortcut(QKeySequence(Qt.Key.Key_Delete), self)

        self.empty_label = QLabel(self.listWidget)
        self.empty_label.setPixmap(QPixmap("icons/no_tasks.jpeg"))
        self.empty_label.setScaledContents(True)  # Растягиваем картинку под размер
        self.empty_label.setFixedSize(300, 300)  # Фиксируем размер (чтобы не была гигантской)
        self.empty_label.hide()

        self.label.setText(f'Привет {name} {surname}!')
        self.calendarWidget.selectionChanged.connect(self.choice_date)
        self.pushButton.clicked.connect(self.add_tasks_storage)
        self.pushButton_2.clicked.connect(self.delete_task)
        self.lineEdit.returnPressed.connect(self.add_tasks_storage)
        self.listWidget.itemChanged.connect(self.on_item_changed)
        self.shortcut_delete.activated.connect(self.delete_task)

        self.reminder_timer = QTimer(self)
        self.reminder_timer.timeout.connect(self.check_reminders)
        self.reminder_timer.start(30000)
        self.reminded_tasks = set()

        self.choice_date()

    def choice_date(self):
        self.listWidget.blockSignals(True)

        self.date = self.calendarWidget.selectedDate().toString("dd.MM.yyyy")

        if self.date not in self.all_tasks.keys():
            self.all_tasks[self.date] = []

        self.label_3.setText(f'Задачи на {self.date}:')
        self.listWidget.clear()

        tasks = self.all_tasks[self.date]
        for i, task in enumerate(tasks, start=1):
            time_prefix = f"[{task.get('time')}] " if task.get('time') else ""
            item = QListWidgetItem(f"{i}. {task['text']} {time_prefix}")
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)

            if task['done']:
                item.setCheckState(Qt.CheckState.Checked)
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)
                item.setForeground(QColor("#a6e3a1"))
            else:
                item.setCheckState(Qt.CheckState.Unchecked)

            self.listWidget.addItem(item)

        self.listWidget.blockSignals(False)

        if len(tasks) == 0:
            self.empty_label.show()
            QTimer.singleShot(0, self.center_empty_label)
        else:
            self.empty_label.hide()

    def center_empty_label(self):
        x = (self.listWidget.width() - self.empty_label.width()) // 2
        y = (self.listWidget.height() - self.empty_label.height()) // 2
        self.empty_label.move(x, y)

    def add_tasks_storage(self):
        text = self.lineEdit.text().strip()
        if not text:
            return

        dialog = TimeDialog(self)
        if dialog.exec(): # запуск цикла если True пишем данные иначе не пишем пропускаем
            self.all_tasks[self.date].append({
                'text': text,
                'done': False,
                'time': dialog.selected_time
            })
            self.lineEdit.clear()
            self.choice_date()
            self.save_all()

    def on_item_changed(self, item):
        self.listWidget.blockSignals(True)
        row = self.listWidget.row(item)

        if item.checkState() == Qt.CheckState.Checked:
            self.all_tasks[self.date][row]['done'] = True
        else:
            self.all_tasks[self.date][row]['done'] = False

        self.listWidget.blockSignals(False)
        self.choice_date()
        self.save_all()

    def check_reminders(self):
        current_date = QDateTime.currentDateTime().toString("dd.MM.yyyy")
        current_time = QDateTime.currentDateTime().toString("HH:mm")

        tasks = self.all_tasks.get(current_date, [])

        for task in tasks:
            if task.get('time') == current_time and not task['done']:
                task_id = f"{current_date}_{task['text']}_{current_time}"
                if task_id not in self.reminded_tasks:
                    self.reminded_tasks.add(task_id)
                    QMessageBox.information(self, "Напоминание", f"Пора выполнить: {task['text']}")

    def delete_task(self):
        row = self.listWidget.currentRow()
        if row == -1:
            return

        self.all_tasks[self.date].pop(row)
        self.choice_date()
        self.save_all()

    def save_all(self):
        save_data({"user": {"name": self.name, "surname": self.surname}, "tasks": self.all_tasks})
