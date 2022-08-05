# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Contribute.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ContributeForm(object):
    def setupUi(self, ContributeForm):
        ContributeForm.setObjectName("ContributeForm")
        ContributeForm.resize(1200, 755)
        self.questionTextEdit = QtWidgets.QTextEdit(ContributeForm)
        self.questionTextEdit.setGeometry(QtCore.QRect(150, 60, 431, 501))
        self.questionTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionTextEdit.setObjectName("questionTextEdit")
        self.userNamelabel = QtWidgets.QLabel(ContributeForm)
        self.userNamelabel.setGeometry(QtCore.QRect(1000, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")
        self.questionTipsLabel = QtWidgets.QLabel(ContributeForm)
        self.questionTipsLabel.setGeometry(QtCore.QRect(160, 30, 431, 31))
        self.questionTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.questionTipsLabel.setObjectName("questionTipsLabel")
        self.openFileForQuestionButton = QtWidgets.QPushButton(ContributeForm)
        self.openFileForQuestionButton.setGeometry(QtCore.QRect(280, 620, 161, 41))
        self.openFileForQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.openFileForQuestionButton.setObjectName("openFileForQuestionButton")
        self.answerTextEdit = QtWidgets.QTextEdit(ContributeForm)
        self.answerTextEdit.setGeometry(QtCore.QRect(610, 60, 431, 501))
        self.answerTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.answerTextEdit.setObjectName("answerTextEdit")
        self.openFileForAnswerButton = QtWidgets.QPushButton(ContributeForm)
        self.openFileForAnswerButton.setGeometry(QtCore.QRect(760, 620, 161, 41))
        self.openFileForAnswerButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.openFileForAnswerButton.setObjectName("openFileForAnswerButton")
        self.questionTypeComboBox = QtWidgets.QComboBox(ContributeForm)
        self.questionTypeComboBox.setGeometry(QtCore.QRect(20, 50, 99, 31))
        self.questionTypeComboBox.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionTypeComboBox.setObjectName("questionTypeComboBox")
        self.goBackButton = QtWidgets.QPushButton(ContributeForm)
        self.goBackButton.setGeometry(QtCore.QRect(1050, 690, 91, 41))
        self.goBackButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.goBackButton.setObjectName("goBackButton")
        self.answerTipsLabel = QtWidgets.QLabel(ContributeForm)
        self.answerTipsLabel.setGeometry(QtCore.QRect(620, 30, 411, 31))
        self.answerTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.answerTipsLabel.setObjectName("answerTipsLabel")
        self.questionLabel = QtWidgets.QLabel(ContributeForm)
        self.questionLabel.setGeometry(QtCore.QRect(30, 20, 81, 31))
        self.questionLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionLabel.setObjectName("questionLabel")
        self.confirmButton = QtWidgets.QPushButton(ContributeForm)
        self.confirmButton.setGeometry(QtCore.QRect(550, 650, 91, 41))
        self.confirmButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.confirmButton.setObjectName("confirmButton")
        self.thanksTipsLabel = QtWidgets.QLabel(ContributeForm)
        self.thanksTipsLabel.setGeometry(QtCore.QRect(530, 580, 431, 31))
        self.thanksTipsLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.thanksTipsLabel.setObjectName("thanksTipsLabel")
        self.clearQuestionButton = QtWidgets.QPushButton(ContributeForm)
        self.clearQuestionButton.setGeometry(QtCore.QRect(280, 680, 161, 41))
        self.clearQuestionButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.clearQuestionButton.setObjectName("clearQuestionButton")
        self.clearAnswerButton = QtWidgets.QPushButton(ContributeForm)
        self.clearAnswerButton.setGeometry(QtCore.QRect(760, 680, 161, 41))
        self.clearAnswerButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.clearAnswerButton.setObjectName("clearAnswerButton")

        self.retranslateUi(ContributeForm)
        QtCore.QMetaObject.connectSlotsByName(ContributeForm)

    def retranslateUi(self, ContributeForm):
        _translate = QtCore.QCoreApplication.translate
        ContributeForm.setWindowTitle(_translate("ContributeForm", "小航搜题-贡献题目"))
        self.userNamelabel.setText(_translate("ContributeForm", "用户名：蛤蛤蛤蛤蛤蛤"))
        self.questionTipsLabel.setText(_translate("ContributeForm", "上传题目不能为空"))
        self.openFileForQuestionButton.setText(_translate("ContributeForm", "上传题目"))
        self.openFileForAnswerButton.setText(_translate("ContributeForm", "上传答案"))
        self.goBackButton.setText(_translate("ContributeForm", "返回"))
        self.answerTipsLabel.setText(_translate("ContributeForm", "上传答案不能为空"))
        self.questionLabel.setText(_translate("ContributeForm", "题目类型"))
        self.confirmButton.setText(_translate("ContributeForm", "确认"))
        self.thanksTipsLabel.setText(_translate("ContributeForm", "感谢您的无私奉献！"))
        self.clearQuestionButton.setText(_translate("ContributeForm", "清空题目"))
        self.clearAnswerButton.setText(_translate("ContributeForm", "清空答案"))

