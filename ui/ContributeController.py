from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal

from db.questionBank import QuestionBank
from db.user import User
from ui.Contribute import Ui_ContributeForm
from OCR_and_PDF.fileProcess import getContent
import re
import db.question_process as checker

_debug = True


class Contribute_controller(QtWidgets.QMainWindow):
	rightfulFormat = re.compile(r'^.*(\.jpg|\.png|\.png|\.pdf|\.txt|\.jpeg)$')
	empty = re.compile(r"^\s*$")
	goBackToMainSignal = pyqtSignal(int)
	
	def __init__(self, userName: str, userPassword: str):
		super(Contribute_controller, self).__init__()
		self.ui = Ui_ContributeForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.setup_control()
		
	def _clearLabelAndText(self):
		self.ui.thanksTipsLabel.clear()
		self.ui.questionTipsLabel.clear()
		self.ui.answerTipsLabel.clear()
		self.ui.answerTextEdit.clear()
		self.ui.questionTextEdit.clear()
		
	def _clearLabel(self):
		self.ui.thanksTipsLabel.clear()
		self.ui.questionTipsLabel.clear()
		self.ui.answerTipsLabel.clear()
		
	def setup_control(self):
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self._clearLabelAndText()
		self.ui.questionTextEdit.setPlaceholderText('注意客观题题目贡献格式为：\n'
													'xxxxxxxxxxx:\n'
													'A. xxx\n'
													'B. xxx\n'
													'C. xxx\n'
													'D. xxx\n'
													'未按格式贡献有可能之后显示会有问题，'
													'同时上述英文字母均需大写，且仅接受4个选项题目')
		self.ui.answerTextEdit.setPlaceholderText('注意客观题答案贡献格式为（以答案为: A, B为例）：'
												  'A, B')
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		self.ui.questionTypeComboBox.addItems(['', '客观题', '主观题'])
		self.ui.questionTypeComboBox.setEditable(False)
		self.ui.openFileForQuestionButton.clicked.connect(self.openFileForQuestionButtonClicked)
		self.ui.openFileForAnswerButton.clicked.connect(self.openFileForAnswerButtonClicked)
		self.ui.confirmButton.clicked.connect(self.confirmButtonClicked)
		self.ui.goBackButton.clicked.connect(self.goBackButtonClicked)
		self.ui.clearQuestionButton.clicked.connect(self.clearQuestionButtonClicked)
		self.ui.clearAnswerButton.clicked.connect(self.clearAnswerButtonClicked)
		
	def openFileForQuestionButtonClicked(self):
		self.ui.questionTextEdit.clear()
		self._clearLabel()
		filePath, fileType = QFileDialog.getOpenFileName(self, "Open file", "./")
		if re.match(self.rightfulFormat, filePath):
			self.ui.questionTipsLabel.setText("正在识别文件，请耐心等待。。。")
			content = getFileContent(filePath)
			self.ui.questionTipsLabel.clear()
			if content:
				self.ui.questionTextEdit.append(content)
			else:
				self.ui.questionTipsLabel.setText("什么都没识别到，请再次尝试")
		else:
			self.ui.questionTipsLabel.setText("无法识别该文件类型，请再次尝试")
	
	def openFileForAnswerButtonClicked(self):
		self.ui.answerTextEdit.clear()
		self._clearLabel()
		filePath, fileType = QFileDialog.getOpenFileName(self, "Open file", "./")
		if re.match(self.rightfulFormat, filePath):
			self.ui.answerTipsLabel.setText("正在识别文件，请耐心等待。。。")
			content = getFileContent(filePath)
			self.ui.answerTipsLabel.clear()
			if content:
				self.ui.answerTextEdit.append(content)
			else:
				self.ui.answerTipsLabel.setText("什么都没识别到，请再次尝试")
		else:
			self.ui.answerTipsLabel.setText("无法识别该文件类型，请再次尝试")

	def confirmButtonClicked(self):
		self._clearLabel()
		question = self.ui.questionTextEdit.toPlainText()
		answer = self.ui.answerTextEdit.toPlainText()
		flag = True
		if re.match(self.empty, question):
			self.ui.questionTipsLabel.setText("题目不应为空！")
			flag = False
		if re.match(self.empty, answer):
			self.ui.answerTipsLabel.setText("答案不应为空！")
			flag = False
		if flag:
			if addToQuestionBank((question, answer, self.ui.questionTypeComboBox.currentText())):
				if _debug:
					print((question, answer, self.ui.questionTypeComboBox.currentText()))
				self.ui.thanksTipsLabel.setText('感谢您的无私奉献！')
			else:
				self.ui.thanksTipsLabel.setText('很可惜题库已经有它了！')
				
	def goBackButtonClicked(self):
		self.goBackToMainSignal.emit(6)
		self._clearLabelAndText()
		
	def clearQuestionButtonClicked(self):
		self._clearLabel()
		self.ui.questionTextEdit.clear()
		
	def clearAnswerButtonClicked(self):
		self._clearLabel()
		self.ui.answerTextEdit.clear()
		
	def showEvent(self, a0: QtGui.QShowEvent):
		self.ui.questionTypeComboBox.setCurrentText('')
		a0.accept()
	
	
def getFileContent(filePath: str) -> str:  # jpg, png, txt, pdf, jpeg

	return getContent(filePath)

def addToQuestionBank(questionAndAnswer: (str, str, str)) -> bool:  # Q, A, type
	user = User()
	qb = QuestionBank()
	provider = user.name
	if questionAndAnswer[2] == '客观题':
		if checker.format_checker(questionAndAnswer[0]) and checker.ans_process(questionAndAnswer[1]) != 0:
			select_question = checker.process(questionAndAnswer[0])
			answer = checker.get_ans(checker.ans_process(questionAndAnswer[1]))
			questionAndAnswer = (questionAndAnswer[0], answer, questionAndAnswer[2])
			return qb.add_select_question(questionAndAnswer, select_question, provider)
		else:
			return qb.add_question(questionAndAnswer[0:2] + ('',), provider)
	else:
		return qb.add_question(questionAndAnswer, provider)

# finish
