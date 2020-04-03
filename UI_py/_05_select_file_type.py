# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '05_select_file_type.ui'
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
        self.label.setGeometry(QtCore.QRect(10, 20, 261, 51))
        self.label.setObjectName("label")
        self.list_signature = QtWidgets.QListView(Dialog)
        self.list_signature.setGeometry(QtCore.QRect(20, 80, 256, 192))
        self.list_signature.setObjectName("list_signature")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(318, 250, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.signature_input_2 = QtWidgets.QTextEdit(Dialog)
        self.signature_input_2.setGeometry(QtCore.QRect(290, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signature_input_2.setFont(font)
        self.signature_input_2.setObjectName("signature_input_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(280, 30, 113, 25))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Please enter the file type   :"))
        self.pushButton.setText(_translate("Dialog", "back"))

