# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogF.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mydpi

from PyQt5.QtGui import QIcon


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        # Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        Dialog.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        # Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 105)
        Dialog.setMinimumSize(QtCore.QSize(400, 105))
        Dialog.setMaximumSize(QtCore.QSize(400, 105))
        Dialog.setWindowIcon(QIcon('src\error1.png'))
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 40, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.btn_try = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
        self.btn_exit = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("QFrame{\n"
                                 "background-color: rgb(81, 50, 108);\n"
                                 "border: 2px solid  rgb(255, 0, 0);\n"
                                 "border-radius:30px;\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 5, 20, 12)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "color: rgb(255, 0, 0);\n"
                                 "font-weight: bold;\n"
                                 "border:no;\n"
                                 "}")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        # self.btn_exit = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton:hover:!pressed\n"
                                    "{\n"
                                    "  border: 1px solid rgb(251, 255, 0);\n"
                                    "    background-color: rgb(255, 0, 0);\n"
                                    "    color: rgb(0, 255, 0);\n"
                                    "}\n"
                                    "QPushButton{\n"
                                    "background-color: rgb(166, 166, 92);\n"
                                    "font: 10pt  \"B Zar\" ;\n"
                                    "font-weight: bold;\n"
                                    "    color: rgb(255, 0, 0);\n"
                                    "border: 1px solid  rgb(255, 0, 0);;\n"
                                    "border-radius: 10px;\n"
                                    "}")
        self.btn_exit.setObjectName("btn_exit")
        self.gridLayout.addWidget(self.btn_exit, 1, 0, 1, 1)
        # self.btn_try = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_try.sizePolicy().hasHeightForWidth())
        self.btn_try.setSizePolicy(sizePolicy)
        self.btn_try.setMinimumSize(QtCore.QSize(20, 10))
        self.btn_try.setSizeIncrement(QtCore.QSize(3, 5))
        self.btn_try.setBaseSize(QtCore.QSize(10, 5))
        self.btn_try.setStyleSheet("QPushButton:hover:!pressed\n"
                                   "{\n"
                                   "  border: 1px solid rgb(255, 85, 255);\n"
                                   "    background-color: rgb(8, 0, 255);\n"
                                   "    color: rgb(255, 255, 0);\n"
                                   "}\n"
                                   "QPushButton{\n"
                                   "background-color: rgb(112, 237, 217);\n"
                                   "font: 10pt \"B Zar\";\n"
                                   "font-weight: bold;\n"
                                   "color: rgb(0, 0, 255);\n"
                                   "border: 1px solid rgb(255, 200, 0);\n"
                                   "border-radius: 10px;\n"
                                   "}")
        self.btn_try.setIconSize(QtCore.QSize(10, 10))
        self.btn_try.setAutoExclusive(True)
        self.btn_try.setFlat(False)
        self.btn_try.setObjectName("btn_try")
        self.gridLayout.addWidget(self.btn_try, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error"))
        self.label.setText(_translate("Dialog", "Username or password is wrong!"))
        self.btn_exit.setText(_translate("Dialog", "Exit"))
        self.btn_try.setText(_translate("Dialog", "Try again"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
