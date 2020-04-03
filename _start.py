import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit


from PyQt5 import uic

# from .UI_py import _01_main
# from .UI_py import _02_choose_dump
# from .UI_py import _03_cant_use_dump
# from .UI_py import _04_dump_complete
# from .UI_py import _05_select_file_type
# from .UI_py import _05_select_file_type_2
# from .UI_py import _06_finish_recover_file


class Form(QtWidgets.QDialog):
#this will be the base layer of the screen
#
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("01_main.ui")
        self.ui.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
