# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WriteOff.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WriteOffForm(object):
    def setupUi(self, WriteOffForm):
        WriteOffForm.setObjectName("WriteOffForm")
        WriteOffForm.resize(400, 180)
        self.writeOfflabel = QtWidgets.QLabel(WriteOffForm)
        self.writeOfflabel.setGeometry(QtCore.QRect(130, 10, 121, 101))
        self.writeOfflabel.setObjectName("writeOfflabel")
        self.confirmButton = QtWidgets.QPushButton(WriteOffForm)
        self.confirmButton.setGeometry(QtCore.QRect(140, 120, 112, 41))
        self.confirmButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.confirmButton.setObjectName("confirmButton")

        self.retranslateUi(WriteOffForm)
        QtCore.QMetaObject.connectSlotsByName(WriteOffForm)

    def retranslateUi(self, WriteOffForm):
        _translate = QtCore.QCoreApplication.translate
        WriteOffForm.setWindowTitle(_translate("WriteOffForm", "下次再会"))
        self.writeOfflabel.setText(_translate("WriteOffForm", "TextLabel"))
        self.confirmButton.setText(_translate("WriteOffForm", "确认"))

