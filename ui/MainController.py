import re

from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog
from ui.Main import Ui_MainForm
from PyQt5.QtCore import pyqtSignal
from HistoryController import History_controller

_debug = False


class Main_controller(QtWidgets.QMainWindow):
	rightfulFormat = re.compile(r'^.*(\.jpg|\.png|\.png|\.pdf|\.txt)$')
	logOutSignal = pyqtSignal()  # 回到登陆界面
	
	def __init__(self, userName: str, userPassword: str):
		super(Main_controller, self).__init__()
		self.ui = Ui_MainForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		# 子界面
		self.history_ui = History_controller(userName, userPassword)
		self.setup_control()
		
	def _reshow(self):
		self.history_ui.hide()
		self.show()
		
	def _hide(self, sel: int):
		self.hide()
		if sel == 0:
			self.history_ui.show()
		
	def setup_control(self):
		self.ui.scheduleLabel.clear()
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		self.history_ui.goBackToMainSignal.connect(self._reshow)
		self.ui.favoriteQuestionButton.clicked.connect(self.favoriteQuestionButtonClicked)
		self.ui.reciteQuestionButton.clicked.connect(self.reciteQuestionButtonClicked)
		self.ui.historyQuestionButton.clicked.connect(self.historyQuestionButtonClicked)
		self.ui.wrongQuestionButton.clicked.connect(self.wrongQuestionButtonClicked)
		self.ui.openFileButton.clicked.connect(self.openFileButtonClicked)
		self.ui.searchButton.clicked.connect(self.searchButtonClicked)
		self.ui.clearButton.clicked.connect(self.clearButtonClicked)
		self.ui.quizButton.clicked.connect(self.quizButtonClicked)
		self.ui.logoutButton.clicked.connect(self.logoutButtonClicked)
	
	def favoriteQuestionButtonClicked(self):
		pass
	
	def reciteQuestionButtonClicked(self):
		pass
	
	def historyQuestionButtonClicked(self):
		self._hide(0)
	
	def wrongQuestionButtonClicked(self):
		pass
	
	def openFileButtonClicked(self):
		self.ui.scheduleLabel.clear()
		filePath, fileType = QFileDialog.getOpenFileName(self, "Open file", "./")
		if _debug:
			print(filePath, fileType)
		if re.match(self.rightfulFormat, filePath):
			if _debug:
				print(re.match(self.rightfulFormat, filePath).group(0))
			self.ui.scheduleLabel.setText("正在识别文件，请耐心等待。。。")
			content = getFileContent(filePath)
			self.ui.scheduleLabel.clear()
			if content:
				self.ui.questionTextEdit.append(content)
			else:
				self.ui.scheduleLabel.setText("什么都没识别到，请再次尝试")
		else:
			self.ui.scheduleLabel.setText("无法识别该文件类型，请再次尝试")
	
	def searchButtonClicked(self):
		pass
	
	def clearButtonClicked(self):
		self.ui.questionTextEdit.clear()
	
	def quizButtonClicked(self):
		pass
	
	def logoutButtonClicked(self):
		self.logOutSignal.emit()
	
	
# ----- 补全的代码 ----- # TODO
def getFileContent(filePath: str) -> str:  # jpg, png, txt, pdf
	return "fuck BUAA!!!"

