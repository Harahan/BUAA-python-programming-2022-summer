# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wrong.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WrongForm(object):
    def setupUi(self, WrongForm):
        WrongForm.setObjectName("WrongForm")
        WrongForm.resize(1200, 755)
        self.horizontalLayoutWidget = QtWidgets.QWidget(WrongForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(290, 520, 721, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutForButtons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayoutForButtons.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutForButtons.setObjectName("horizontalLayoutForButtons")
        self.addToFavoriteQuestionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addToFavoriteQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.addToFavoriteQuestionButton.setObjectName("addToFavoriteQuestionButton")
        self.horizontalLayoutForButtons.addWidget(self.addToFavoriteQuestionButton)
        self.addToReciteQuestionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addToReciteQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.addToReciteQuestionButton.setObjectName("addToReciteQuestionButton")
        self.horizontalLayoutForButtons.addWidget(self.addToReciteQuestionButton)
        self.questionTextEdit = QtWidgets.QTextEdit(WrongForm)
        self.questionTextEdit.setGeometry(QtCore.QRect(240, 60, 821, 171))
        self.questionTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionTextEdit.setObjectName("questionTextEdit")
        self.nextQuestionButton = QtWidgets.QPushButton(WrongForm)
        self.nextQuestionButton.setGeometry(QtCore.QRect(40, 250, 151, 51))
        self.nextQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.nextQuestionButton.setObjectName("nextQuestionButton")
        self.clearCurrentQuestionButton = QtWidgets.QPushButton(WrongForm)
        self.clearCurrentQuestionButton.setGeometry(QtCore.QRect(40, 70, 151, 51))
        self.clearCurrentQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.clearCurrentQuestionButton.setObjectName("clearCurrentQuestionButton")
        self.preQuestionButton = QtWidgets.QPushButton(WrongForm)
        self.preQuestionButton.setGeometry(QtCore.QRect(50, 430, 151, 51))
        self.preQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.preQuestionButton.setObjectName("preQuestionButton")
        self.goBackButton = QtWidgets.QPushButton(WrongForm)
        self.goBackButton.setGeometry(QtCore.QRect(1050, 700, 91, 41))
        self.goBackButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.goBackButton.setObjectName("goBackButton")
        self.userNamelabel = QtWidgets.QLabel(WrongForm)
        self.userNamelabel.setGeometry(QtCore.QRect(1000, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")
        self.label = QtWidgets.QLabel(WrongForm)
        self.label.setGeometry(QtCore.QRect(580, 10, 161, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.scheduleTipsLabel = QtWidgets.QLabel(WrongForm)
        self.scheduleTipsLabel.setGeometry(QtCore.QRect(510, 30, 301, 31))
        self.scheduleTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.scheduleTipsLabel.setObjectName("scheduleTipsLabel")
        self.rightAnswerTextEdit = QtWidgets.QTextEdit(WrongForm)
        self.rightAnswerTextEdit.setGeometry(QtCore.QRect(240, 260, 401, 231))
        self.rightAnswerTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.rightAnswerTextEdit.setObjectName("rightAnswerTextEdit")
        self.questionLabel = QtWidgets.QLabel(WrongForm)
        self.questionLabel.setGeometry(QtCore.QRect(240, 40, 81, 18))
        self.questionLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionLabel.setObjectName("questionLabel")
        self.rightAnswerLabel = QtWidgets.QLabel(WrongForm)
        self.rightAnswerLabel.setGeometry(QtCore.QRect(240, 240, 111, 18))
        self.rightAnswerLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.rightAnswerLabel.setObjectName("rightAnswerLabel")
        self.currentScheduleLabel = QtWidgets.QLabel(WrongForm)
        self.currentScheduleLabel.setGeometry(QtCore.QRect(500, 500, 91, 18))
        self.currentScheduleLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.currentScheduleLabel.setObjectName("currentScheduleLabel")
        self.questionNumberLineEdit = QtWidgets.QLineEdit(WrongForm)
        self.questionNumberLineEdit.setGeometry(QtCore.QRect(580, 497, 51, 25))
        self.questionNumberLineEdit.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.questionNumberLineEdit.setObjectName("questionNumberLineEdit")
        self.totQuestionLabel = QtWidgets.QLabel(WrongForm)
        self.totQuestionLabel.setGeometry(QtCore.QRect(640, 497, 41, 18))
        self.totQuestionLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.totQuestionLabel.setObjectName("totQuestionLabel")
        self.changeQuestionButton = QtWidgets.QPushButton(WrongForm)
        self.changeQuestionButton.setGeometry(QtCore.QRect(690, 500, 21, 21))
        self.changeQuestionButton.setText("")
        self.changeQuestionButton.setObjectName("changeQuestionButton")
        self.wrongAnswerTextEdit = QtWidgets.QTextEdit(WrongForm)
        self.wrongAnswerTextEdit.setGeometry(QtCore.QRect(660, 260, 401, 231))
        self.wrongAnswerTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.wrongAnswerTextEdit.setObjectName("wrongAnswerTextEdit")
        self.wrongAnswerLabel = QtWidgets.QLabel(WrongForm)
        self.wrongAnswerLabel.setGeometry(QtCore.QRect(660, 240, 141, 18))
        self.wrongAnswerLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.wrongAnswerLabel.setObjectName("wrongAnswerLabel")

        self.retranslateUi(WrongForm)
        QtCore.QMetaObject.connectSlotsByName(WrongForm)

    def retranslateUi(self, WrongForm):
        _translate = QtCore.QCoreApplication.translate
        WrongForm.setWindowTitle(_translate("WrongForm", "小航搜题-我的错题本"))
        self.addToFavoriteQuestionButton.setText(_translate("WrongForm", "加入我喜欢的问题"))
        self.addToReciteQuestionButton.setText(_translate("WrongForm", "加入我的背题集"))
        self.questionTextEdit.setHtml(_translate("WrongForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.nextQuestionButton.setText(_translate("WrongForm", "下一条错题"))
        self.clearCurrentQuestionButton.setText(_translate("WrongForm", "删除该条错题"))
        self.preQuestionButton.setText(_translate("WrongForm", "上一条错题"))
        self.goBackButton.setText(_translate("WrongForm", "返回"))
        self.userNamelabel.setText(_translate("WrongForm", "用户名：蛤蛤蛤蛤蛤蛤"))
        self.scheduleTipsLabel.setText(_translate("WrongForm", "已经到底了，没有别的记录了。。。"))
        self.rightAnswerTextEdit.setHtml(_translate("WrongForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.questionLabel.setText(_translate("WrongForm", "题目："))
        self.rightAnswerLabel.setText(_translate("WrongForm", "正确答案："))
        self.currentScheduleLabel.setText(_translate("WrongForm", "当前题目："))
        self.questionNumberLineEdit.setText(_translate("WrongForm", "12"))
        self.totQuestionLabel.setText(_translate("WrongForm", "/129"))
        self.wrongAnswerTextEdit.setHtml(_translate("WrongForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.wrongAnswerLabel.setText(_translate("WrongForm", "我的错误答案："))

