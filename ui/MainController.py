import re

from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog
from ui.Main import Ui_MainForm
from PyQt5.QtCore import pyqtSignal
from HistoryController import History_controller
from WrongController import Wrong_controller
from FavoriteController import Favorite_controller
from ReciteController import Recite_controller
from SearchingResultController import SearchingResult_controller
from WriteOffController import WriteOffController
from ContributeController import Contribute_controller

_debug = True


class Main_controller(QtWidgets.QMainWindow):
	rightfulFormat = re.compile(r'^.*(\.jpg|\.png|\.png|\.pdf|\.txt|\.jpeg)$')
	empty = re.compile(r"^\s*$")
	logOutSignal = pyqtSignal()  # 回到登陆界面
	
	def __init__(self, userName: str, userPassword: str):
		super(Main_controller, self).__init__()
		self.ui = Ui_MainForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		# 子界面
		self.history_ui = History_controller(userName, userPassword)
		self.wrong_ui = Wrong_controller(userName, userPassword)
		self.favorite_ui = Favorite_controller(userName, userPassword)
		self.recite_ui = Recite_controller(userName, userPassword)
		self.searchingResult_ui = SearchingResult_controller(userName, userPassword, '')
		self.writeOff_ui = WriteOffController(userName, userPassword)
		self.contribute_ui = Contribute_controller(userName, userPassword)
		self.setup_control()
		
	def _reshow(self, sel: int):
		if sel == 0:
			self.history_ui.hide()
		elif sel == 1:
			self.wrong_ui.hide()
		elif sel == 2:
			self.favorite_ui.hide()
		elif sel == 3:
			self.recite_ui.hide()
		elif sel == 4:
			self.searchingResult_ui.hide()
		elif sel == 5:
			self.writeOff_ui.hide()
		elif sel == 6:
			self.contribute_ui.hide()
		self.show()
		
	def _hide(self, sel: int):
		self.hide()
		if sel == 0:
			self.history_ui.show()
		elif sel == 1:
			self.wrong_ui.show()
		elif sel == 2:
			self.favorite_ui.show()
		elif sel == 3:
			self.recite_ui.show()
		elif sel == 4:
			self.searchingResult_ui.show()
		elif sel == 5:
			self.writeOff_ui.show()
		elif sel == 6:
			self.contribute_ui.show()
		
	def setup_control(self):
		self.ui.scheduleLabel.clear()
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		# 返回
		self.history_ui.goBackToMainSignal.connect(self._reshow)
		self.wrong_ui.goBackToMainSignal.connect(self._reshow)
		self.favorite_ui.goBackToMainSignal.connect(self._reshow)
		self.recite_ui.goBackToMainSignal.connect(self._reshow)
		self.searchingResult_ui.goBackToMainSignal.connect(self._reshow)
		self.writeOff_ui.goBackToMainSignal.connect(self._reshow)
		self.writeOff_ui.goBackToLoginSignal.connect(self.logoutButtonClicked)
		self.contribute_ui.goBackToMainSignal.connect(self._reshow)
		
		self.ui.favoriteQuestionButton.clicked.connect(self.favoriteQuestionButtonClicked)
		self.ui.reciteQuestionButton.clicked.connect(self.reciteQuestionButtonClicked)
		self.ui.historyQuestionButton.clicked.connect(self.historyQuestionButtonClicked)
		self.ui.wrongQuestionButton.clicked.connect(self.wrongQuestionButtonClicked)
		self.ui.openFileButton.clicked.connect(self.openFileButtonClicked)
		self.ui.searchButton.clicked.connect(self.searchButtonClicked)
		self.ui.clearButton.clicked.connect(self.clearButtonClicked)
		self.ui.quizButton.clicked.connect(self.quizButtonClicked)
		self.ui.logoutButton.clicked.connect(self.logoutButtonClicked)
		self.ui.contributeButton.clicked.connect(self.contributeButtonClicked)
		self.ui.writeOffButton.clicked.connect(self.writeOffButtonClicked)
	
	def favoriteQuestionButtonClicked(self):
		self.ui.scheduleLabel.clear()
		self._hide(2)
	
	def reciteQuestionButtonClicked(self):
		self.ui.scheduleLabel.clear()
		self._hide(3)
	
	def historyQuestionButtonClicked(self):
		self.ui.scheduleLabel.clear()
		self._hide(0)
	
	def wrongQuestionButtonClicked(self):
		self.ui.scheduleLabel.clear()
		self._hide(1)
	
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
		self.ui.scheduleLabel.clear()
		question = self.ui.questionTextEdit.toPlainText()
		if _debug:
			print(question)
		if re.match(self.empty, question):
			self.ui.scheduleLabel.setText("搜索内容不应为空！")
		else:
			self.ui.scheduleLabel.setText("正在搜索中，请耐心等待。。。")
			self.searchingResult_ui.questionAndAnswer = (question, getAnswer(question))
			self.ui.scheduleLabel.clear()
			self._hide(4)
	
	def clearButtonClicked(self):
		self.ui.scheduleLabel.clear()
		self.ui.questionTextEdit.clear()
	
	def quizButtonClicked(self):  # TODO
		self.ui.scheduleLabel.clear()
		pass
	
	def logoutButtonClicked(self):
		self.ui.scheduleLabel.clear()
		self.logOutSignal.emit()
		
	def contributeButtonClicked(self):
		self.ui.scheduleLabel.clear()
		self._hide(6)
	
	def writeOffButtonClicked(self):
		self._hide(5)
	
	
# ----- 补全的代码 ----- # TODO
def getFileContent(filePath: str) -> str:  # jpg, png, txt, pdf, jpeg
	return "fuck BUAA!!!"


def getAnswer(question: str) -> str:   # 可以返回一个空的字符串，如果没有
	return ""

