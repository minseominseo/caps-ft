# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
import sys

#from Ui_Dialog import ui_testcode_03_
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_testcode_02_1 import Ui_CreateDump

class Ui_OtherWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateDump()
        self.ui.setupUi(self.window)
        OtherWindow.hide()
        self.window.show()

    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open.setGeometry(QtCore.QRect(300, 230, 80, 40))
        self.btn_open.setObjectName("btn_open")
        self.btn_open.setText("next")

        self.btn1 = QtWidgets.QPushButton(self.centralwidget)

        self.btn1.setGeometry(QtCore.QRect(300, 110, 80, 32))
        self.btn1.setObjectName("btn_open")
        self.btn1.setText("path")

        self.gtdumpc = QtWidgets.QPushButton(self.centralwidget)

        self.gtdumpc.setGeometry(QtCore.QRect(20, 60, 360, 32))
        self.gtdumpc.setObjectName("btn_open")
        self.gtdumpc.setText("Create dump file")

        self.btn3 = QtWidgets.QPushButton(self.centralwidget)

        self.btn3.setGeometry(QtCore.QRect(300, 160, 80, 32))
        self.btn3.setObjectName("btn_open")
        self.btn3.setText("path")

        self.textedit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit1.setGeometry(QtCore.QRect(20,110,270,32))
        self.textedit1.setText("Choose dump file for recover")

        self.textedit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit2.setGeometry(QtCore.QRect(20, 160, 270, 32))
        self.textedit2.setText("Choose recovery folder")

        #self.textedit3 = QtWidgets.QTextEdit(self.centralwidget)
        #self.textedit3.setGeometry(QtCore.QRect(20, 160, 270, 32))
        #self.textedit3.setText("Choose recovery folder")
        self.gtdumpc.clicked.connect(self.openWindow)
        self.btn1.clicked.connect(self.openFileNameDialog)
        #self.gtdumpc.clicked.connect(self.openFileNamesDialog)
        self.btn3.clicked.connect(self.saveFileDialog)

        #self.show()

        #self.centralwidget.setObjectName("centralwidget")
        #self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(110, 30, 371, 41))
        #font = QtGui.QFont()
        #font.setPointSize(22)
        #self.label.setFont(font)
        #self.label.setObjectName("label")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        #self.retranslateUi(OtherWindow)
        #QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        self.btn_open.setText(_translate("OtherWindow", "Open Window"))
        #OtherWindow.setWindowTitle(_translate("OtherWindow", "MainWindow"))
        #self.label.setText(_translate("OtherWindow", ""))

    def openFileNameDialog(self):
        fname = QFileDialog.getOpenFileName(self.centralwidget,caption="openfile",directory="./",filter="All Files (*)")
        self.textedit1.setText(fname[0])

    #list error
    def openFileNamesDialog(self):
        fname2 = QFileDialog.getOpenFileNames(self.centralwidget, caption="openfile", directory="./", filter="All Files (*)")
        #self.textedit2.setText(self,fname2[0])

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        working_path = QFileDialog.getExistingDirectory(self.centralwidget,"select Directory")

        self.textedit2.setText(working_path)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())

