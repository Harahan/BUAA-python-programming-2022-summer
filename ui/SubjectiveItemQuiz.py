# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubjectiveItemQuiz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SubjectiveItemQuizForm(object):
    def setupUi(self, SubjectiveItemQuizForm):
        SubjectiveItemQuizForm.setObjectName("SubjectiveItemQuizForm")
        SubjectiveItemQuizForm.resize(1200, 755)
        self.questionTextEdit = QtWidgets.QTextEdit(SubjectiveItemQuizForm)
        self.questionTextEdit.setGeometry(QtCore.QRect(240, 60, 821, 221))
        self.questionTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionTextEdit.setObjectName("questionTextEdit")
        self.preQuestionButton = QtWidgets.QPushButton(SubjectiveItemQuizForm)
        self.preQuestionButton.setGeometry(QtCore.QRect(30, 210, 151, 51))
        self.preQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.preQuestionButton.setObjectName("preQuestionButton")
        self.clearButton = QtWidgets.QPushButton(SubjectiveItemQuizForm)
        self.clearButton.setGeometry(QtCore.QRect(30, 60, 151, 51))
        self.clearButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.clearButton.setObjectName("clearButton")
        self.nextQuestionButton = QtWidgets.QPushButton(SubjectiveItemQuizForm)
        self.nextQuestionButton.setGeometry(QtCore.QRect(30, 390, 151, 51))
        self.nextQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.nextQuestionButton.setObjectName("nextQuestionButton")
        self.userNamelabel = QtWidgets.QLabel(SubjectiveItemQuizForm)
        self.userNamelabel.setGeometry(QtCore.QRect(1000, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")
        self.scheduleLabel = QtWidgets.QLabel(SubjectiveItemQuizForm)
        self.scheduleLabel.setGeometry(QtCore.QRect(510, 30, 301, 31))
        self.scheduleLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.scheduleLabel.setObjectName("scheduleLabel")
        self.confirmButton = QtWidgets.QPushButton(SubjectiveItemQuizForm)
        self.confirmButton.setGeometry(QtCore.QRect(550, 610, 151, 51))
        self.confirmButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.confirmButton.setObjectName("confirmButton")
        self.goBackButton = QtWidgets.QPushButton(SubjectiveItemQuizForm)
        self.goBackButton.setGeometry(QtCore.QRect(1050, 700, 91, 41))
        self.goBackButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.goBackButton.setObjectName("goBackButton")
        self.scoreLabel = QtWidgets.QLabel(SubjectiveItemQuizForm)
        self.scoreLabel.setGeometry(QtCore.QRect(960, 600, 71, 41))
        self.scoreLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.scoreLabel.setObjectName("scoreLabel")
        self.myAnswerLabel = QtWidgets.QLabel(SubjectiveItemQuizForm)
        self.myAnswerLabel.setGeometry(QtCore.QRect(660, 320, 141, 18))
        self.myAnswerLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.myAnswerLabel.setObjectName("myAnswerLabel")
        self.rightAnswerTextEdit = QtWidgets.QTextEdit(SubjectiveItemQuizForm)
        self.rightAnswerTextEdit.setGeometry(QtCore.QRect(240, 340, 401, 231))
        self.rightAnswerTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.rightAnswerTextEdit.setObjectName("rightAnswerTextEdit")
        self.rightAnswerLabel = QtWidgets.QLabel(SubjectiveItemQuizForm)
        self.rightAnswerLabel.setGeometry(QtCore.QRect(240, 320, 111, 18))
        self.rightAnswerLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.rightAnswerLabel.setObjectName("rightAnswerLabel")
        self.myAnswerTextEdit = QtWidgets.QTextEdit(SubjectiveItemQuizForm)
        self.myAnswerTextEdit.setGeometry(QtCore.QRect(660, 340, 401, 231))
        self.myAnswerTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.myAnswerTextEdit.setObjectName("myAnswerTextEdit")
        self.writeTextEdit = QtWidgets.QTextEdit(SubjectiveItemQuizForm)
        self.writeTextEdit.setGeometry(QtCore.QRect(240, 310, 821, 261))
        self.writeTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.writeTextEdit.setObjectName("writeTextEdit")
        self.lineEdit = QtWidgets.QLineEdit(SubjectiveItemQuizForm)
        self.lineEdit.setGeometry(QtCore.QRect(1010, 610, 61, 25))
        self.lineEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.totScoreLabel = QtWidgets.QLabel(SubjectiveItemQuizForm)
        self.totScoreLabel.setGeometry(QtCore.QRect(1080, 600, 71, 41))
        self.totScoreLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.totScoreLabel.setObjectName("totScoreLabel")
        self.goBackButton_2 = QtWidgets.QPushButton(SubjectiveItemQuizForm)
        self.goBackButton_2.setGeometry(QtCore.QRect(940, 700, 91, 41))
        self.goBackButton_2.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.goBackButton_2.setObjectName("goBackButton_2")

        self.retranslateUi(SubjectiveItemQuizForm)
        QtCore.QMetaObject.connectSlotsByName(SubjectiveItemQuizForm)

    def retranslateUi(self, SubjectiveItemQuizForm):
        _translate = QtCore.QCoreApplication.translate
        SubjectiveItemQuizForm.setWindowTitle(_translate("SubjectiveItemQuizForm", "小航搜题-小测试"))
        self.preQuestionButton.setText(_translate("SubjectiveItemQuizForm", "上一题"))
        self.clearButton.setText(_translate("SubjectiveItemQuizForm", "清空答题区"))
        self.nextQuestionButton.setText(_translate("SubjectiveItemQuizForm", "下一题"))
        self.userNamelabel.setText(_translate("SubjectiveItemQuizForm", "用户名：蛤蛤蛤蛤蛤蛤"))
        self.scheduleLabel.setText(_translate("SubjectiveItemQuizForm", "正在识别文件，请耐心等待。。。"))
        self.confirmButton.setText(_translate("SubjectiveItemQuizForm", "确认提交"))
        self.goBackButton.setText(_translate("SubjectiveItemQuizForm", "交卷"))
        self.scoreLabel.setText(_translate("SubjectiveItemQuizForm", "得分："))
        self.myAnswerLabel.setText(_translate("SubjectiveItemQuizForm", "我的答案："))
        self.rightAnswerTextEdit.setHtml(_translate("SubjectiveItemQuizForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.rightAnswerLabel.setText(_translate("SubjectiveItemQuizForm", "正确答案："))
        self.myAnswerTextEdit.setHtml(_translate("SubjectiveItemQuizForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.totScoreLabel.setText(_translate("SubjectiveItemQuizForm", "/10"))
        self.goBackButton_2.setText(_translate("SubjectiveItemQuizForm", "返回"))

