import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic

from ui_testcode_06_v2 import MyWindow
from ui_testcode_02 import Ui_OtherWindow

from recover_deleted_file import recover_file

form_class = uic.loadUiType("../UI/05_select_file_type_2.ui")[0]


class Window_05(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.backButton_clicked)
        self.startButton.clicked.connect(self.startButton_clicked)
        qsig_list = [".jpeg", ".png", ".pdf", ".gif", ".mpg", ".vob"]
        self.sig_list.addItems(qsig_list)

    def backButton_clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        window.hide()
        self.window.show()

    def startButton_clicked(self):
        sigValue = self.sig_list.currentText()
        sigHeader = {".jpeg":"jpeg", ".png":"png", ".pdf":"pdf", ".gif":"gif", ".mpg":"mpg", ".vob":"vob"}

        #r_file = recover_file(sigHeader[sigValue], dump_path, recovery_path)
        r_file = recover_file(sigHeader[sigValue])
        r_file.start_recovery()
        
        #problem:
        #start_recovery is no done properly
        #window no 6 is not opening
        print('am i comming back.....?')
        self.window = QtWidgets.QMainWindow()
        self.ui = MyWindow()
        self.ui.setupUi(self.window)
        window.hide()
        self.window.show()
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window_05()
    window.show()
    app.exec_()
