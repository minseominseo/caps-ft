import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
from cDump import cDump_func

#from ui_testcode_02 import Ui_OtherWindow
fname=' '
working_path=' '

class Ui_CreateDump(object):

 #    def openWindow(self):
  #       self.window1 = QtWidgets.QMainWindow()
   #      self.ui = Ui_OtherWindow
    #     self.ui.setupUi(self.window1)
     #    CreateDump.hide()
      #   self.window1.show()


    def setupUi(self, CreateDump):
        CreateDump.setObjectName("CreateDump")
        CreateDump.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(CreateDump)
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open.setGeometry(QtCore.QRect(300, 230, 80, 40))
        self.btn_open.setObjectName("btn_open")
        self.btn_open.setText("next")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setText("*** Craete dump file ***")
        self.label2.setGeometry(QtCore.QRect(110, 30, 211, 41))


        self.btn1 = QtWidgets.QPushButton(self.centralwidget)

        self.btn1.setGeometry(QtCore.QRect(300, 110, 80, 32))
        self.btn1.setObjectName("btn_open")
        self.btn1.setText("path")

        self.CreDum = QtWidgets.QPushButton(self.centralwidget)

        self.CreDum.setGeometry(QtCore.QRect(20, 230, 180, 40))
        self.CreDum.setObjectName("btn_open")
        self.CreDum.setText("Create dump")

        self.btn3 = QtWidgets.QPushButton(self.centralwidget)

        self.btn3.setGeometry(QtCore.QRect(300, 160, 80, 32))
        self.btn3.setObjectName("btn_open")
        self.btn3.setText("path")

        self.textedit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit1.setGeometry(QtCore.QRect(20,110,270,32))
        self.textedit1.setText("Choose disk")



        self.textedit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit2.setGeometry(QtCore.QRect(20, 160, 270, 32))
        self.textedit2.setText("Choose recovery folder")

   #      self.textedit3 = QtWidgets.QTextEdit(self.centralwidget)
   #     self.textedit3.setGeometry(QtCore.QRect(20, 160, 270, 32))
   #     self.textedit3.setText("Choose recovery folder")

        self.btn1.clicked.connect(self.openFileNameDialog)
        self.CreDum.clicked.connect(self.gotoCreateDump)
        self.btn3.clicked.connect(self.saveFileDialog)

#        self.show()

        #self.centralwidget.setObjectName("centralwidget")
        #self.label = QtWidgets.QLabel(self.centralwidget)
       # self.label.setGeometry(QtCore.QRect(110, 30, 371, 41))
       # font = QtGui.QFont()
        #font.setPointSize(22)
        #self.label.setFont(font)
       # self.label.setObjectName("label")
        CreateDump.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CreateDump)
        self.statusbar.setObjectName("statusbar")
        CreateDump.setStatusBar(self.statusbar)



    def retranslateUi(self, CreateDump):
        _translate = QtCore.QCoreApplication.translate
        self.btn_open.setText(_translate("CreateDump", "Open Window"))


    def openFileNameDialog(self):
        fname = QFileDialog.getOpenFileName(self.centralwidget, caption="openfile", directory="/dev/",
                                            filter="All Files (*)")
        self.textedit1.setText(fname[0])


    #list error
    def gotoCreateDump(self,fname,working_path):
        cDump_func.command_dd(fname,working_path)


    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        working_path = QFileDialog.getExistingDirectory(self.centralwidget,"select Directory")

        self.textedit2.setText(working_path)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateDump = QtWidgets.QMainWindow()
    ui = Ui_CreateDump()
    ui.setupUi(CreateDump)
    CreateDump.show()
    sys.exit(app.exec_())