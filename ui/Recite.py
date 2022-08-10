# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Recite.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReciteForm(object):
    def setupUi(self, ReciteForm):
        ReciteForm.setObjectName("ReciteForm")
        ReciteForm.resize(1200, 755)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ReciteForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(290, 520, 721, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutForButtons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayoutForButtons.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutForButtons.setObjectName("horizontalLayoutForButtons")
        self.addToWrongQuestionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addToWrongQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.addToWrongQuestionButton.setObjectName("addToWrongQuestionButton")
        self.horizontalLayoutForButtons.addWidget(self.addToWrongQuestionButton)
        self.addToFavoriteQuestionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addToFavoriteQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.addToFavoriteQuestionButton.setObjectName("addToFavoriteQuestionButton")
        self.horizontalLayoutForButtons.addWidget(self.addToFavoriteQuestionButton)
        self.questionTextEdit = QtWidgets.QTextEdit(ReciteForm)
        self.questionTextEdit.setGeometry(QtCore.QRect(240, 60, 821, 201))
        self.questionTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionTextEdit.setObjectName("questionTextEdit")
        self.nextQuestionButton = QtWidgets.QPushButton(ReciteForm)
        self.nextQuestionButton.setGeometry(QtCore.QRect(40, 250, 151, 51))
        self.nextQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.nextQuestionButton.setObjectName("nextQuestionButton")
        self.clearCurrentQuestionButton = QtWidgets.QPushButton(ReciteForm)
        self.clearCurrentQuestionButton.setGeometry(QtCore.QRect(40, 70, 151, 51))
        self.clearCurrentQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.clearCurrentQuestionButton.setObjectName("clearCurrentQuestionButton")
        self.preQuestionButton = QtWidgets.QPushButton(ReciteForm)
        self.preQuestionButton.setGeometry(QtCore.QRect(50, 430, 151, 51))
        self.preQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.preQuestionButton.setObjectName("preQuestionButton")
        self.goBackButton = QtWidgets.QPushButton(ReciteForm)
        self.goBackButton.setGeometry(QtCore.QRect(1050, 700, 91, 41))
        self.goBackButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.goBackButton.setObjectName("goBackButton")
        self.userNamelabel = QtWidgets.QLabel(ReciteForm)
        self.userNamelabel.setGeometry(QtCore.QRect(1000, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")
        self.label = QtWidgets.QLabel(ReciteForm)
        self.label.setGeometry(QtCore.QRect(580, 10, 161, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.scheduleTipsLabel = QtWidgets.QLabel(ReciteForm)
        self.scheduleTipsLabel.setGeometry(QtCore.QRect(510, 30, 301, 31))
        self.scheduleTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.scheduleTipsLabel.setObjectName("scheduleTipsLabel")
        self.answerTextEdit = QtWidgets.QTextEdit(ReciteForm)
        self.answerTextEdit.setGeometry(QtCore.QRect(240, 290, 821, 201))
        self.answerTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.answerTextEdit.setObjectName("answerTextEdit")
        self.questionLabel = QtWidgets.QLabel(ReciteForm)
        self.questionLabel.setGeometry(QtCore.QRect(240, 40, 81, 18))
        self.questionLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionLabel.setObjectName("questionLabel")
        self.rightAnswerLabel = QtWidgets.QLabel(ReciteForm)
        self.rightAnswerLabel.setGeometry(QtCore.QRect(240, 270, 111, 18))
        self.rightAnswerLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.rightAnswerLabel.setObjectName("rightAnswerLabel")
        self.currentScheduleLabel = QtWidgets.QLabel(ReciteForm)
        self.currentScheduleLabel.setGeometry(QtCore.QRect(540, 510, 91, 18))
        self.currentScheduleLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.currentScheduleLabel.setObjectName("currentScheduleLabel")
        self.questionNumberLineEdit = QtWidgets.QLineEdit(ReciteForm)
        self.questionNumberLineEdit.setGeometry(QtCore.QRect(630, 500, 51, 31))
        self.questionNumberLineEdit.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.questionNumberLineEdit.setObjectName("questionNumberLineEdit")
        self.totQuestionLabel = QtWidgets.QLabel(ReciteForm)
        self.totQuestionLabel.setGeometry(QtCore.QRect(680, 507, 41, 18))
        self.totQuestionLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.totQuestionLabel.setObjectName("totQuestionLabel")
        self.changeQuestionButton = QtWidgets.QPushButton(ReciteForm)
        self.changeQuestionButton.setGeometry(QtCore.QRect(730, 510, 21, 21))
        self.changeQuestionButton.setText("")
        self.changeQuestionButton.setObjectName("changeQuestionButton")

        self.retranslateUi(ReciteForm)
        QtCore.QMetaObject.connectSlotsByName(ReciteForm)

    def retranslateUi(self, ReciteForm):
        _translate = QtCore.QCoreApplication.translate
        ReciteForm.setWindowTitle(_translate("ReciteForm", "小航搜题-我的背题集"))
        self.addToWrongQuestionButton.setText(_translate("ReciteForm", "加入我的错题本"))
        self.addToFavoriteQuestionButton.setText(_translate("ReciteForm", "加入我喜欢的问题"))
        self.questionTextEdit.setHtml(_translate("ReciteForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.nextQuestionButton.setText(_translate("ReciteForm", "下一题"))
        self.clearCurrentQuestionButton.setText(_translate("ReciteForm", "不再背诵该题"))
        self.preQuestionButton.setText(_translate("ReciteForm", "上一题"))
        self.goBackButton.setText(_translate("ReciteForm", "返回"))
        self.userNamelabel.setText(_translate("ReciteForm", "用户名：蛤蛤蛤蛤蛤蛤"))
        self.scheduleTipsLabel.setText(_translate("ReciteForm", "已经到底了，没有别的记录了。。。"))
        self.answerTextEdit.setHtml(_translate("ReciteForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.questionLabel.setText(_translate("ReciteForm", "题目："))
        self.rightAnswerLabel.setText(_translate("ReciteForm", "答案："))
        self.currentScheduleLabel.setText(_translate("ReciteForm", "当前题目："))
        self.questionNumberLineEdit.setText(_translate("ReciteForm", "12"))
        self.totQuestionLabel.setText(_translate("ReciteForm", "/129"))

