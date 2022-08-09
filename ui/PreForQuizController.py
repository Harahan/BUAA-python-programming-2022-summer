import re

from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *

from db.questionBank import QuestionBank
from db.user import User
from ui.PreForQuiz import Ui_PreForQuizForm
from ui.ObjectiveItemQuizController import ObjectiveItemQuiz_controller
from ui.SubjectiveItemQuizController import SubjectiveItemQuiz_controller
from ui.QuizResultController import QuizResult_controller


class PreForQuiz_controller(QtWidgets.QMainWindow):
	digit = re.compile(r'^\d+$')
	goBackToMainSignal = pyqtSignal(int)

	def __init__(self, userName: str, userPassword: str, quizResult_ui: QuizResult_controller):
		super(PreForQuiz_controller, self).__init__()
		self.ui = Ui_PreForQuizForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.quizResult_ui = quizResult_ui
		self.numbers = []
		self.setup_control()
		self.choices = [self.ui.historyLineEdit, self.ui.favoriteLineEdit, self.ui.wrongLineEdit,
						self.ui.reciteLineEdit, self.ui.originLineEdit]
		self.x = []
		self.finish0 = 0
		self.result0 = 0
		self.finish1 = 0
		self.result1 = 0
		self.o = 0
		self.s = 0
		self.flag = True

	def _check(self):
		flag, tag = 0, 0
		for k in range(5):
			p = self.choices[k].text()
			if re.match(self.digit, p):
				if 0 <= int(p) <= self.numbers[k]:
					flag += 1
					if int(p) == 0:
						tag += 1
		if flag == 5 and tag != 5:
			return True
		else:
			return False

	def _decide(self, val):
		if val == '自选':
			for i in range(5):
				self.choices[i].setDisabled(False)
		elif val == '随机':
			for i in range(4):
				self.choices[i].setDisabled(True)
				self.choices[i].clear()
			self.ui.originLineEdit.setDisabled(False)

	def _changeWindows(self, n: int, op: int):
		if op == 0 and n != 0:
			self.x[n].hide()
			self.x[n - 1].show()
		elif op == 1 and n != len(self.x) - 1:
			self.x[n].hide()
			self.x[n + 1].show()

	def _result(self, n: float, op: int):
		# print(n, op)
		if op == 0:
			self.finish0 += 1
			self.result0 += n
		else:
			self.finish1 += 1
			self.result1 += n

	def _showResult(self, n: int):
		self.x[n].hide()
		self.quizResult_ui.set(self.o, self.s, self.finish0, self.finish1,
							   int(10 * (self.result1 + self.result0) / (self.o + self.s)))
		self.quizResult_ui.show()

	def setup_control(self):
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.ui.tipslabel.clear()
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		self.ui.comboBox.addItems(['', '自选', '随机'])
		self.ui.comboBox.setEditable(False)
		self.ui.confirmButton.clicked.connect(self.confirmButtonClicked)
		self.ui.comboBox.activated[str].connect(lambda val: self._decide(val))

	def confirmButtonClicked(self):
		self.ui.tipslabel.clear()
		if self.ui.comboBox.currentText() == '':
			self.ui.tipslabel.setText('请选择是随机出题还是手动选题')
		else:
			if self.ui.comboBox.currentText() == '自选':
				if self._check():
					self.quiz(getQuestionAndAnswer(int(self.choices[0].text()), int(self.choices[1].text()),
												   int(self.choices[2].text()), int(self.choices[3].text()),
																				int(self.choices[4].text())))
				else:
					self.ui.tipslabel.setText('请对测试所选题目进行正确输入！')
			else:
				p = self.choices[4].text()
				if re.match(self.digit, p) and 0 < int(p) <= self.numbers[4]:
					self.quiz(getQuestionAndAnswer(0, 0, 0, 0, int(p)))
				else:
					self.ui.tipslabel.setText('请对测试所选题目进行正确输入！')

	def showEvent(self, a0: QtGui.QShowEvent):
		self.numbers = getQuestionNumber()
		self.ui.historyNumberLabel.setText('/' + str(self.numbers[0]))
		self.ui.favoriteNumberLabel.setText('/' + str(self.numbers[1]))
		self.ui.wrongNumberLabel.setText('/' + str(self.numbers[2]))
		self.ui.reciteNumberLabel.setText('/' + str(self.numbers[3]))
		self.ui.originNumberLabel.setText('/' + str(self.numbers[4]))
		self.finish0 = 0
		self.result0 = 0
		self.finish1 = 0
		self.result1 = 0
		self.o = 0
		self.s = 0
		self.flag = True
		for i in range(5):
			self.choices[i].setText('0')
		self.ui.tipslabel.clear()
		self.ui.comboBox.setCurrentText('')
		a0.accept()

	def closeEvent(self, a0: QtGui.QCloseEvent):
		if self.flag:
			self.goBackToMainSignal.emit(7)
		a0.accept()
		
	def quiz(self, q: [(str, str, str, int), (str, str, [str], int, int)]):
		self.x = []
		for i in range(len(q)):
			if len(q[i]) == 4:
				self.s += 1
				sub = SubjectiveItemQuiz_controller(self.userName, self.userPassword, q[i][1], q[i][2], q[i][3], i)
			else:
				self.o += 1
				sub = ObjectiveItemQuiz_controller(self.userName, self.userPassword, q[i][1], q[i][2], q[i][3], q[i][4], i)
			sub.changeSignal.connect(self._changeWindows)
			sub.resultSignal.connect(self._result)
			sub.goToResultSignal.connect(self._showResult)
			self.x.append(sub)
			# print(i)
		self.flag = False
		self.close()
		self.x[0].show()


def getQuestionNumber() -> (int, int, int, int, int):
	"""
	:return: 历史，喜欢，错题，背题，题库的题目数目
	"""
	user = User()
	return user.get_question_number()


def getQuestionAndAnswer(n1: int, n2: int, n3: int, n4: int, n5: int) -> [(str, str, str), (str, str, [str], int)]:
	"""
	:param n1: 历史，喜欢，错题，背题，题库要返回题目数
	:param n2:
	:param n3:
	:param n4:
	:param n5:
	:return:
	"""
	user = User()
	qb = QuestionBank()
	result = user.get_questions('history', n1) + user.get_questions('like', n2) + \
			user.get_questions('wrong', n3) + user.get_questions('recite', n4) + qb.get_questions(n5)
	return result  # 选择题的答案是二进制表示，高位为D

# finish