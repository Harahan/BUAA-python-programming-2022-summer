from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal
from Contribute import Ui_ContributeForm
import re

_debug = False


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
		
	def setup_control(self):
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self._clearLabelAndText()
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
		self.ui.answerTipsLabel.clear()
		self.ui.questionTipsLabel.clear()
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
		self.ui.questionTipsLabel.clear()
		self.ui.questionTextEdit.clear()
		
	def clearAnswerButtonClicked(self):
		self.ui.answerTipsLabel.clear()
		self.ui.answerTextEdit.clear()
		
	def showEvent(self, a0: QtGui.QShowEvent):
		self.ui.questionTypeComboBox.setCurrentText('')
		a0.accept()
	
	
# ----- 补全的代码 ----- # TODO
def getFileContent(filePath: str) -> str:  # jpg, png, txt, pdf, jpeg
	return "fuck BUAA!!!"


def addToQuestionBank(questionAndAnswer: (str, str, str)) -> bool:  # Q, A, type
	return True
