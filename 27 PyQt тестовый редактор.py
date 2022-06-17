#базовый минимальный код (для создания окна)
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    # конструктор
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Редактор кода")
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys

class Window(QMainWindow):
    # конструктор
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Редактор кода")
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        # создадим вкладку "Файл"
        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction('Открыть', self.action_clicked)
        fileMenu.addAction('Сохранить', self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender() #sender() получаем всю инфу обьекта (на который нажали)
        if action.text() == "Открыть":
            fname = QFileDialog.getOpenFileName(self)[0]

            try:
                f = open(fname, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)

                f.close()
            except FileNotFoundError:
                print("Файл не найден")

        elif action.text() == "Сохранить":
            fname = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(fname, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("Файл не найден")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()