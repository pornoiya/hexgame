from PyQt5.QtWidgets import (QAbstractItemView, QTableWidgetItem, QWidget, QLineEdit, QInputDialog)
import datetime


class UserName(QWidget):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        self.show_dialog()

    def show_dialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.line_edit.setText(str(text))


class Table:
    @staticmethod
    def fill_table(tableWidget):
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tableWidget.setWindowTitle('Table of Records')
        tableWidget.resize(344, 500)
        tableWidget.move(300, 300)
        tableWidget.setRowCount(10)
        tableWidget.setColumnCount(2)
        tableWidget.setHorizontalHeaderLabels(('Name', 'Time'))
        with open('records.txt') as r:
            lines = r.readlines()[0:10]
        for row in range(0, 10):
            for col in range(0, 2):
                tableWidget.setItem(row, col, QTableWidgetItem(lines[row].split(' ')[col]))
                tableWidget.setItem(row, 1, QTableWidgetItem(str(datetime.timedelta(seconds=int(lines[row].split(' ')[1])))))
        tableWidget.show()

