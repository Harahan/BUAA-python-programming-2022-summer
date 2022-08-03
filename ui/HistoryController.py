from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from ui.History import Ui_HistoryForm


class History_controller(QtWidgets.QMainWindow):
	goBackToMainSignal = pyqtSignal()
	
	def __init__(self, userName: str, userPassword: str):
		super(History_controller, self).__init__()
		self.ui = Ui_HistoryForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.historyQuestionAndAnswer = getHistoryQuestionAndAnswer(userName, userPassword)
		self.setup_control()
		
	def _showQuestionAndAnswer(self, number: int):
		self.ui.questionTextEdit.setText(self.historyQuestionAndAnswer[number][0])
		self.ui.answerTextEdit.setText(self.historyQuestionAndAnswer[number][1])
		
	def _checkNumber(self, number: int):
		maxNumber = len(self.historyQuestionAndAnswer)
		if number > maxNumber:
			self.ui.scheduleTipsLabel.setText("已经到底了，什么也没有了。。。")
			self.ui.questionTextEdit.setWindowIcon(QIcon("../img/404.png"))  # TODO
	
	def _initParameter(self):
		# self.ui.questionTextEdit.setWindowIcon(QIcon("../img/404.png"))  # TODO: test
		self.ui.totQuestionLabel.setText('/' + str(len(self.historyQuestionAndAnswer)))
		self.ui.questionNumberlineEdit.clear()
		self.ui.scheduleTipsLabel.clear()
		self.ui.questionTextEdit.setDisabled(True)
		self.ui.answerTextEdit.setDisabled(True)
		self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.ui.changeQuestionButton.setIcon(QIcon("../img/rightArrow.jpg"))
		self.ui.changeQuestionButton.setIconSize(QSize(15, 15))
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		
	def setup_control(self):
		self._initParameter()
		self.ui.historyAnalyzeButton.clicked.connect(self.historyAnalyzeButtonClicked)
		self.ui.clearCurrentQuestionButton.clicked.connect(self.clearCurrentQuestionButtonClicked)
		self.ui.nextQuestionButton.clicked.connect(self.nextQuestionButtonClicked)
		self.ui.preQuestionButton.clicked.connect(self.preQuestionButtonClicked)
		self.ui.addToFavoriteQuestionButton.clicked.connect(self.addToFavoriteQuestionButtonClicked)
		self.ui.addToReciteQuestionButton.clicked.connect(self.addToReciteQuestionButtonClicked)
		self.ui.addToWrongQuestionButton.clicked.connect(self.addToWrongQuestionButtonClicked)
		self.ui.goBackButton.clicked.connect(self.goBackButtonClicked)
		self.ui.changeQuestionButton.clicked.connect(self.changeQuestionButtonClicked)
	
	def historyAnalyzeButtonClicked(self):
		pass
	
	def clearCurrentQuestionButtonClicked(self):
		pass
	
	def nextQuestionButtonClicked(self):
		pass
	
	def preQuestionButtonClicked(self):
		pass
	
	def addToFavoriteQuestionButtonClicked(self):
		pass
	
	def addToReciteQuestionButtonClicked(self):
		pass
	
	def addToWrongQuestionButtonClicked(self):
		pass
	
	def goBackButtonClicked(self):
		self.goBackToMainSignal.emit()
		self._initParameter()
	
	def changeQuestionButtonClicked(self):
		pass
	
	def showEvent(self, a0: QtGui.QShowEvent):
		self.historyQuestionAndAnswer = getHistoryQuestionAndAnswer(self.userName, self.userPassword)
		a0.accept()
	
	
# ----- 要补的函数 ----- # TODO
def getHistoryQuestionAndAnswer(userName: str, userPassword: str) -> [(str, str)]:  # question, answer
	return [('1 + 1 = ', '2'), ('x**2 + 2 * x = -1, x = ', '-1')]
	