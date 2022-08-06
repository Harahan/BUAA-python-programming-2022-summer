import re

from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from ui.PreForQuiz import Ui_PreForQuizForm


class PreForQuiz_controller(QtWidgets.QMainWindow):
	digit = re.compile(r'\d+')
	goBackToMainSignal = pyqtSignal(int)
	
	def __init__(self, userName: str, userPassword: str):
		super(PreForQuiz_controller, self).__init__()
		self.ui = Ui_PreForQuizForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.numbers = []
		self.setup_control()
		self.choices = [self.ui.historyLineEdit, self.ui.favoriteLineEdit, self.ui.wrongLineEdit,
						self.ui.reciteLineEdit, self.ui.originLineEdit]
		
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
					print('ok')
				else:
					self.ui.tipslabel.setText('请对测试所选题目进行正确输入！')
			else:
				p = self.choices[4].text()
				if re.match(self.digit, p) and 0 < int(p) <= self.numbers[4]:
					print('ok')
				else:
					self.ui.tipslabel.setText('请对测试所选题目进行正确输入！')
					
	def showEvent(self, a0: QtGui.QShowEvent):
		self.numbers = getQuestionNumber()
		self.ui.historyNumberLabel.setText('/' + str(self.numbers[0]))
		self.ui.favoriteNumberLabel.setText('/' + str(self.numbers[1]))
		self.ui.wrongNumberLabel.setText('/' + str(self.numbers[2]))
		self.ui.reciteNumberLabel.setText('/' + str(self.numbers[3]))
		self.ui.originNumberLabel.setText('/' + str(self.numbers[4]))
		for i in range(5):
			self.choices[i].setText('0')
		self.ui.tipslabel.clear()
		self.ui.comboBox.setCurrentText('')
		a0.accept()
		
	def closeEvent(self, a0: QtGui.QCloseEvent):
		self.goBackToMainSignal.emit(7)
		self.hide()
		

# ----- 要提供的函数 ----- # TODO
def getQuestionNumber() -> (int, int, int, int, int):
	"""
	:return: 历史，喜欢，错题，背题，题库的题目数目
	"""
	return 2, 1, 1, 1, 4
