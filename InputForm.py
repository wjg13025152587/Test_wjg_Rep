# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputForm.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from refer import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 450, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 450, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 50, 371, 381))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 10, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.joint_code)
        self.pushButton_2.clicked.connect(self.clear_btn)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "请输入C++源代码路径："))
        self.pushButton.setText(_translate("MainWindow", "输出结果"))
        self.pushButton_2.setText(_translate("MainWindow", "清空"))
        self.label_2.setText(_translate("MainWindow", "输出结果："))

    def clear_btn(self):
        self.textEdit_2.clear()

    def joint_code(self):
        ComPlier = Complier()
        ComPlier.str = ""
        SourceProgram = []
        Filepath = self.lineEdit.text()
        for line in open(Filepath, 'r', encoding='UTF-8-sig'):
            line = line.replace('\n', '')
            SourceProgram.append(line)
        SourceProgram = ComPlier.DeleteNote(SourceProgram)
        SourceProgram = ComPlier.RemoveSpace(SourceProgram)
        SourceProgram = ComPlier.Reader(SourceProgram)
        SourceProgram = ComPlier.combine_head(SourceProgram)
        ComPlier.JugeMent(SourceProgram)
        self.textEdit_2.setPlainText(ComPlier.str)