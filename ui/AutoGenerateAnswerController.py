from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *

from MRC.MRC_request import MRC_function
from OCR_and_PDF.fileProcess import getContent
from ui.AutoGenerateAnswer import Ui_AutoGenerateAnswerForm
import re


class AutoGenerateAnswer_controller(QtWidgets.QMainWindow):
	goBackToMainSignal = pyqtSignal(int)
	empty = re.compile(r"^\s*$")
	rightfulFormat = re.compile(r'^.*(\.jpg|\.png|\.png|\.pdf|\.txt|\.jpeg)$')
	
	def __init__(self, userName: str, userPassword: str, question: str):
		super(AutoGenerateAnswer_controller, self).__init__()
		self.ui = Ui_AutoGenerateAnswerForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.question = question
		self.setup_control()
		
	def setup_control(self):
		self.ui.scheduleTipsLabel.clear()
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		self.ui.openFileButton.clicked.connect(self.openFileButtonClicked)
		self.ui.confirmButton.clicked.connect(self.confirmButtonClicked)
		self.ui.goBackButton.clicked.connect(self.goBackButtonClicked)
		self.ui.questionTextEdit.setText(self.question)
		
	def setQuestion(self, s: str):
		self.question = s
		
	def showEvent(self, a0: QtGui.QShowEvent):
		self.ui.questionTextEdit.setText(self.question)
		self.ui.scheduleTipsLabel.clear()
		self.ui.AnswerTextEdit.clear()
		self.ui.refTxtTextEdit.clear()
		
	def openFileButtonClicked(self):
		self.ui.refTxtTextEdit.clear()
		self.ui.scheduleTipsLabel.clear()
		filePath, fileType = QFileDialog.getOpenFileName(self, "Open file", "./")
		if re.match(self.rightfulFormat, filePath):
			self.ui.scheduleTipsLabel.setText("正在识别文件，请耐心等待。。。")
			content = getContent(filePath)
			self.ui.scheduleTipsLabel.clear()
			if content:
				self.ui.refTxtTextEdit.append(content)
			else:
				self.ui.scheduleTipsLabel.setText("什么都没识别到，请再次尝试")
		else:
			self.ui.scheduleTipsLabel.setText("无法识别该文件类型，请再次尝试")

	def confirmButtonClicked(self):
		self.ui.scheduleTipsLabel.clear()
		question = self.ui.questionTextEdit.toPlainText()
		txt = self.ui.refTxtTextEdit.toPlainText()
		if re.match(self.empty, question) or re.match(self.empty, txt):
			self.ui.scheduleTipsLabel.setText("问题和文本不应为空！")
		else:
			self.ui.scheduleTipsLabel.setText("正在搜索中，请耐心等待。。。")
			result = MRC_function(question, txt)
			self.ui.scheduleTipsLabel.clear()
			if re.match(self.empty, result):
				self.ui.scheduleTipsLabel.setText("不好意思，这题太难了。。。")
			else:
				self.ui.AnswerTextEdit.setText(result)
			
	def goBackButtonClicked(self):
		self.goBackToMainSignal.emit(11)
		