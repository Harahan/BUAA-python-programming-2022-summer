# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Favorite.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FavoriteForm(object):
    def setupUi(self, FavoriteForm):
        FavoriteForm.setObjectName("FavoriteForm")
        FavoriteForm.resize(1200, 755)
        self.horizontalLayoutWidget = QtWidgets.QWidget(FavoriteForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(290, 520, 721, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutForButtons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayoutForButtons.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutForButtons.setObjectName("horizontalLayoutForButtons")
        self.addToWrongQuestionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addToWrongQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.addToWrongQuestionButton.setObjectName("addToWrongQuestionButton")
        self.horizontalLayoutForButtons.addWidget(self.addToWrongQuestionButton)
        self.addToReciteQuestionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addToReciteQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.addToReciteQuestionButton.setObjectName("addToReciteQuestionButton")
        self.horizontalLayoutForButtons.addWidget(self.addToReciteQuestionButton)
        self.questionTextEdit = QtWidgets.QTextEdit(FavoriteForm)
        self.questionTextEdit.setGeometry(QtCore.QRect(240, 60, 821, 201))
        self.questionTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionTextEdit.setObjectName("questionTextEdit")
        self.nextQuestionButton = QtWidgets.QPushButton(FavoriteForm)
        self.nextQuestionButton.setGeometry(QtCore.QRect(40, 250, 151, 51))
        self.nextQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.nextQuestionButton.setObjectName("nextQuestionButton")
        self.clearCurrentQuestionButton = QtWidgets.QPushButton(FavoriteForm)
        self.clearCurrentQuestionButton.setGeometry(QtCore.QRect(40, 70, 151, 51))
        self.clearCurrentQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.clearCurrentQuestionButton.setObjectName("clearCurrentQuestionButton")
        self.preQuestionButton = QtWidgets.QPushButton(FavoriteForm)
        self.preQuestionButton.setGeometry(QtCore.QRect(50, 430, 151, 51))
        self.preQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.preQuestionButton.setObjectName("preQuestionButton")
        self.goBackButton = QtWidgets.QPushButton(FavoriteForm)
        self.goBackButton.setGeometry(QtCore.QRect(1050, 700, 91, 41))
        self.goBackButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.goBackButton.setObjectName("goBackButton")
        self.userNamelabel = QtWidgets.QLabel(FavoriteForm)
        self.userNamelabel.setGeometry(QtCore.QRect(1000, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")
        self.label = QtWidgets.QLabel(FavoriteForm)
        self.label.setGeometry(QtCore.QRect(580, 10, 161, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.scheduleTipsLabel = QtWidgets.QLabel(FavoriteForm)
        self.scheduleTipsLabel.setGeometry(QtCore.QRect(510, 30, 301, 31))
        self.scheduleTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.scheduleTipsLabel.setObjectName("scheduleTipsLabel")
        self.answerTextEdit = QtWidgets.QTextEdit(FavoriteForm)
        self.answerTextEdit.setGeometry(QtCore.QRect(240, 290, 821, 201))
        self.answerTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.answerTextEdit.setObjectName("answerTextEdit")
        self.questionLabel = QtWidgets.QLabel(FavoriteForm)
        self.questionLabel.setGeometry(QtCore.QRect(240, 40, 81, 18))
        self.questionLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionLabel.setObjectName("questionLabel")
        self.rightAnswerLabel = QtWidgets.QLabel(FavoriteForm)
        self.rightAnswerLabel.setGeometry(QtCore.QRect(240, 270, 111, 18))
        self.rightAnswerLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.rightAnswerLabel.setObjectName("rightAnswerLabel")
        self.currentScheduleLabel = QtWidgets.QLabel(FavoriteForm)
        self.currentScheduleLabel.setGeometry(QtCore.QRect(520, 510, 91, 18))
        self.currentScheduleLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.currentScheduleLabel.setObjectName("currentScheduleLabel")
        self.questionNumberLineEdit = QtWidgets.QLineEdit(FavoriteForm)
        self.questionNumberLineEdit.setGeometry(QtCore.QRect(610, 500, 51, 31))
        self.questionNumberLineEdit.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.questionNumberLineEdit.setObjectName("questionNumberLineEdit")
        self.totQuestionLabel = QtWidgets.QLabel(FavoriteForm)
        self.totQuestionLabel.setGeometry(QtCore.QRect(660, 507, 41, 18))
        self.totQuestionLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.totQuestionLabel.setObjectName("totQuestionLabel")
        self.changeQuestionButton = QtWidgets.QPushButton(FavoriteForm)
        self.changeQuestionButton.setGeometry(QtCore.QRect(710, 510, 21, 21))
        self.changeQuestionButton.setText("")
        self.changeQuestionButton.setObjectName("changeQuestionButton")

        self.retranslateUi(FavoriteForm)
        QtCore.QMetaObject.connectSlotsByName(FavoriteForm)

    def retranslateUi(self, FavoriteForm):
        _translate = QtCore.QCoreApplication.translate
        FavoriteForm.setWindowTitle(_translate("FavoriteForm", "小航搜题-我喜欢的问题"))
        self.addToWrongQuestionButton.setText(_translate("FavoriteForm", "加入我的错题本"))
        self.addToReciteQuestionButton.setText(_translate("FavoriteForm", "加入我的背题集"))
        self.questionTextEdit.setHtml(_translate("FavoriteForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.nextQuestionButton.setText(_translate("FavoriteForm", "下一题"))
        self.clearCurrentQuestionButton.setText(_translate("FavoriteForm", "不再喜欢该题"))
        self.preQuestionButton.setText(_translate("FavoriteForm", "上一题"))
        self.goBackButton.setText(_translate("FavoriteForm", "返回"))
        self.userNamelabel.setText(_translate("FavoriteForm", "用户名：蛤蛤蛤蛤蛤蛤"))
        self.scheduleTipsLabel.setText(_translate("FavoriteForm", "已经到底了，没有别的记录了。。。"))
        self.answerTextEdit.setHtml(_translate("FavoriteForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.questionLabel.setText(_translate("FavoriteForm", "题目："))
        self.rightAnswerLabel.setText(_translate("FavoriteForm", "答案："))
        self.currentScheduleLabel.setText(_translate("FavoriteForm", "当前题目："))
        self.questionNumberLineEdit.setText(_translate("FavoriteForm", "12"))
        self.totQuestionLabel.setText(_translate("FavoriteForm", "/129"))

