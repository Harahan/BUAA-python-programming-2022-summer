from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from ui.SubjectiveItemQuiz import Ui_SubjectiveItemQuizForm


class SubjectiveItemQuiz_controller(QtWidgets.QMainWindow):
	goNextSignal = pyqtSignal()
	goPreSignal = pyqtSignal()
	goToResultSignal = pyqtSignal()
	
	def __init__(self, userName: str, userPassword: str, question: str, answer: str):
		super(SubjectiveItemQuiz_controller, self).__init__()
		self.nxt = None
		self.pre = None
		self.ui = Ui_SubjectiveItemQuizForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.question = question
		self.answer = answer
		self.setup_control()
		
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
		
	def setPreAndNext(self, pre: int, nxt: int):
		self.pre = pre
		self.nxt = nxt
	
	def confirmButtonClicked(self):
		self.ui.scheduleLabel.clear()  # TODO
	
	def clearButtonClicked(self):
		self.ui.scheduleLabel.clear()
		self.ui.writeTextEdit.clear()
	
	def goBackButtonClicked(self):  # TODO
		pass
	
	def nextQuestionButtonClicked(self):  # TODO
		pass
	
	def preQuestionButtonClicked(self):  # TODO
		pass


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
