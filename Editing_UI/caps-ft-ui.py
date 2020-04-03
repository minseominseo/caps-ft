import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic

from recover_deleted_file import recover_file
from get_file_content import read_result_string
from get_file_content import read_result_num

form_class_05 = uic.loadUiType("../UI/05_select_file_type_2.ui")[0]
form_class_06 = uic.loadUiType("../UI/06_finish_recover_file.ui")[0]

class UI_startWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_secondWindow()
        self.ui.setupUi(self.window)
        window_01.hide()
        self.window.show()
        
        #window_02 = QtWidgets.QMainWindow()
        #ui_02 = Ui_secondWindow()
        #ui_02.setupUi(window_02)
        #print("am i Happenig???")
        #window_02.show()
        #print("am i Happenig???????")
        #window_01.hide()
        
    def setupUi(self, window_01):
        window_01.setObjectName("window_01")
        window_01.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(window_01)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(20, 230, 360, 40))
        self.btn_open.setObjectName("btn_open")

        self.btn_open.clicked.connect(self.openWindow)
    
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setText("* Warning!")
        self.label2.setGeometry(QtCore.QRect(40, 100, 211, 41))

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setText("* It may not be fully recovered.")
        self.label3.setGeometry(QtCore.QRect(40, 120, 211, 41))

        window_01.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(window_01)
        self.statusbar.setObjectName("statusbar")
        window_01.setStatusBar(self.statusbar)

        self.retranslateUi(window_01)
        QtCore.QMetaObject.connectSlotsByName(window_01)

    def retranslateUi(self, window_01):
        _translate = QtCore.QCoreApplication.translate
        window_01.setWindowTitle(_translate("window_01", "window_01"))
        self.btn_open.setText(_translate("window_01", "Open Window"))
        self.label.setText(_translate("window_01", "FT Carving"))


class Ui_secondWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateDump()
        self.ui.setupUi(self.window)
        window_02.hide()
        self.window.show()
        
    def opneNextWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window_05()
        self.setupUi(self.window)
        window_02.hide()
        self.window.show()

    def setupUi(self, window_02):
        window_02.setObjectName("window_02")
        window_02.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(window_02)
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
        self.btn_open.clicked.connect(self.opneNextWindow)

        #self.show()

        #self.centralwidget.setObjectName("centralwidget")
        #self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(110, 30, 371, 41))
        #font = QtGui.QFont()
        #font.setPointSize(22)
        #self.label.setFont(font)
        #self.label.setObjectName("label")
        window_02.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(window_02)
        self.statusbar.setObjectName("statusbar")
        window_02.setStatusBar(self.statusbar)

        #self.retranslateUi(OtherWindow)
        #QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, window_02):
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


