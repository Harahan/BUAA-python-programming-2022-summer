# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchingResult.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchingResultForm(object):
    def setupUi(self, SearchingResultForm):
        SearchingResultForm.setObjectName("SearchingResultForm")
        SearchingResultForm.resize(1200, 755)
        self.horizontalLayoutWidget = QtWidgets.QWidget(SearchingResultForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 520, 1091, 171))
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
        self.addToWrongQuestionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addToWrongQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.addToWrongQuestionButton.setObjectName("addToWrongQuestionButton")
        self.horizontalLayoutForButtons.addWidget(self.addToWrongQuestionButton)
        self.questionTextEdit = QtWidgets.QTextEdit(SearchingResultForm)
        self.questionTextEdit.setGeometry(QtCore.QRect(150, 60, 911, 201))
        self.questionTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionTextEdit.setObjectName("questionTextEdit")
        self.goBackButton = QtWidgets.QPushButton(SearchingResultForm)
        self.goBackButton.setGeometry(QtCore.QRect(1050, 700, 91, 41))
        self.goBackButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.goBackButton.setObjectName("goBackButton")
        self.userNamelabel = QtWidgets.QLabel(SearchingResultForm)
        self.userNamelabel.setGeometry(QtCore.QRect(1000, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")
        self.label = QtWidgets.QLabel(SearchingResultForm)
        self.label.setGeometry(QtCore.QRect(580, 10, 161, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.scheduleTipsLabel = QtWidgets.QLabel(SearchingResultForm)
        self.scheduleTipsLabel.setGeometry(QtCore.QRect(250, 30, 741, 31))
        self.scheduleTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.scheduleTipsLabel.setObjectName("scheduleTipsLabel")
        self.answerTextEdit = QtWidgets.QTextEdit(SearchingResultForm)
        self.answerTextEdit.setGeometry(QtCore.QRect(150, 290, 911, 201))
        self.answerTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.answerTextEdit.setObjectName("answerTextEdit")
        self.questionLabel = QtWidgets.QLabel(SearchingResultForm)
        self.questionLabel.setGeometry(QtCore.QRect(150, 40, 111, 18))
        self.questionLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionLabel.setObjectName("questionLabel")
        self.answerLabel = QtWidgets.QLabel(SearchingResultForm)
        self.answerLabel.setGeometry(QtCore.QRect(150, 270, 101, 18))
        self.answerLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.answerLabel.setObjectName("answerLabel")
        self.pushButton = QtWidgets.QPushButton(SearchingResultForm)
        self.pushButton.setGeometry(QtCore.QRect(411, 500, 351, 34))
        self.pushButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(SearchingResultForm)
        QtCore.QMetaObject.connectSlotsByName(SearchingResultForm)

    def retranslateUi(self, SearchingResultForm):
        _translate = QtCore.QCoreApplication.translate
        SearchingResultForm.setWindowTitle(_translate("SearchingResultForm", "小航搜题-搜索结果"))
        self.addToFavoriteQuestionButton.setText(_translate("SearchingResultForm", "加入我喜欢的问题"))
        self.addToReciteQuestionButton.setText(_translate("SearchingResultForm", "加入我的背题集"))
        self.addToWrongQuestionButton.setText(_translate("SearchingResultForm", "加入我的错题本"))
        self.questionTextEdit.setHtml(_translate("SearchingResultForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.goBackButton.setText(_translate("SearchingResultForm", "返回"))
        self.userNamelabel.setText(_translate("SearchingResultForm", "用户名：蛤蛤蛤蛤蛤蛤"))
        self.scheduleTipsLabel.setText(_translate("SearchingResultForm", "什么也没搜到，选择自动生成答案吧（注：需提供一段与答案有关的参考文本与原问题）"))
        self.answerTextEdit.setHtml(_translate("SearchingResultForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.questionLabel.setText(_translate("SearchingResultForm", "搜索问题："))
        self.answerLabel.setText(_translate("SearchingResultForm", "搜索结果："))
        self.pushButton.setText(_translate("SearchingResultForm", "自动生成答案"))

