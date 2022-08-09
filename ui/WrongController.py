from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *

from db.user import User
from ui.Wrong import Ui_WrongForm
import re


class Wrong_controller(QtWidgets.QMainWindow):
	goBackToMainSignal = pyqtSignal(int)
	digit = re.compile(r'^\d+$')
	
	def __init__(self, userName: str, userPassword: str):
		super(Wrong_controller, self).__init__()
		self.ui = Ui_WrongForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.wrongQuestionAndAnswer = getWrongQuestionAndAnswer()
		self.currentPage = 1
		self.setup_control()
		
	def _checkNumber(self, number: int):
		maxNumber = len(self.wrongQuestionAndAnswer)
		if number > maxNumber:
			self.ui.scheduleTipsLabel.setText("已经到底了，什么也没有了。。。")
			self.ui.questionTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
			self.ui.rightAnswerTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
			self.ui.wrongAnswerTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
		elif number <= 0:
			self.ui.scheduleTipsLabel.setText("没有更近的错题了。。。")
			self.ui.questionTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
			self.ui.rightAnswerTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
			self.ui.wrongAnswerTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
		else:
			return True
		return False
		
	def _showQuestionAndAnswer(self, number: int):
		self.ui.scheduleTipsLabel.clear()
		self.ui.questionTextEdit.clear()
		self.ui.rightAnswerTextEdit.clear()
		self.ui.wrongAnswerTextEdit.clear()
		self.ui.questionTextEdit.setStyleSheet("background-image:url(); font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
		self.ui.rightAnswerTextEdit.setStyleSheet("background-image:url(); font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
		self.ui.wrongAnswerTextEdit.setStyleSheet("background-image:url(); font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
		self.currentPage = number
		self.ui.questionNumberLineEdit.setText(str(number))
		if self._checkNumber(number):
			self.ui.questionTextEdit.setText(self.wrongQuestionAndAnswer[number - 1][0])
			self.ui.rightAnswerTextEdit.setText(self.wrongQuestionAndAnswer[number - 1][1])
			if self.wrongQuestionAndAnswer[number - 1][2] != '':
				self.ui.wrongAnswerTextEdit.setText(self.wrongQuestionAndAnswer[number - 1][2])
			else:
				self.ui.wrongAnswerTextEdit.setText("您好像没有提交过该题的答案呀。。。")
			
	def _initParameter(self):
		self._showQuestionAndAnswer(1)
		self.ui.totQuestionLabel.setText('/' + str(len(self.wrongQuestionAndAnswer)))
		self.ui.scheduleTipsLabel.clear()
		
	def setup_control(self):
		self._initParameter()
		self.ui.questionTextEdit.setReadOnly(True)
		self.ui.rightAnswerTextEdit.setReadOnly(True)
		self.ui.wrongAnswerTextEdit.setReadOnly(True)
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.ui.changeQuestionButton.setIcon(QIcon("../img/rightArrow.jpg"))
		self.ui.changeQuestionButton.setIconSize(QSize(15, 15))
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		self.ui.clearCurrentQuestionButton.clicked.connect(self.clearCurrentQuestionButtonClicked)
		self.ui.nextQuestionButton.clicked.connect(self.nextQuestionButtonClicked)
		self.ui.preQuestionButton.clicked.connect(self.preQuestionButtonClicked)
		self.ui.addToFavoriteQuestionButton.clicked.connect(self.addToFavoriteQuestionButtonClicked)
		self.ui.addToReciteQuestionButton.clicked.connect(self.addToReciteQuestionButtonClicked)
		self.ui.goBackButton.clicked.connect(self.goBackButtonClicked)
		self.ui.changeQuestionButton.clicked.connect(self.changeQuestionButtonClicked)

	def clearCurrentQuestionButtonClicked(self):
		if self._checkNumber(self.currentPage):
			if clearCurrentWrongQuestion(self.wrongQuestionAndAnswer[self.currentPage - 1]):
				self.ui.scheduleTipsLabel.setText("清除成功，下一次进来它就消失了！")
			else:
				self.ui.scheduleTipsLabel.setText("该题在刚才已被清除！")
	
	def nextQuestionButtonClicked(self):
		self._showQuestionAndAnswer(self.currentPage + 1)
	
	def preQuestionButtonClicked(self):
		self._showQuestionAndAnswer(self.currentPage - 1)
	
	def addToFavoriteQuestionButtonClicked(self):
		if self._checkNumber(self.currentPage):
			if addToFavoriteQuestion(self.wrongQuestionAndAnswer[self.currentPage - 1]):
				self.ui.scheduleTipsLabel.setText("已成功加入我喜欢的问题！")
			else:
				self.ui.scheduleTipsLabel.setText("该题在我喜欢的问题中已存在！")
	
	def addToReciteQuestionButtonClicked(self):
		if self._checkNumber(self.currentPage):
			if addToReciteQuestion(self.wrongQuestionAndAnswer[self.currentPage - 1]):
				self.ui.scheduleTipsLabel.setText("已成功加入我的背题集！")
			else:
				self.ui.scheduleTipsLabel.setText("该题在我的背题集中已存在！")
	
	def goBackButtonClicked(self):
		self.goBackToMainSignal.emit(1)
	
	def changeQuestionButtonClicked(self):
		p = self.ui.questionNumberLineEdit.text()
		if re.match(self.digit, p):
			number = int(p)
			self._showQuestionAndAnswer(number)
	
	def showEvent(self, a0: QtGui.QShowEvent):
		self.wrongQuestionAndAnswer = getWrongQuestionAndAnswer()
		self._initParameter()
		a0.accept()
	
	
def getWrongQuestionAndAnswer() -> [(str, str, str, int)]:  # question, right answer, wrong answer, question_id
	user = User()
	return user.get_wrong_table()


def addToFavoriteQuestion(questionAndAnswer: (str, str, str, int)) -> bool:  # Q, right A
	user = User()
	return user.add_like(questionAndAnswer[3])


def addToReciteQuestion(questionAndAnswer: (str, str, str, int)) -> bool:
	user = User()
	return user.add_recite(questionAndAnswer[3])


def clearCurrentWrongQuestion(questionAndAnswer: (str, str, str ,int)) -> bool:
	user = User()
	return user.delete_data('wrong', questionAndAnswer[3])

# finish
