# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TetrisResult.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TetrisResultForm(object):
    def setupUi(self, TetrisResultForm):
        TetrisResultForm.setObjectName("TetrisResultForm")
        TetrisResultForm.resize(584, 350)
        self.goBackButton = QtWidgets.QPushButton(TetrisResultForm)
        self.goBackButton.setGeometry(QtCore.QRect(320, 270, 111, 41))
        self.goBackButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.goBackButton.setObjectName("goBackButton")
        self.userNamelabel = QtWidgets.QLabel(TetrisResultForm)
        self.userNamelabel.setGeometry(QtCore.QRect(370, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")
        self.againButton = QtWidgets.QPushButton(TetrisResultForm)
        self.againButton.setGeometry(QtCore.QRect(160, 270, 111, 41))
        self.againButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.againButton.setObjectName("againButton")
        self.sysLabel = QtWidgets.QLabel(TetrisResultForm)
        self.sysLabel.setGeometry(QtCore.QRect(160, 70, 101, 31))
        self.sysLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.sysLabel.setObjectName("sysLabel")
        self.userLabel = QtWidgets.QLabel(TetrisResultForm)
        self.userLabel.setGeometry(QtCore.QRect(160, 130, 101, 31))
        self.userLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.userLabel.setObjectName("userLabel")
        self.userCurLabel = QtWidgets.QLabel(TetrisResultForm)
        self.userCurLabel.setGeometry(QtCore.QRect(160, 190, 161, 31))
        self.userCurLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.userCurLabel.setObjectName("userCurLabel")
        self.lineEdit = QtWidgets.QLineEdit(TetrisResultForm)
        self.lineEdit.setGeometry(QtCore.QRect(300, 70, 113, 31))
        self.lineEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(TetrisResultForm)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 130, 113, 31))
        self.lineEdit_2.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(TetrisResultForm)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 190, 113, 31))
        self.lineEdit_3.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(TetrisResultForm)
        self.label.setGeometry(QtCore.QRect(230, 240, 251, 18))
        self.label.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.label.setObjectName("label")

        self.retranslateUi(TetrisResultForm)
        QtCore.QMetaObject.connectSlotsByName(TetrisResultForm)

    def retranslateUi(self, TetrisResultForm):
        _translate = QtCore.QCoreApplication.translate
        TetrisResultForm.setWindowTitle(_translate("TetrisResultForm", "游戏结果"))
        self.goBackButton.setText(_translate("TetrisResultForm", "返回"))
        self.userNamelabel.setText(_translate("TetrisResultForm", "用户名：蛤蛤蛤蛤蛤蛤"))
        self.againButton.setText(_translate("TetrisResultForm", "再来一局"))
        self.sysLabel.setText(_translate("TetrisResultForm", "系统记录："))
        self.userLabel.setText(_translate("TetrisResultForm", "用户记录："))
        self.userCurLabel.setText(_translate("TetrisResultForm", "用户此局分数："))
        self.label.setText(_translate("TetrisResultForm", "你觉得可能吗？"))

