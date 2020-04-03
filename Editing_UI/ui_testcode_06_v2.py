import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic

from ui_testcode_02 import Ui_OtherWindow
from get_file_content import read_result_string
from get_file_content import read_result_num
import os
#from get_file_content import str_line,number_re

form_class = uic.loadUiType("../UI/06_finish_recover_file.ui")[0]



class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back_btn_clicked)
        self.exit_btn.clicked.connect(self.exit_btn_clicked)

        str_line = read_result_string()
        number_re = read_result_num()

        self.num_list.setText( number_re)
        text =QListWidgetItem()
        text.setText(str_line)
        self.list_signature.addItem(text)


    def exit_btn_clicked(self):
        os.remove('./recover_list.tmp')
        sys.exit()


    def back_btn_clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        window.hide()
        self.window.show()
   



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()