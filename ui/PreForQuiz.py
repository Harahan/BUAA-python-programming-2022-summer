# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreForQuiz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreForQuizForm(object):
    def setupUi(self, PreForQuizForm):
        PreForQuizForm.setObjectName("PreForQuizForm")
        PreForQuizForm.resize(894, 553)
        self.comboBox = QtWidgets.QComboBox(PreForQuizForm)
        self.comboBox.setGeometry(QtCore.QRect(70, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.comboBox.setObjectName("comboBox")
        self.historyLabel = QtWidgets.QLabel(PreForQuizForm)
        self.historyLabel.setGeometry(QtCore.QRect(260, 60, 131, 41))
        self.historyLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.historyLabel.setObjectName("historyLabel")
        self.favoriteLabel = QtWidgets.QLabel(PreForQuizForm)
        self.favoriteLabel.setGeometry(QtCore.QRect(260, 150, 131, 41))
        self.favoriteLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.favoriteLabel.setObjectName("favoriteLabel")
        self.wrongLabel = QtWidgets.QLabel(PreForQuizForm)
        self.wrongLabel.setGeometry(QtCore.QRect(260, 240, 131, 41))
        self.wrongLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.wrongLabel.setObjectName("wrongLabel")
        self.reciteLabel = QtWidgets.QLabel(PreForQuizForm)
        self.reciteLabel.setGeometry(QtCore.QRect(260, 330, 131, 41))
        self.reciteLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.reciteLabel.setObjectName("reciteLabel")
        self.historyLineEdit = QtWidgets.QLineEdit(PreForQuizForm)
        self.historyLineEdit.setGeometry(QtCore.QRect(420, 64, 113, 31))
        self.historyLineEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.historyLineEdit.setObjectName("historyLineEdit")
        self.favoriteLineEdit = QtWidgets.QLineEdit(PreForQuizForm)
        self.favoriteLineEdit.setGeometry(QtCore.QRect(420, 150, 113, 31))
        self.favoriteLineEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.favoriteLineEdit.setObjectName("favoriteLineEdit")
        self.wrongLineEdit = QtWidgets.QLineEdit(PreForQuizForm)
        self.wrongLineEdit.setGeometry(QtCore.QRect(420, 240, 113, 31))
        self.wrongLineEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.wrongLineEdit.setObjectName("wrongLineEdit")
        self.reciteLineEdit = QtWidgets.QLineEdit(PreForQuizForm)
        self.reciteLineEdit.setGeometry(QtCore.QRect(420, 330, 113, 31))
        self.reciteLineEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.reciteLineEdit.setObjectName("reciteLineEdit")
        self.historyNumberLabel = QtWidgets.QLabel(PreForQuizForm)
        self.historyNumberLabel.setGeometry(QtCore.QRect(550, 60, 91, 41))
        self.historyNumberLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.historyNumberLabel.setObjectName("historyNumberLabel")
        self.originLabel = QtWidgets.QLabel(PreForQuizForm)
        self.originLabel.setGeometry(QtCore.QRect(260, 420, 131, 41))
        self.originLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.originLabel.setObjectName("originLabel")
        self.originLineEdit = QtWidgets.QLineEdit(PreForQuizForm)
        self.originLineEdit.setGeometry(QtCore.QRect(420, 420, 113, 31))
        self.originLineEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.originLineEdit.setObjectName("originLineEdit")
        self.favoriteNumberLabel = QtWidgets.QLabel(PreForQuizForm)
        self.favoriteNumberLabel.setGeometry(QtCore.QRect(550, 150, 91, 41))
        self.favoriteNumberLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.favoriteNumberLabel.setObjectName("favoriteNumberLabel")
        self.wrongNumberLabel = QtWidgets.QLabel(PreForQuizForm)
        self.wrongNumberLabel.setGeometry(QtCore.QRect(550, 240, 91, 41))
        self.wrongNumberLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.wrongNumberLabel.setObjectName("wrongNumberLabel")
        self.reciteNumberLabel = QtWidgets.QLabel(PreForQuizForm)
        self.reciteNumberLabel.setGeometry(QtCore.QRect(550, 330, 91, 41))
        self.reciteNumberLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.reciteNumberLabel.setObjectName("reciteNumberLabel")
        self.originNumberLabel = QtWidgets.QLabel(PreForQuizForm)
        self.originNumberLabel.setGeometry(QtCore.QRect(550, 420, 91, 41))
        self.originNumberLabel.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.originNumberLabel.setObjectName("originNumberLabel")
        self.confirmButton = QtWidgets.QPushButton(PreForQuizForm)
        self.confirmButton.setGeometry(QtCore.QRect(720, 480, 112, 34))
        self.confirmButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.confirmButton.setObjectName("confirmButton")
        self.tipslabel = QtWidgets.QLabel(PreForQuizForm)
        self.tipslabel.setGeometry(QtCore.QRect(280, 20, 311, 20))
        self.tipslabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);\n"
"")
        self.tipslabel.setObjectName("tipslabel")
        self.userNamelabel = QtWidgets.QLabel(PreForQuizForm)
        self.userNamelabel.setGeometry(QtCore.QRect(690, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")

        self.retranslateUi(PreForQuizForm)
        QtCore.QMetaObject.connectSlotsByName(PreForQuizForm)

    def retranslateUi(self, PreForQuizForm):
        _translate = QtCore.QCoreApplication.translate
        PreForQuizForm.setWindowTitle(_translate("PreForQuizForm", "小测验"))
        self.historyLabel.setText(_translate("PreForQuizForm", "我的历史记录："))
        self.favoriteLabel.setText(_translate("PreForQuizForm", "我喜欢的问题："))
        self.wrongLabel.setText(_translate("PreForQuizForm", "我的错题本："))
        self.reciteLabel.setText(_translate("PreForQuizForm", "我的背题集："))
        self.historyNumberLabel.setText(_translate("PreForQuizForm", "/0"))
        self.originLabel.setText(_translate("PreForQuizForm", "系统题库："))
        self.favoriteNumberLabel.setText(_translate("PreForQuizForm", "/0"))
        self.wrongNumberLabel.setText(_translate("PreForQuizForm", "/0"))
        self.reciteNumberLabel.setText(_translate("PreForQuizForm", "/0"))
        self.originNumberLabel.setText(_translate("PreForQuizForm", "/0"))
        self.confirmButton.setText(_translate("PreForQuizForm", "确定"))
        self.tipslabel.setText(_translate("PreForQuizForm", "所选题目数量不得超过题库数量！"))
        self.userNamelabel.setText(_translate("PreForQuizForm", "用户名：蛤蛤蛤蛤蛤蛤"))

