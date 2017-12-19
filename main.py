# -*- coding: utf-8 -*-
import sys
import datetime
import random
from form1 import *
from form2 import *
from real import test_word, next_test
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import openpyxl

exel = []


class Anketa(QtWidgets.QMainWindow):
    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_SecWindow()
        self.ui.setupUi(self)
        self.ui.priem.clicked.connect(self.next)
        self.ui.otmena.clicked.connect(self.close)

    def next(self):
        global exel
        name = self.ui.name.text()
        combobox = self.ui.combobox.currentText()
        exel += [[name, combobox]]
        Anketa.close(self)
        self.window = Window()
        self.window.show()


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.procent = 0
        self.step = 25
        self.begin_time = 0
        self.color = ''
        self.type = 'Test'
        self.name_type = {'pts': 0, 'dictator': 0, 'x': 0}

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_yellow.clicked.connect(self.yellow)
        self.ui.pushButton_red.clicked.connect(self.red)
        self.ui.pushButton_blue.clicked.connect(self.blue)
        self.ui.pushButton_green.clicked.connect(self.green)
        self.ui.pushButton_purple.clicked.connect(self.purple)

        self.botton_off(False)
        buttonReply = QtWidgets.QMessageBox.question(self, 'Внимание!', "Сейчас несколько раз нужно выбрать првильный цвет слова", QtWidgets.QMessageBox.Ok)
        if buttonReply == QtWidgets.QMessageBox.Ok:
            self.game_word()

    def botton_off(self, switch):
        self.ui.pushButton_yellow.setEnabled(switch)
        self.ui.pushButton_red.setEnabled(switch)
        self.ui.pushButton_blue.setEnabled(switch)
        self.ui.pushButton_green.setEnabled(switch)
        self.ui.pushButton_purple.setEnabled(switch)
        if switch is True:
            self.begin_time = datetime.datetime.now()

    def proc(self):
        self.procent += self.step
        self.ui.progressBar.setProperty("value", self.procent)
        if self.procent > 97:
            self.ui.progressBar.setProperty("value", 100)
            if self.type != 'Test':
                global exel
                data = openpyxl.load_workbook('Result.xlsx')
                lines = data.active
                for row in exel:
                    lines.append(row)
                data.save("Result.xlsx")
                buttonReply = QtWidgets.QMessageBox.question(self, 'Поздравляем!', "Тест окончен, Спасибо вам!", QtWidgets.QMessageBox.Ok)
                if buttonReply == QtWidgets.QMessageBox.Ok:
                    sys.exit(app.exec_())
            else:
                buttonReply = QtWidgets.QMessageBox.question(self, 'Внимание!', "Сейчас нужно выбрать првильный цвет второго слова", QtWidgets.QMessageBox.Ok)
                if buttonReply == QtWidgets.QMessageBox.Ok:
                    self.procent = 0
                    self.begin_time = 0
                    self.step = 3.7
                    self.color = ''
                    self.type = 'No test'
                    self.ui.progressBar.setProperty("value", 0)
                else:
                    sys.exit(app.exec_())

    def game_word(self):
        timer = 500 + (random.randint(1, 4) * 1000)
        if self.type == 'Test':
            result = test_word(self.color)
            self.botton_off(True)
        else:
            name, iteral = random.choice(list(self.name_type.items()))
            result = next_test(name, self.color)
            self.type = name
            self.name_type[name] += 1
            if self.name_type[name] >= 9:
                self.name_type.pop(name)
        color = result[1]
        word = result[0]
        self.message(word, color)
        self.color = color
        if self.type != 'Test':
            result = next_test(name, self.color)
            QtCore.QTimer.singleShot(500, partial(self.message, '', 'white'))
            color = result[1]
            word = result[0]
            self.color = color
            QtCore.QTimer.singleShot(timer, partial(self.message, word, color))
            QtCore.QTimer.singleShot(timer, partial(self.botton_off, True))

    def message(self, word, color):
        self.ui.textBrowser.setStyleSheet("QTextEdit {color:" + color + "}")
        self.ui.textBrowser.setText(word)

    def prosec(self, color):
        self.botton_off(False)
        if self.type != 'Test':
            global exel
            timer = (datetime.datetime.now() - self.begin_time).total_seconds()
            if self.color == color:
                exel.append(['', '', self.type, 'Правильно', timer])
            else:
                exel.append(['', '', self.type, 'Не правильно', timer])
        self.proc()
        self.game_word()

    def yellow(self):
        self.prosec('yellow')

    def red(self):
        self.prosec('red')

    def blue(self):
        self.prosec('blue')

    def green(self):
        self.prosec('green')

    def purple(self):
        self.prosec('purple')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Anketa()
    myapp.show()
    sys.exit(app.exec_())
