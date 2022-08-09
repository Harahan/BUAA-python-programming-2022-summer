from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *

from db.user import User
from ui.TetrisResult import Ui_TetrisResultForm


class TetrisResult_controller(QtWidgets.QMainWindow):
	goBackToMainSignal = pyqtSignal(int)
	
	def __init__(self, userName: str, userPassword: str, x: int = 0):
		super(TetrisResult_controller, self).__init__()
		self.x = x
		self.userName = userName
		self.userPassword = userPassword
		self.ui = Ui_TetrisResultForm()
		self.ui.setupUi(self)
		self.setup_control()
		
	def set(self, x: int):
		self.x = x
		
	def setup_control(self):
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		self.ui.label.clear()
		self.ui.lineEdit.setReadOnly(True)
		self.ui.lineEdit_2.setReadOnly(True)
		self.ui.lineEdit_3.setReadOnly(True)
		self.ui.againButton.clicked.connect(self.againButtonClicked)
		self.ui.goBackButton.clicked.connect(self.goBackButtonClicked)
		
	def againButtonClicked(self):
		self.ui.label.setText('你觉得可能吗？')
		
	def goBackButtonClicked(self):
		self.goBackToMainSignal.emit(9)
		
	def showEvent(self, a0: QtGui.QShowEvent):
		self.ui.label.clear()
		self.ui.lineEdit_3.setText(str(self.x))
		x, y = getHighestScore()
		self.ui.lineEdit_2.setText(str(y))
		self.ui.lineEdit.setText(str(x))
		if y < self.x:
			restoreHighestScore(self.x)
		a0.accept()
		
		
# ----- 补全的代码 ----- # TODO
def getHighestScore() -> (int, int):
	user = User()
	return user.get_tetris_score()  # system, user


def restoreHighestScore(x: int):
	user = User()
	user.add_tetris_score(x)
	
# finish
	