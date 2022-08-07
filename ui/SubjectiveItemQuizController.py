import re
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from ui.SubjectiveItemQuiz import Ui_SubjectiveItemQuizForm


class SubjectiveItemQuiz_controller(QtWidgets.QMainWindow):
	changeSignal = pyqtSignal(int, int)
	goToResultSignal = pyqtSignal(int)
	resultSignal = pyqtSignal(int, int)
	empty = re.compile(r"^\s*$")
	digit = re.compile(r'^\d+(\.\d+)?$')
	
	def __init__(self, userName: str, userPassword: str, question: str, answer: str, n: int):
		super(SubjectiveItemQuiz_controller, self).__init__()
		self.ui = Ui_SubjectiveItemQuizForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.question = question
		self.answer = answer
		self.setup_control()
		self.n = n
		self.flag = True
		
	def setup_control(self):
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		self.ui.rightAnswerTextEdit.hide()
		self.ui.scheduleLabel.clear()
		self.ui.myAnswerTextEdit.hide()
		self.ui.myAnswerLabel.hide()
		self.ui.rightAnswerLabel.hide()
		self.ui.scoreLabel.hide()
		self.ui.lineEdit.hide()
		self.ui.totScoreLabel.hide()
		self.ui.questionTextEdit.setText(self.question)
		self.ui.questionTextEdit.setReadOnly(True)
		self.ui.nextQuestionButton.clicked.connect(self.nextQuestionButtonClicked)
		self.ui.preQuestionButton.clicked.connect(self.preQuestionButtonClicked)
		self.ui.confirmButton.clicked.connect(self.confirmButtonClicked)
		self.ui.goBackButton.clicked.connect(self.goBackButtonClicked)
		self.ui.clearButton.clicked.connect(self.clearButtonClicked)

	def showEvent(self, a0: QtGui.QShowEvent):
		self.ui.scheduleLabel.clear()
		a0.accept()
	
	def confirmButtonClicked(self):
		self.ui.scheduleLabel.clear()
		if self.flag:
			if not re.match(self.empty, self.ui.writeTextEdit.toPlainText()):
				self.flag = False
				self.ui.rightAnswerTextEdit.setText(self.answer)
				self.ui.myAnswerTextEdit.setText(self.ui.writeTextEdit.toPlainText())
				self.ui.rightAnswerTextEdit.setReadOnly(True)
				self.ui.myAnswerTextEdit.setReadOnly(True)
				self.ui.rightAnswerTextEdit.show()
				self.ui.myAnswerTextEdit.show()
				self.ui.rightAnswerLabel.show()
				self.ui.myAnswerLabel.show()
				self.ui.writeTextEdit.hide()
				self.ui.clearButton.setDisabled(True)
				self.ui.scoreLabel.show()
				self.ui.totScoreLabel.show()
				self.ui.lineEdit.show()
				# 暂时
				self.ui.nextQuestionButton.setDisabled(True)
				self.ui.preQuestionButton.setDisabled(True)
				self.ui.goBackButton.setDisabled(True)
				self.ui.scheduleLabel.setText('请输入分数后再次确认！')
			else:
				self.ui.scheduleLabel.setText('答案不能为空')
		else:
			p = self.ui.lineEdit.text()
			if re.match(self.empty, p):
				self.ui.scheduleLabel.setText('分数不能为空')
			else:
				if re.match(self.digit, p) and 0 <= float(p) <= 10:
					self.ui.confirmButton.setDisabled(True)
					self.ui.nextQuestionButton.setDisabled(False)
					self.ui.preQuestionButton.setDisabled(False)
					self.ui.goBackButton.setDisabled(False)
					addToQuizHistoryQuestion(self.question, self.answer, self.ui.writeTextEdit.toPlainText(), float(p))
					if float(p) < 10:
						addToWrongQuestion(self.question, self.answer, self.ui.writeTextEdit.toPlainText())
					self.resultSignal.emit(float(p), 1)
				else:
					self.ui.scheduleLabel.setText('所输分数不符合要求')
		
	def clearButtonClicked(self):
		self.ui.scheduleLabel.clear()
		self.ui.writeTextEdit.clear()
	
	def goBackButtonClicked(self):
		self.goToResultSignal.emit(self.n)
	
	def nextQuestionButtonClicked(self):
		self.changeSignal.emit(self.n, 1)
	
	def preQuestionButtonClicked(self):
		self.changeSignal.emit(self.n, 0)
		
	def closeEvent(self, a0: QtGui.QCloseEvent):
		a0.accept()
		exit(0)


# ----- 要提供的函数 ----- # TODO
def addToQuizHistoryQuestion(question: str, answer: str, myAnswer: int, score: float):
	"""
	:param question:
	:param answer:
	:param myAnswer: 1011这种二进制数，高位为D
	:param score:
	:return:
	"""
	pass


def addToWrongQuestion(question: str, answer: str, myAnswer: str):
	pass
