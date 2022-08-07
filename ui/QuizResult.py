# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuizResult.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QuizResultForm(object):
    def setupUi(self, QuizResultForm):
        QuizResultForm.setObjectName("QuizResultForm")
        QuizResultForm.resize(584, 350)
        self.goBackButton = QtWidgets.QPushButton(QuizResultForm)
        self.goBackButton.setGeometry(QtCore.QRect(340, 270, 91, 41))
        self.goBackButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.goBackButton.setObjectName("goBackButton")
        self.relaxButton = QtWidgets.QPushButton(QuizResultForm)
        self.relaxButton.setGeometry(QtCore.QRect(120, 270, 91, 41))
        self.relaxButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.relaxButton.setObjectName("relaxButton")
        self.textEdit = QtWidgets.QTextEdit(QuizResultForm)
        self.textEdit.setGeometry(QtCore.QRect(46, 50, 491, 191))
        self.textEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.textEdit.setObjectName("textEdit")
        self.userNamelabel = QtWidgets.QLabel(QuizResultForm)
        self.userNamelabel.setGeometry(QtCore.QRect(370, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")

        self.retranslateUi(QuizResultForm)
        QtCore.QMetaObject.connectSlotsByName(QuizResultForm)

    def retranslateUi(self, QuizResultForm):
        _translate = QtCore.QCoreApplication.translate
        QuizResultForm.setWindowTitle(_translate("QuizResultForm", "测试结果"))
        self.goBackButton.setText(_translate("QuizResultForm", "返回"))
        self.relaxButton.setText(_translate("QuizResultForm", "放松"))
        self.textEdit.setHtml(_translate("QuizResultForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  恭喜你完成了本次测验，本次测验一共有客观题x道，主观题以及暂无类型的题y道，你完成了z道客观题，w道主观题以及暂无类型的题，取得了a/100的总成绩（每题均按十分满分折合而成），可以选择直接返回主界面或者打把小游戏放松一下啦！</p></body></html>"))
        self.userNamelabel.setText(_translate("QuizResultForm", "用户名：蛤蛤蛤蛤蛤蛤"))

