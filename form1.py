# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_yellow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_yellow.setGeometry(QtCore.QRect(270, 390, 75, 23))
        self.pushButton_yellow.setObjectName("pushButton_yellow")
        self.pushButton_red = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_red.setGeometry(QtCore.QRect(470, 390, 75, 23))
        self.pushButton_red.setObjectName("pushButton_red")
        self.pushButton_blue = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_blue.setGeometry(QtCore.QRect(570, 390, 75, 23))
        self.pushButton_blue.setObjectName("pushButton_blue")
        self.pushButton_green = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_green.setGeometry(QtCore.QRect(170, 390, 75, 23))
        self.pushButton_green.setObjectName("pushButton_green")
        self.pushButton_purple = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_purple.setGeometry(QtCore.QRect(370, 390, 75, 23))
        self.pushButton_purple.setObjectName("pushButton_purple")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 110, 650, 192))
        self.textBrowser.setObjectName("textBrowser")
        font = QtGui.QFont()
        font.setPointSize(80)
        self.textBrowser.setFont(font)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(250, 10, 318, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 330, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 50, 731, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.created = QtWidgets.QLabel(MainWindow)
        self.created.setGeometry(QtCore.QRect(600, 450, 210, 80))
        self.created.setText("Created by Averianov K. vs Anchutkin S.")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тест"))
        self.pushButton_yellow.setText(_translate("MainWindow", "Желтый"))
        self.pushButton_red.setText(_translate("MainWindow", "Красный"))
        self.pushButton_blue.setText(_translate("MainWindow", "Синий"))
        self.pushButton_green.setText(_translate("MainWindow", "Зеленый"))
        self.pushButton_purple.setText(_translate("MainWindow", "Фиолетовый"))