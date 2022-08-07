from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from ui.ObjectiveItemQuiz import Ui_ObjectiveItemQuizForm


class ObjectiveItemQuiz_controller(QtWidgets.QMainWindow):
	changeSignal = pyqtSignal(int, int)
	goToResultSignal = pyqtSignal(int)
	resultSignal = pyqtSignal(int, int)
	
	def __init__(self, userName: str, userPassword: str, question: str, choices: [str], answer: int, n: int):
		super(ObjectiveItemQuiz_controller, self).__init__()
		self.ui = Ui_ObjectiveItemQuizForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.question = question
		self.answer = answer
		self.cnt = 0
		for i in range(4):
			self.cnt += (1 if answer & (1 << i) != 0 else 0)
		self.choices = choices
		self.choicesEdit = [self.ui.AQuestionTextEdit, self.ui.BQuestionTextEdit,
							self.ui.CQuestionTextEdit, self.ui.DQuestionTextEdit]
		self.choicesBox = [self.ui.AradioButton, self.ui.BradioButton, self.ui.CradioButton,
						   self.ui.DradioButton]
		self.n = n
		self.setup_control()
	
	def _check(self):
		rt = 0
		for i in range(4):
			rt |= (1 << i) if self.choicesBox[i].isChecked() else 0
		return rt
	
	def setup_control(self):
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		self.ui.choiceQuestionTextEdit.setText(self.question)
		self.ui.choiceQuestionTextEdit.setReadOnly(True)
		for i in range(4):
			self.choicesBox[i].setAutoExclusive(False)
			self.choicesEdit[i].setText(self.choices[i])
			self.choicesEdit[i].setReadOnly(True)
		self.ui.scheduleLabel.clear()
		self.ui.scoreLabel.hide()
		self.ui.answerLabel.hide()
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
		ans = self._check()
		if ans == 0:
			self.ui.scheduleLabel.setText('请选择至少一个答案')
		else:
			for i in range(4):
				self.choicesBox[i].setDisabled(True)
			self.ui.clearButton.setDisabled(True)
			self.ui.confirmButton.setDisabled(True)
			self.ui.scoreLabel.show()
			self.ui.answerLabel.show()
			ras = '正确答案：'
			for i in range(4):
				if self.answer & (1 << i) != 0:
					ras += chr(ord('A') + i)
					ras += ', '
			self.ui.answerLabel.setText(ras[:len(ras) - 2])
			mrs = 0
			for i in range(4):
				if self.answer & (1 << i) == 0 and ans & (1 << i) != 0:
					self.ui.scoreLabel.setText('得分：0/10')
					return
				if self.answer & (1 << i) != 0 and ans & (1 << i) != 0:
					mrs += 1
			x = mrs / self.cnt * 10
			self.ui.scoreLabel.setText('得分：' + str(x) + '/10')
			addToQuizHistoryQuestion(self.question, self.choices, self.answer, ans, x)
			if x != 10:
				addToWrongQuestion(self.question, self.choices, self.answer, ans)
			self.resultSignal.emit(x, 0)
			
	def clearButtonClicked(self):
		self.ui.scheduleLabel.clear()
		for i in range(4):
			self.choicesBox[i].setChecked(False)
	
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
def addToQuizHistoryQuestion(question: str, choices: [str], answer: int, myAnswer: int, score: float):
	"""
	:param question:
	:param choices: [str, str, str, str]
	:param answer: 1011这种二进制数，高位为D
	:param myAnswer: 1011这种二进制数，高位为D
	:param score:
	:return:
	"""
	pass


def addToWrongQuestion(question: str, choices: [str], answer: int, myAnswer: int):
	pass
