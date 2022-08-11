# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoGenerateAnswer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AutoGenerateAnswerForm(object):
    def setupUi(self, AutoGenerateAnswerForm):
        AutoGenerateAnswerForm.setObjectName("AutoGenerateAnswerForm")
        AutoGenerateAnswerForm.resize(1200, 755)
        self.refTxtTextEdit = QtWidgets.QTextEdit(AutoGenerateAnswerForm)
        self.refTxtTextEdit.setGeometry(QtCore.QRect(240, 60, 821, 241))
        self.refTxtTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.refTxtTextEdit.setObjectName("refTxtTextEdit")
        self.openFileButton = QtWidgets.QPushButton(AutoGenerateAnswerForm)
        self.openFileButton.setGeometry(QtCore.QRect(30, 130, 151, 51))
        self.openFileButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.openFileButton.setObjectName("openFileButton")
        self.goBackButton = QtWidgets.QPushButton(AutoGenerateAnswerForm)
        self.goBackButton.setGeometry(QtCore.QRect(1050, 700, 91, 41))
        self.goBackButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.goBackButton.setObjectName("goBackButton")
        self.userNamelabel = QtWidgets.QLabel(AutoGenerateAnswerForm)
        self.userNamelabel.setGeometry(QtCore.QRect(1000, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")
        self.label = QtWidgets.QLabel(AutoGenerateAnswerForm)
        self.label.setGeometry(QtCore.QRect(580, 10, 161, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.scheduleTipsLabel = QtWidgets.QLabel(AutoGenerateAnswerForm)
        self.scheduleTipsLabel.setGeometry(QtCore.QRect(510, 30, 301, 31))
        self.scheduleTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.scheduleTipsLabel.setObjectName("scheduleTipsLabel")
        self.questionTextEdit = QtWidgets.QTextEdit(AutoGenerateAnswerForm)
        self.questionTextEdit.setGeometry(QtCore.QRect(240, 340, 401, 321))
        self.questionTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionTextEdit.setObjectName("questionTextEdit")
        self.refTxtLabel = QtWidgets.QLabel(AutoGenerateAnswerForm)
        self.refTxtLabel.setGeometry(QtCore.QRect(240, 40, 111, 18))
        self.refTxtLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.refTxtLabel.setObjectName("refTxtLabel")
        self.questionLabel = QtWidgets.QLabel(AutoGenerateAnswerForm)
        self.questionLabel.setGeometry(QtCore.QRect(240, 310, 111, 18))
        self.questionLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionLabel.setObjectName("questionLabel")
        self.AnswerTextEdit = QtWidgets.QTextEdit(AutoGenerateAnswerForm)
        self.AnswerTextEdit.setGeometry(QtCore.QRect(660, 340, 401, 321))
        self.AnswerTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.AnswerTextEdit.setObjectName("AnswerTextEdit")
        self.AnswerLabel = QtWidgets.QLabel(AutoGenerateAnswerForm)
        self.AnswerLabel.setGeometry(QtCore.QRect(660, 310, 141, 18))
        self.AnswerLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.AnswerLabel.setObjectName("AnswerLabel")
        self.confirmButton = QtWidgets.QPushButton(AutoGenerateAnswerForm)
        self.confirmButton.setGeometry(QtCore.QRect(30, 370, 151, 51))
        self.confirmButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.confirmButton.setObjectName("confirmButton")

        self.retranslateUi(AutoGenerateAnswerForm)
        QtCore.QMetaObject.connectSlotsByName(AutoGenerateAnswerForm)

    def retranslateUi(self, AutoGenerateAnswerForm):
        _translate = QtCore.QCoreApplication.translate
        AutoGenerateAnswerForm.setWindowTitle(_translate("AutoGenerateAnswerForm", "小航搜题-自动生成答案"))
        self.refTxtTextEdit.setHtml(_translate("AutoGenerateAnswerForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.openFileButton.setText(_translate("AutoGenerateAnswerForm", "上传文本"))
        self.goBackButton.setText(_translate("AutoGenerateAnswerForm", "返回"))
        self.userNamelabel.setText(_translate("AutoGenerateAnswerForm", "用户名：蛤蛤蛤蛤蛤蛤"))
        self.scheduleTipsLabel.setText(_translate("AutoGenerateAnswerForm", "已经到底了，没有别的记录了。。。"))
        self.questionTextEdit.setHtml(_translate("AutoGenerateAnswerForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.refTxtLabel.setText(_translate("AutoGenerateAnswerForm", "参考文本："))
        self.questionLabel.setText(_translate("AutoGenerateAnswerForm", "问题："))
        self.AnswerTextEdit.setHtml(_translate("AutoGenerateAnswerForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.AnswerLabel.setText(_translate("AutoGenerateAnswerForm", "参考答案："))
        self.confirmButton.setText(_translate("AutoGenerateAnswerForm", "确认"))

