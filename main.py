from PyQt5.QtWidgets import QApplication, QMainWindow ,QTableWidgetItem,QDialog
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtMultimedia,QtCore,uic
import sys
import cv2
import os
from menu import Ui_MainWindow 
from operation import Ui_Op as OpDlg
from register import Ui_Rg as RgDlg
from login import Ui_Lg as LgDlg

class MainClass(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        lg = LoginDlg(self)
        lg.exec()
        sys.exit(app)
    

class LoginDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = LgDlg()
        self.ui.setupUi(self)
        self.ui.registerOpen.clicked.connect(self.openRg)
        self.ui.loginButton.clicked.connect(self.openMenu)

    def openRg(self):
        rg = RegisterDlg(self)
        rg.exec()
    
    def openMenu(self):
        mw = MenuDlg(self)
        mw.show()
        

class RegisterDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = RgDlg()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.openMenu)
    
    def openMenu(self):
        mw = MenuDlg(self)
        mw.show()

class OperationDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = OpDlg()
        self.ui.setupUi(self)

class MenuDlg(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpera_o.triggered.connect(self.openOperation)
        self.ui.startDrone.clicked.connect(self.initCamera)
    
    def initCamera(self):
        self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.ui.camera)
        fileName = "petroleomar.avi"
        url = QtCore.QUrl.fromLocalFile(fileName)
        self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(url))
        self.mediaPlayer.play()
    
    def openOperation(self):
        op = OperationDlg(self)
        op.exec()

if __name__ == '__main__':  
    app = QApplication(sys.argv)
    wMain=MainClass()
    sys.exit(app.exec())