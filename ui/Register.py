# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisterForm(object):
    def setupUi(self, RegisterForm):
        RegisterForm.setObjectName("RegisterForm")
        RegisterForm.resize(563, 343)
        self.userNameInput = QtWidgets.QLineEdit(RegisterForm)
        self.userNameInput.setGeometry(QtCore.QRect(160, 60, 291, 41))
        self.userNameInput.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.userNameInput.setText("")
        self.userNameInput.setObjectName("userNameInput")
        self.userPasswordLable = QtWidgets.QLabel(RegisterForm)
        self.userPasswordLable.setGeometry(QtCore.QRect(50, 150, 91, 31))
        self.userPasswordLable.setStyleSheet("font: 75 10pt \"Consolas\"rgb(241, 255, 235);")
        self.userPasswordLable.setObjectName("userPasswordLable")
        self.userNameTipsLabel = QtWidgets.QLabel(RegisterForm)
        self.userNameTipsLabel.setGeometry(QtCore.QRect(160, 110, 231, 21))
        self.userNameTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNameTipsLabel.setText("")
        self.userNameTipsLabel.setObjectName("userNameTipsLabel")
        self.userPasswordInput = QtWidgets.QLineEdit(RegisterForm)
        self.userPasswordInput.setGeometry(QtCore.QRect(160, 150, 291, 41))
        self.userPasswordInput.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.userPasswordInput.setText("")
        self.userPasswordInput.setObjectName("userPasswordInput")
        self.userPasswordTipsLabel = QtWidgets.QLabel(RegisterForm)
        self.userPasswordTipsLabel.setGeometry(QtCore.QRect(160, 200, 371, 21))
        self.userPasswordTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userPasswordTipsLabel.setText("")
        self.userPasswordTipsLabel.setObjectName("userPasswordTipsLabel")
        self.userNameLable = QtWidgets.QLabel(RegisterForm)
        self.userNameLable.setGeometry(QtCore.QRect(70, 60, 91, 31))
        self.userNameLable.setStyleSheet("font: 75 10pt \"Consolas\"rgb(241, 255, 235);")
        self.userNameLable.setObjectName("userNameLable")
        self.confirmButton = QtWidgets.QPushButton(RegisterForm)
        self.confirmButton.setGeometry(QtCore.QRect(220, 240, 112, 34))
        self.confirmButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.confirmButton.setObjectName("confirmButton")

        self.retranslateUi(RegisterForm)
        QtCore.QMetaObject.connectSlotsByName(RegisterForm)

    def retranslateUi(self, RegisterForm):
        _translate = QtCore.QCoreApplication.translate
        RegisterForm.setWindowTitle(_translate("RegisterForm", "欢迎注册小航搜题"))
        self.userPasswordLable.setText(_translate("RegisterForm", "用户密码："))
        self.userNameLable.setText(_translate("RegisterForm", "用户名："))
        self.confirmButton.setText(_translate("RegisterForm", "确认"))

