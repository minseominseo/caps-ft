# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '06_finish_recover_file.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(15)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 141, 51))
        self.label.setObjectName("label")
        self.list_signature = QtWidgets.QListView(Dialog)
        self.list_signature.setGeometry(QtCore.QRect(20, 60, 271, 171))
        self.list_signature.setObjectName("list_signature")
        self.back_btn = QtWidgets.QPushButton(Dialog)
        self.back_btn.setGeometry(QtCore.QRect(240, 260, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.exit_btn = QtWidgets.QPushButton(Dialog)
        self.exit_btn.setGeometry(QtCore.QRect(320, 260, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 240, 141, 51))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Recover Start!!"))
        self.back_btn.setText(_translate("Dialog", "back"))
        self.exit_btn.setText(_translate("Dialog", "exit"))
        self.label_2.setText(_translate("Dialog", "Recover Finish!!"))

