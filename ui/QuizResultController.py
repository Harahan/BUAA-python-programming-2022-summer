from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from ui.QuizResult import Ui_QuizResultForm
from ui.Tetris import Tetris
from ui.TerisResultController import TetrisResult_controller


class QuizResult_controller(QtWidgets.QMainWindow):
	goBackToMainSignal = pyqtSignal(int)
	
	def __init__(self, userName: str, userPassword: str, totO: int = 0, totS: int = 0, mO: int = 0, mS: int = 0,
				 x: int = 0, tetrisResult_ui: TetrisResult_controller = None):
		super(QuizResult_controller, self).__init__()
		self.userName = userName
		self.userPassword = userPassword
		self.totO = totO
		self.totS = totS
		self.mO = mO
		self.mS = mS
		self.x = x
		self.ui = Ui_QuizResultForm()
		self.ui.setupUi(self)
		self.setup_control()
		self.tetris = None
		self.tetrisResult_ui = tetrisResult_ui
		
	def set(self, totO: int = 0, totS: int = 0, mO: int = 0, mS: int = 0, x: int = 0):
		self.totO = totO
		self.totS = totS
		self.mO = mO
		self.mS = mS
		self.x = x
		
	def setup_control(self):
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		self.ui.goBackButton.clicked.connect(self.goBackButtonClicked)
		self.ui.relaxButton.clicked.connect(self.relaxButtonClicked)
		
	def goBackButtonClicked(self):
		self.goBackToMainSignal.emit(8)
		
	def relaxButtonClicked(self):
		self.tetris = Tetris(self.tetrisResult_ui)
		self.close()
		self.tetris.show()
	
	def showEvent(self, a0: QtGui.QShowEvent):
		self.ui.textEdit.setText(
			'  恭喜你完成了本次测验，本次测验一共有客观题' + str(self.totO) + '道，主观题以及暂无类型的题' + str(
				self.totS) +
			'道，你完成了' + str(self.mO) + '道客观题，' + str(self.mS) + '道主观题以及暂无类型的题，取得了'
			+ str(self.x) + '/100的总成绩（每题均按十分满分折合而成），可以选择直接返回主界面或者打把小游戏放松一下啦！')
		a0.accept()
	