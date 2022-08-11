import os
import sys

import easyocr

from OCR_and_PDF import fileProcess
from ui.LoginController import LoginForm_controller
from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
import db.initial
from db.questionBank import QuestionBank
import db.DB


def runGui():
	os.chdir('./ui')
	app = QApplication(sys.argv)
	apply_stylesheet(app, theme='dark_teal.xml')
	testWin = LoginForm_controller()
	testWin.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	db.DB.data_path = db.initial.initial()
	fileProcess.OCR_reader = easyocr.Reader(['ch_sim', 'en'])
	qb = QuestionBank()
	runGui()