class Ui_Window_05(QMainWindow, form_class_05):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.backButton_clicked)
        self.startButton.clicked.connect(self.startButton_clicked)
        qsig_list = [".jpeg", ".png", ".pdf", ".gif", ".mpg", ".vob"]
        self.sig_list.addItems(qsig_list)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(15)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 110, 261, 51))
        self.label.setObjectName("label")

        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(300, 250, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.startButton_clicked)

        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setGeometry(QtCore.QRect(40, 250, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.backButton_clicked)

        self.sig_list = QtWidgets.QComboBox(Dialog)
        self.sig_list.setGeometry(QtCore.QRect(290, 130, 86, 25))
        self.sig_list.setObjectName("sig_list")
        qsig_list = [".jpeg", ".png", ".pdf", ".gif", ".mpg", ".vob"]
        self.sig_list.addItems(qsig_list)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Please select the file type   :"))
        self.backButton.setText(_translate("Dialog", "back"))
        self.startButton.setText(_translate("Dialog", "start"))

    def backButton_clicked(self):
        #self.window = QtWidgets.QMainWindow()
        #self.ui = Ui_OtherWindow()
        #self.ui.setupUi(self.window)
        #window.hide()
        #self.window.show()
        window_02 = QtWidgets.QMainWindow()
        ui_02 = Ui_secondWindow()
        ui_02.setupUi(window_02)
        self.window.hide()
        window_02.show()

    def startButton_clicked(self):
        sigValue = self.sig_list.currentText()
        sigHeader = {".jpeg":"jpeg", ".png":"png", ".pdf":"pdf", ".gif":"gif", ".mpg":"mpg", ".vob":"vob"}

        #r_file = recover_file(sigHeader[sigValue], dump_path, recovery_path)
        r_file = recover_file(sigHeader[sigValue])
        r_file.start_recovery()
        
        #problem:
        #start_recovery is no done properly --> resolved!
        #window no 6 is not opening --> resolved!
        print('i am doing my work!!')

        #self.window = QtWidgets.QMainWindow()
        #self.ui = MyWindow()
        #self.ui.setupUi(self.window)
        #window.hide()
        #self.window.show()
        window_06 = QtWidgets.QMainWindow()
        ui_06 = Ui_secondWindow()
        ui_06.setupUi(window_06)
        self.window.hide()
        window_06.show()


class Ui_Window_06(QMainWindow, form_class_06):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back_btn_clicked)
        self.exit_btn.clicked.connect(self.exit_btn_clicked)

        str_line = read_result_string()
        number_re = read_result_num()

        self.num_list.setText( number_re)
        text = QListWidgetItem()
        text.setText(str_line)
        self.list_signature.addItem(text)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(15)
        Dialog.setFont(font)
        #back_btn
        self.back_btn = QtWidgets.QPushButton(Dialog)
        self.back_btn.setGeometry(QtCore.QRect(240, 230, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(self.back_btn_clicked)
        #exit_btn
        self.exit_btn = QtWidgets.QPushButton(Dialog)
        self.exit_btn.setGeometry(QtCore.QRect(320, 230, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(self.exit_btn_clicked)
        #num_list
        self.num_list = QtWidgets.QLabel(Dialog)
        self.num_list.setGeometry(QtCore.QRect(260, 30, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.num_list.setFont(font)
        self.num_list.setObjectName("num_list")
        #label_3
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        #label_4
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(260, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        #label_5
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        #label_6
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(260, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        #list_signature
        self.list_signature = QtWidgets.QListWidget(Dialog)
        self.list_signature.setGeometry(QtCore.QRect(10, 30, 221, 241))
        self.list_signature.setObjectName("list_signature")

        str_line = read_result_string()
        number_re = read_result_num()
        self.num_list.setText( number_re)
        text =QListWidgetItem()
        text.setText(str_line)
        self.list_signature.addItem(text)

        #retranslateUi
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.back_btn.setText(_translate("Dialog", "recover"))
        self.exit_btn.setText(_translate("Dialog", "exit"))
        self.num_list.setText(_translate("Dialog", "12"))
        self.label_3.setText(_translate("Dialog", " FILES "))
        self.label_4.setText(_translate("Dialog", "RECOVERED"))
        self.label_5.setText(_translate("Dialog", "Continue?"))
        self.label_6.setText(_translate("Dialog", "FINISH!!"))


    def exit_btn_clicked(self):
        os.remove('./recover_list.tmp')
        sys.exit()

    def back_btn_clicked(self):
        #self.window = QtWidgets.QMainWindow()
        #self.ui = Ui_OtherWindow()
        #self.ui.setupUi(self.window)
        #window.hide()
        #self.window.show()
        window_05 = QtWidgets.QMainWindow()
        ui_05 = Ui_secondWindow()
        ui_05.setupUi(window_05)
        self.window.hide()
        window_05.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window_01 = QtWidgets.QMainWindow()
    ui_01 = UI_startWindow()
    ui_01.setupUi(window_01)

    window_02 = QtWidgets.QMainWindow()
    window_05 = QtWidgets.QMainWindow()
    window_06 = QtWidgets.QMainWindow()

    #ui_02 = Ui_secondWindow()
    #ui_05 = Ui_Window_05()
    #ui_06 = Ui_Window_06()

    #ui_02.setupUi(window_02)
    #ui_05.setupUi(window_05)
    #ui_06.setupUi(window_06)

    
    window_01.show()

    sys.exit(app.exec_())
