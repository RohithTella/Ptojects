# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, mydpi,bk_rc

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Ui_Form(object):
    def setupUi(self, Form):

        Form.setWindowFlags( QtCore.Qt.FramelessWindowHint)     ## hazfe Dokmehaie panjere X # -
        # Form.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)     ## hazfe Dokmehaie panjere X # -

        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)  ## backgrond transparent ya shafaf baray barname ,roshan,shafaf
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)   ## in khat code ba khate balaiie baray transparent kardane background barnamas
        Form.setObjectName("Form")
        Form.setWindowIcon(QIcon('src\icon.png'))
        Form.resize(320, 240)
        Form.setMinimumSize(QtCore.QSize(320, 240))
        Form.setMaximumSize(QtCore.QSize(320, 240))
        Form.setStyleSheet("QWidget{\n"
"background-color: rgb(13, 65, 57);\n"
"}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QFrame {\n"
"background-image: url(:/bg/src/LoginPage.png);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"border-color: rgb(225, 148, 255);\n"
"   border-radius: 30px;\n"
"   height: 25px;\n"
"}\n"
"QToolTip {\n"
"background-color: rgba(0, 0, 0, 0);\n"
"    border: 1px solid darkkhaki;\n"
"    border-radius: 5px;\n"
"    opacity: 0.5;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.userline = QtWidgets.QLineEdit(self.frame)
        self.userline.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.userline.setFont(font)
        self.userline.setWhatsThis("")
        self.userline.setStyleSheet("QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"Arial\";\n"
"color:#d5f931;\n"
"    border-style: solid;\n"
"    border-bottom-width: 1px;\n"
"    border-bottom-color: #55ffff;\n"
"   border-radius: 10px;\n"
"\n"
"}\n"
"")
        self.userline.setText("")
        self.userline.setAlignment(QtCore.Qt.AlignCenter)
        self.userline.setObjectName("userline")
        self.gridLayout.addWidget(self.userline, 0, 0, 1, 2)
        self.passline = QtWidgets.QLineEdit(self.frame)
        self.passline.setStyleSheet("QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"Arial\";\n"
"color:#d5f931;\n"
"    border-style: solid;\n"
"    border-bottom-width: 1px;\n"
"    border-bottom-color: #55ffff;\n"
"   border-radius: 10px;\n"
"\n"
"}\n"
"")
        self.passline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passline.setAlignment(QtCore.Qt.AlignCenter)
        self.passline.setObjectName("passline")
        self.gridLayout.addWidget(self.passline, 1, 0, 1, 2)
        self.btn_login = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px solid rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(0, 92, 67);\n"
"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 127);\n"
"border: 1px solid  #55ffff;;\n"
"border-radius: 10px;\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.btn_login.setFocus()
        self.gridLayout.addWidget(self.btn_login, 2, 1, 1, 1)
        self.btn_exit = QtWidgets.QPushButton(self.frame)
        self.btn_exit.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px solid rgb(255, 85, 0);\n"
"background-color: rgb(255, 170, 127);\n"
"    color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(205, 68, 102);\n"
"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 127);\n"
"border: 1px solid  #55ffff;;\n"
"border-radius: 10px;\n"
"}")
        self.btn_exit.setShortcut("")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.clicked.connect(lambda : sys.exit())
        self.gridLayout.addWidget(self.btn_exit, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "login page"))
        self.userline.setToolTip(_translate(
            "Form", "<html><head/><body><p><span style=\" font-size:6pt; color:#e7ffcb;\">Enter your username</span></p></body></html>"))
        self.userline.setPlaceholderText(_translate("Form", "username"))
        self.passline.setToolTip(_translate(
            "Form", "<html><head/><body><p><span style=\"font-size:6pt; color:#e7ffcb;\">Enter your password</span></p></body></html>"))
        self.passline.setPlaceholderText(_translate("Form", "password"))
        self.btn_login.setText(_translate("Form", "Login"))
        # self.btn_login.setShortcut(_translate("Form", "Return, Enter"))
        self.btn_exit.setText(_translate("Form", "Exit"))

    #     self.btn_login.keyPressEvent = self.pppp
    #     def pppp(self,e):
    #     if e.key() == Qt.Key_Return:
    #        print("presed E")


def RunLogins():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    RunLogins()

