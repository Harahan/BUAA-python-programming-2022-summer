from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *

from db.user import User
from ui.Favorite import Ui_FavoriteForm
import re


class Favorite_controller(QtWidgets.QMainWindow):
	goBackToMainSignal = pyqtSignal(int)
	digit = re.compile(r'^\d+$')
	
	def __init__(self, userName: str, userPassword: str):
		super(Favorite_controller, self).__init__()
		self.ui = Ui_FavoriteForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.favoriteQuestionAndAnswer = getFavoriteQuestionAndAnswer()
		self.currentPage = 1
		self.setup_control()
		
	def _checkNumber(self, number: int):
		maxNumber = len(self.favoriteQuestionAndAnswer)
		if number > maxNumber:
			self.ui.scheduleTipsLabel.setText("已经到底了，什么也没有了。。。")
			self.ui.questionTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
			self.ui.answerTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
		elif number <= 0:
			self.ui.scheduleTipsLabel.setText("没有更近的题了。。。")
			self.ui.questionTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
			self.ui.answerTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
		else:
			return True
		return False
	
	def _showQuestionAndAnswer(self, number: int):
		self.ui.scheduleTipsLabel.clear()
		self.ui.questionTextEdit.clear()
		self.ui.answerTextEdit.clear()
		self.ui.questionTextEdit.setStyleSheet("background-image:url(); font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
		self.ui.answerTextEdit.setStyleSheet("background-image:url(); font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
		self.currentPage = number
		self.ui.questionNumberLineEdit.setText(str(number))
		if self._checkNumber(number):
			self.ui.questionTextEdit.setText(self.favoriteQuestionAndAnswer[number - 1][0])
			self.ui.answerTextEdit.setText(self.favoriteQuestionAndAnswer[number - 1][1])
	
	def _initParameter(self):
		self._showQuestionAndAnswer(1)
		self.ui.totQuestionLabel.setText('/' + str(len(self.favoriteQuestionAndAnswer)))
		self.ui.scheduleTipsLabel.clear()
		self.ui.questionTextEdit.setReadOnly(True)
		self.ui.answerTextEdit.setReadOnly(True)
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.ui.changeQuestionButton.setIcon(QIcon("../img/rightArrow.jpg"))
		self.ui.changeQuestionButton.setIconSize(QSize(15, 15))
		self.ui.userNamelabel.setText("用户名：" + self.userName)
	
	def setup_control(self):
		self._initParameter()
		self.ui.clearCurrentQuestionButton.clicked.connect(self.clearCurrentQuestionButtonClicked)
		self.ui.nextQuestionButton.clicked.connect(self.nextQuestionButtonClicked)
		self.ui.preQuestionButton.clicked.connect(self.preQuestionButtonClicked)
		self.ui.addToWrongQuestionButton.clicked.connect(self.addToWrongQuestionButtonClicked)
		self.ui.addToReciteQuestionButton.clicked.connect(self.addToReciteQuestionButtonClicked)
		self.ui.goBackButton.clicked.connect(self.goBackButtonClicked)
		self.ui.changeQuestionButton.clicked.connect(self.changeQuestionButtonClicked)
	
	def clearCurrentQuestionButtonClicked(self):
		if self._checkNumber(self.currentPage):
			if clearCurrentFavoriteQuestion(self.favoriteQuestionAndAnswer[self.currentPage - 1]):
				self.ui.scheduleTipsLabel.setText("清除成功，下一次进来它就消失了！")
			else:
				self.ui.scheduleTipsLabel.setText("该题在刚才已被清除！")
	
	def nextQuestionButtonClicked(self):
		self._showQuestionAndAnswer(self.currentPage + 1)
	
	def preQuestionButtonClicked(self):
		self._showQuestionAndAnswer(self.currentPage - 1)
	
	def addToWrongQuestionButtonClicked(self):
		if self._checkNumber(self.currentPage):
			if addToWrongQuestion(self.favoriteQuestionAndAnswer[self.currentPage - 1]):
				self.ui.scheduleTipsLabel.setText("已成功加入我的错题本！")
			else:
				self.ui.scheduleTipsLabel.setText("该题在我的错题本中已存在！")
	
	def addToReciteQuestionButtonClicked(self):
		if self._checkNumber(self.currentPage):
			if addToReciteQuestion(self.favoriteQuestionAndAnswer[self.currentPage - 1]):
				self.ui.scheduleTipsLabel.setText("已成功加入我的背题集！")
			else:
				self.ui.scheduleTipsLabel.setText("该题在我的背题集中已存在！")
	
	def goBackButtonClicked(self):
		self.goBackToMainSignal.emit(2)
		self._initParameter()
	
	def changeQuestionButtonClicked(self):
		p = self.ui.questionNumberLineEdit.text()
		if re.match(self.digit, p):
			number = int(p)
			self._showQuestionAndAnswer(number)
	
	def showEvent(self, a0: QtGui.QShowEvent):
		self.favoriteQuestionAndAnswer = getFavoriteQuestionAndAnswer()
		a0.accept()


# ----- 要提供的函数 ----- # TODO
def getFavoriteQuestionAndAnswer() -> [(str, str, int)]:  # question, right answer, question_id
	user = User()
	return user.get_like_table()


def addToWrongQuestion(questionAndAnswer: (str, str, int)) -> bool:  # Q, right A
	user = User()
	return user.add_wrong_no_answer(questionAndAnswer[2])


def addToReciteQuestion(questionAndAnswer: (str, str, int)) -> bool:
	user = User()
	return user.add_recite(questionAndAnswer[2])


def clearCurrentFavoriteQuestion(questionAndAnswer: (str, str, int)) -> bool:
	user = User()
	return user.delete_data('like', questionAndAnswer[2])

# finish
