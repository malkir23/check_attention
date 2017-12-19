# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecWindow(object):
    def setupUi(self, SecWindow):
        SecWindow.setObjectName("SecWindow")
        SecWindow.setWindowModality(QtCore.Qt.WindowModal)
        SecWindow.resize(500, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SecWindow.sizePolicy().hasHeightForWidth())
        SecWindow.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(SecWindow)
        self.label.setGeometry(QtCore.QRect(20, 43, 91, 16))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(SecWindow)
        self.name.setGeometry(QtCore.QRect(50, 40, 190, 21))
        self.name.setObjectName("name")
        self.label2 = QtWidgets.QLabel(SecWindow)
        self.label2.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label2.setObjectName("label2")
        self.combobox = QtWidgets.QComboBox(SecWindow)
        self.combobox.move(50, 70)
        self.combobox.addItems(['Жен.', 'Мужч.'])
        self.combobox.setObjectName("combobox")
        self.priem = QtWidgets.QPushButton(SecWindow)
        self.priem.setGeometry(QtCore.QRect(250, 160, 113, 32))
        self.priem.setObjectName("priem")
        self.otmena = QtWidgets.QPushButton(SecWindow)
        self.otmena.setGeometry(QtCore.QRect(380, 160, 113, 32))
        self.otmena.setObjectName("otmena")

        self.retranslateUi(SecWindow)
        self.otmena.clicked.connect(SecWindow.close)
        QtCore.QMetaObject.connectSlotsByName(SecWindow)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))

    def retranslateUi(self, SecWindow):
        _translate = QtCore.QCoreApplication.translate
        SecWindow.setWindowTitle(_translate("SecWindow", "Анкета учасника"))
        self.label.setText(_translate("SecWindow", "Имя"))
        self.label2.setText(_translate("SecWindow", "Пол"))
        self.priem.setText(_translate("SecWindow", "Готово"))
        self.otmena.setText(_translate("SecWindow", "Отмена"))
