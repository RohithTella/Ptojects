import sys,mydpi
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QDialog
from LOGIN import Ui_Form
from dialogF import Ui_Dialog
from pageN import Ui_MainWindow

class NoteP():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.login)
        self.ui.btn_login.clicked.connect(self.loginp)
        self.ui.frame.keyPressEvent = self.loginPK
        self.login.show()
        self.app.exec_()


    def loginPK(self, e):
        if e.key() == Qt.Key_Return:
            self.loginp()

    def loginp(self):
        user_ = self.ui.userline.text()
        pass_ = self.ui.passline.text()
        if (user_ != "") & (pass_ != ""):
            if (user_ =='Rohith') & (pass_=='130359'):
                print("Login")
                # print(user_+'\n'+pass_)
                self.PageNotePad()
            else:
                print('Error login')
                # self.ui.userline.setText('')
                self.ui.passline.setText('')
                Dialog_Error()
        else:
            print('Not Empty Field')
            Dialog_Error()

    def PageNotePad(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupU(self.window)
        self.window.show()
        self.login.hide()

class Dialog_Error():
    def __init__(self):
        dialog = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(dialog)
        dialog.show()
        res = dialog.exec_()
        if res == QDialog.Accepted:
            print('Ok')
            NoteP.loginp
        else:
            print('cancel')
            sys.exit()


if __name__ =='__main__':
    ex = NoteP()