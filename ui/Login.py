# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtWidgets
from qt_material import apply_stylesheet
from PyQt5.Qt import *


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(637, 408)
        self.userNameInput = QtWidgets.QLineEdit(LoginForm)
        self.userNameInput.setGeometry(QtCore.QRect(180, 90, 291, 41))
        self.userNameInput.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.userNameInput.setObjectName("userNameInput")
        self.userPasswordInput = QtWidgets.QLineEdit(LoginForm)
        self.userPasswordInput.setGeometry(QtCore.QRect(180, 180, 291, 41))
        self.userPasswordInput.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.userPasswordInput.setObjectName("userPasswordInput")
        self.signInButton = QtWidgets.QPushButton(LoginForm)
        self.signInButton.setGeometry(QtCore.QRect(260, 290, 112, 34))
        self.signInButton.setStyleSheet("font: 75 10pt \"Consolas\"rgb(241, 255, 235);\n"
"")
        self.signInButton.setObjectName("signInButton")
        self.signUpButton = QtWidgets.QPushButton(LoginForm)
        self.signUpButton.setGeometry(QtCore.QRect(510, 350, 112, 34))
        self.signUpButton.setStyleSheet("font: 75 10pt \"Consolas\"rgb(241, 255, 235);")
        self.signUpButton.setObjectName("signUpButton")
        self.userNameLable = QtWidgets.QLabel(LoginForm)
        self.userNameLable.setGeometry(QtCore.QRect(90, 90, 91, 31))
        self.userNameLable.setStyleSheet("font: 75 10pt \"Consolas\"rgb(241, 255, 235);")
        self.userNameLable.setObjectName("userNameLable")
        self.userPasswordLable = QtWidgets.QLabel(LoginForm)
        self.userPasswordLable.setGeometry(QtCore.QRect(70, 180, 91, 31))
        self.userPasswordLable.setStyleSheet("font: 75 10pt \"Consolas\"rgb(241, 255, 235);")
        self.userPasswordLable.setObjectName("userPasswordLable")
        self.userNameTipsLabel = QtWidgets.QLabel(LoginForm)
        self.userNameTipsLabel.setGeometry(QtCore.QRect(180, 140, 231, 21))
        self.userNameTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNameTipsLabel.setObjectName("userNameTipsLabel")
        self.userPasswordTipsLabel = QtWidgets.QLabel(LoginForm)
        self.userPasswordTipsLabel.setGeometry(QtCore.QRect(180, 230, 231, 21))
        self.userPasswordTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userPasswordTipsLabel.setObjectName("userPasswordTipsLabel")

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "登陆小航搜题"))
        self.signInButton.setText(_translate("LoginForm", "登陆"))
        self.signUpButton.setText(_translate("LoginForm", "注册"))
        self.userNameLable.setText(_translate("LoginForm", "用户名："))
        self.userPasswordLable.setText(_translate("LoginForm", "用户密码："))
        self.userNameTipsLabel.setText(_translate("LoginForm", "该用户名不存在!"))
        self.userPasswordTipsLabel.setText(_translate("LoginForm", "密码错误!"))


if __name__ == "__main__":
    class MyMainForm(QMainWindow, Ui_LoginForm):
        def __init__(self, parent=None):
            super(MyMainForm, self).__init__(parent)
            self.setupUi(self)
    
    
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())