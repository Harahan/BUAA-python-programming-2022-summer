import sys
from LoginController import LoginForm_controller
from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
# from MainController import Main_controller

if __name__ == "__main__":
	app = QApplication(sys.argv)
	apply_stylesheet(app, theme='dark_teal.xml')
	testWin = LoginForm_controller()
	testWin.show()
	sys.exit(app.exec_())
	