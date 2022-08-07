import os
import sys
from ui.LoginController import LoginForm_controller
from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet


def runGui():
	os.chdir('./ui')
	app = QApplication(sys.argv)
	apply_stylesheet(app, theme='dark_teal.xml')
	testWin = LoginForm_controller()
	testWin.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	runGui()
	