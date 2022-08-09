from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *

from db.user import User
from ui.SearchingResult import Ui_SearchingResultForm
import re


class SearchingResult_controller(QtWidgets.QMainWindow):
	goBackToMainSignal = pyqtSignal(int)
	digit = re.compile(r'^\d+$')
	
	def __init__(self, userName: str, userPassword: str, questionAndAnswer: (str, str, int)):
		super(SearchingResult_controller, self).__init__()
		self.ui = Ui_SearchingResultForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.questionAndAnswer = questionAndAnswer
		self.setup_control()
	
	def _initParameter(self):
		self.ui.scheduleTipsLabel.clear()
		self.ui.questionTextEdit.setReadOnly(True)
		self.ui.answerTextEdit.setReadOnly(True)
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.ui.userNamelabel.setText("用户名：" + self.userName)
	
	def setup_control(self):
		self._initParameter()
		self.ui.addToFavoriteQuestionButton.clicked.connect(self.addToFavoriteQuestionButtonClicked)
		self.ui.addToReciteQuestionButton.clicked.connect(self.addToReciteQuestionButtonClicked)
		self.ui.addToWrongQuestionButton.clicked.connect(self.addToWrongQuestionButtonClicked)
		self.ui.goBackButton.clicked.connect(self.goBackButtonClicked)
	
	def addToFavoriteQuestionButtonClicked(self):
		if addToFavoriteQuestion(self.questionAndAnswer):
			self.ui.scheduleTipsLabel.setText("已成功加入我喜欢的问题！")
		else:
			self.ui.scheduleTipsLabel.setText("该题在我喜欢的问题中已存在！")
	
	def addToReciteQuestionButtonClicked(self):
		if addToReciteQuestion(self.questionAndAnswer):
			self.ui.scheduleTipsLabel.setText("已成功加入我的背题集！")
		else:
			self.ui.scheduleTipsLabel.setText("该题在我的背题集中已存在！")
	
	def addToWrongQuestionButtonClicked(self):
		if addToWrongQuestion(self.questionAndAnswer):
			self.ui.scheduleTipsLabel.setText("已成功加入我的错题本！")
		else:
			self.ui.scheduleTipsLabel.setText("该题在我的错题本中已存在！")
	
	def goBackButtonClicked(self):
		self.goBackToMainSignal.emit(4)
		self._initParameter()
	
	def showEvent(self, a0: QtGui.QShowEvent):
		self.ui.scheduleTipsLabel.clear()
		self.ui.addToFavoriteQuestionButton.setDisabled(False)
		self.ui.addToWrongQuestionButton.setDisabled(False)
		self.ui.addToReciteQuestionButton.setDisabled(False)
		self.ui.questionTextEdit.setStyleSheet("background-image:url(); font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
		self.ui.answerTextEdit.setStyleSheet("background-image:url(); font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
		self.ui.questionTextEdit.setText(self.questionAndAnswer[0])
		if self.questionAndAnswer[1] != '':
			self.ui.answerTextEdit.setText(self.questionAndAnswer[1])
			addToSearchHistoryQuestion(self.questionAndAnswer)
		else:
			self.ui.answerTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
			self.ui.addToFavoriteQuestionButton.setDisabled(True)
			self.ui.addToWrongQuestionButton.setDisabled(True)
			self.ui.addToReciteQuestionButton.setDisabled(True)
			self.ui.scheduleTipsLabel.setText("什么也没搜到，再试一次吧。。。温馨提示：我们不会保留这种无意义的搜索历史！")
		a0.accept()


# ----- 要提供的函数 ----- # TODO
def addToFavoriteQuestion(questionAndAnswer: (str, str, int)) -> bool:
	user = User()
	return user.add_like(questionAndAnswer[2])


def addToReciteQuestion(questionAndAnswer: (str, str, int)) -> bool:
	user = User()
	return user.add_recite(questionAndAnswer[2])


def addToWrongQuestion(questionAndAnswer: (str, str, int)) -> bool:
	user = User()
	return user.add_wrong_no_answer(questionAndAnswer[2])


def addToSearchHistoryQuestion(questionAndAnswer: (str, str, int)) -> bool:
	user = User()
	return user.add_search_history(questionAndAnswer[2])

# finish
