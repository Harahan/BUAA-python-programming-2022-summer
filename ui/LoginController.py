import re

from PyQt5 import QtGui

from ui.MainController import Main_controller
from ui.RegisterController import RegisterForm_controller
from PyQt5.Qt import *
from ui.Login import Ui_LoginForm

_debug = False


class LoginForm_controller(QMainWindow):
	empty = re.compile(r"^\s*$")
	
	def __init__(self):
		super(LoginForm_controller, self).__init__()
		self.main_ui = None
		self.register_ui = RegisterForm_controller()
		self.ui = Ui_LoginForm()
		self.ui.setupUi(self)
		self.setup_control()
		
	def _prohibitButtonAndInput(self):
		self.ui.signInButton.setDisabled(True)
		self.ui.signUpButton.setDisabled(True)
		self.ui.userNameInput.setDisabled(True)
		self.ui.userPasswordInput.setDisabled(True)
		
	def _reworkButtonAndInput(self):
		self.ui.signInButton.setDisabled(False)
		self.ui.signUpButton.setDisabled(False)
		self.ui.userNameInput.setDisabled(False)
		self.ui.userPasswordInput.setDisabled(False)
		
	def _clearLabel(self):
		self.ui.userPasswordTipsLabel.clear()
		self.ui.userNameTipsLabel.clear()
		
	def _clearInput(self):
		self.ui.userNameInput.clear()
		self.ui.userPasswordInput.clear()
	
	def _hide(self, userName, userPassword):
		self.hide()
		self.main_ui = Main_controller(userName, userPassword)
		self.main_ui.logOutSignal.connect(self._reshow)
		self.main_ui.show()
	
	def _reshow(self):
		self.main_ui: Main_controller
		self.main_ui.close()
		self.show()
		
	def setup_control(self):
		self.ui.userNameTipsLabel.clear()
		self.ui.userPasswordTipsLabel.clear()
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.register_ui.reworkLoginButtonSignal.connect(self._reworkButtonAndInput)
		self.ui.signInButton.clicked.connect(self.signInButtonClicked)
		self.ui.signUpButton.clicked.connect(self.signUpButtonClicked)
	
	def signInButtonClicked(self):
		self._clearLabel()
		flag = True
		userName = str(self.ui.userNameInput.text())
		userPassword = str(self.ui.userPasswordInput.text())
		if _debug:
			print("Login:")
			print("userName: [" + userName + "], userPassword: [" + userPassword + "]")
		if re.match(self.empty, userName):
			if _debug:
				print("用户名不能为空!")
			self.ui.userNameTipsLabel.setText("用户名不能为空!")
			flag = False
		if flag and len(userName) > 6:
			self.ui.userNameTipsLabel.setText("用户名不能超过6位!")
			flag = False
		if re.match(self.empty, userPassword):
			if _debug:
				print("用户密码不能为空!")
			self.ui.userPasswordTipsLabel.setText("用户密码不能为空!")
			flag = False
		if flag and not checkUserNameAlive(userName):
			if _debug:
				print("用户名不存在!")
			self.ui.userNameTipsLabel.setText("用户名不存在!")
		elif flag and not checkUserPassword(userName, userPassword):
			if _debug:
				print("用户密码错误!")
			self.ui.userPasswordTipsLabel.setText("用户密码错误!")
		elif flag:
			self._hide(userName, userPassword)
		
	def signUpButtonClicked(self):
		self._prohibitButtonAndInput()
		self.register_ui.show()
		
		
# ----- 补全的的部分 ----- # TODO
def checkUserNameAlive(name: str) -> bool:
	return True
	
	
def checkUserPassword(name: str, password: str) -> bool:
	return True
