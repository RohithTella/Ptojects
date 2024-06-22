# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import bk_rc
import mydpi
import dataB

from AnyQt.QtWidgets import QWidget, QGridLayout, QLineEdit, QSizePolicy, QTextEdit, QFrame, QStatusBar, QToolBar, \
    QAction
from PyQt5.QtCore import Qt, QLocale, QCoreApplication, QMetaObject
from PyQt5.QtGui import QIcon, QFont, QCursor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Ui_MainWindow(QMainWindow):
    def setupU(self, MainWindow):
        # MainWindow.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowIcon(QIcon('src\iconPT.png'))
        MainWindow.setWindowTitle("Secure Notepad")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 440)
        font = QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setWhatsThis("")
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "background-color: rgb(33, 33, 33);\n"
                                 "}\n"
                                 "QStatusBar{\n"
                                 "background-color:rgb(33, 33, 33);\n"
                                 "color: rgb(0, 255, 59);\n"
                                 "border:1px solid rgbrgb(0, 148, 0);\n"
                                 "border-radius:2px;\n"
                                 "    font: 8pt \"Arial\";\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "background-color:rgb(45, 45, 45);\n"
                                    "    border: 1.2px solid rgb(177, 255, 51);\n"
                                    "    border-radius: 5px;\n"
                                    "    color: rgb(0, 255, 255);\n"
                                    "}\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.textEdit = QTextEdit(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setToolTipDuration(-4)
        self.textEdit.setLayoutDirection(Qt.LeftToRight)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("QTextEdit {\n"
                                    "background-color:rgb(45, 45, 45);\n"
                                    "    border: 1px solid rgb(177, 255, 51);\n"
                                    "    border-radius: 5px;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "}\n"
                                    "")
        self.textEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setDocumentTitle("")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolBar.setToolTip("")
        self.toolBar.setStatusTip("")
        self.toolBar.setStyleSheet("QToolBar{\n"
                                   "background-color: rgb(33, 33, 33);\n"
                                   "    border: 1px solid rgb(169, 137, 189);\n"
                                   "    border-radius: 5px;\n"
                                   "}\n"
                                   "\n"
                                   "QToolTip {\n"
                                   "background-color: rgba(0, 0, 0, 0);\n"
                                   "    border: 1px solid darkkhaki;\n"
                                   "    border-radius: 5px;\n"
                                   "    color: rgb(255, 255, 0);\n"
                                   "}")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar)
        self.action_new = QAction(MainWindow)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/ToolBar/file.svg"), QIcon.Normal, QIcon.Off)
        self.action_new.setIcon(icon)
        self.action_new.setObjectName("action_new")
        self.action_open = QAction(MainWindow)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/ToolBar/folder.svg"), QIcon.Normal, QIcon.Off)
        self.action_open.setIcon(icon1)
        self.action_open.setObjectName("action_open")
        self.action_save = QAction(MainWindow)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/ToolBar/save.svg"), QIcon.Normal, QIcon.Off)
        self.action_save.setIcon(icon2)
        self.action_save.setObjectName("action_save")
        self.action_exit = QAction(MainWindow)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/ToolBar/src/exit.png"), QIcon.Normal, QIcon.Off)
        self.action_exit.setIcon(icon3)
        self.action_exit.setObjectName("action_exit")
        self.action_clear = QAction(MainWindow)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/ToolBar/src/clear.png"), QIcon.Normal, QIcon.Off)
        self.action_clear.setIcon(icon4)
        self.action_clear.setObjectName("action_clear")
        self.action_setting = QAction(MainWindow)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(":/ToolBar/settings.svg"), QIcon.Normal, QIcon.Off)
        self.action_setting.setIcon(icon5)
        self.action_setting.setObjectName("action_setting")
        self.action_FM = QAction(MainWindow)
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(":/ToolBar/src/full_screen.png"), QIcon.Normal, QIcon.Off)
        self.action_FM.setIcon(icon6)
        self.action_FM.setObjectName("action_FM")
        self.toolBar.addAction(self.action_new)
        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_save)
        self.toolBar.addAction(self.action_clear)
        self.toolBar.addAction(self.action_FM)
        self.toolBar.addAction(self.action_setting)
        self.toolBar.addAction(self.action_exit)

        self.retranslateUi(MainWindow)
        self.mwmw = MainWindow
        self.action_exit.triggered.connect(MainWindow.close)
        self.action_new.triggered.connect(self.Add_New)
        self.action_clear.triggered.connect(self.Pakon)
        self.action_save.triggered.connect(self.Save_Data)
        self.action_FM.triggered.connect(self.stateWindowSizes)
        QMetaObject.connectSlotsByName(MainWindow)

# Tabehaie dokmehaie Toolbar
    def Add_New(self):
        self.Save_Data()
        self.lineEdit.setText('')
        self.textEdit.setText('')

    def Pakon(self):
        self.lineEdit.setText('')
        self.textEdit.setText('')

    def Save_Data(self):
        self.O = self.lineEdit.text()
        self.T = self.textEdit.toPlainText()
        if str(self.O) != '' or str(self.T) != '':
            dataB.database.dbcn(self, self.O, self.T)
            box = QMessageBox()
            box.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowTitleHint)
            box.setIcon(QMessageBox.Question)
            box.setWindowTitle('save')
            box.setText('The note was saved successfully')
            box.setStandardButtons(QMessageBox.Yes)
            buttonY = box.button(QMessageBox.Yes)
            buttonY.setText('OK')
            box.exec_()
        else:
            box = QMessageBox()
            box.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowTitleHint)
            box.setIcon(QMessageBox.Question)
            box.setWindowTitle('save')
            box.setText('Failed to save!\nThere must be at least one field containing information.')
            box.setStandardButtons(QMessageBox.Yes)
            buttonY = box.button(QMessageBox.Yes)
            buttonY.setText('OK')
            box.exec_()

    def stateWindowSizes(self):
        MainWindow = self.mwmw
        if MainWindow.isMaximized():
            MainWindow.showNormal()
        else:
            MainWindow.showMaximized()

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secure Notepad"))
        self.lineEdit.setStatusTip(_translate("MainWindow", "Enter the title of your note"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Title ... "))
        self.lineEdit.setToolTip(_translate("MainWindow", "Title ..."))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Body ... "))
        self.textEdit.setStatusTip(_translate("MainWindow", "Enter your note"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_new.setText(_translate("MainWindow", "New"))
        self.action_new.setToolTip(_translate("MainWindow", "New"))
        self.action_new.setStatusTip(_translate("MainWindow", "Create a new note"))
        self.action_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_open.setToolTip(_translate("MainWindow", "Open"))
        self.action_open.setStatusTip(_translate("MainWindow", "View saved notes "))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "To save"))
        self.action_save.setToolTip(_translate("MainWindow", "To save"))
        self.action_save.setStatusTip(_translate("MainWindow", "Save current note"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_exit.setStatusTip(_translate("MainWindow", "Exit the program"))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_clear.setText(_translate("MainWindow", "Clean"))
        self.action_clear.setStatusTip(_translate("MainWindow", "Delete current note"))
        self.action_clear.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.action_setting.setText(_translate("MainWindow", "Settings"))
        self.action_setting.setStatusTip(_translate("MainWindow", "Program settings"))
        self.action_setting.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.action_FM.setText(_translate("MainWindow", "Change window mode"))
        self.action_FM.setToolTip(_translate("MainWindow", "Change window mode"))
        self.action_FM.setStatusTip(_translate("MainWindow", "Zoom in or zoom out"))
        self.action_FM.setShortcut(_translate("MainWindow", "Ctrl+Up"))


def RunMains():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupU(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    RunMains()
