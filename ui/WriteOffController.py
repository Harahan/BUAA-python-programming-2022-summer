from WriteOff import Ui_WriteOffForm
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *


class WriteOffController(QtWidgets.QMainWindow):
	goBackToLoginSignal = pyqtSignal()
	goBackToMainSignal = pyqtSignal(int)
	
	def __init__(self, userName: str, userPassword: str):
		super(WriteOffController, self).__init__()
		self.ui = Ui_WriteOffForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.flag = False
		self.setup_control()
		
	def setup_control(self):
		self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
		self.setWindowFlags(Qt.WindowCloseButtonHint)
		self.ui.writeOfflabel.clear()
		self.ui.writeOfflabel.setStyleSheet("background-image:url(../img/bye.jpg)")
		self.ui.confirmButton.clicked.connect(self.confirmButtonClicked)
		
	def confirmButtonClicked(self):
		writeOffUser(self.userName, self.userPassword)
		self.goBackToLoginSignal.emit()
		self.flag = True
		self.close()
		
	def closeEvent(self, a0: QtGui.QCloseEvent):
		if self.flag:
			a0.accept()
		else:
			self.goBackToMainSignal.emit(5)
			a0.ignore()
		
	def showEvent(self, a0: QtGui.QShowEvent):
		self.flag = False
		a0.accept()
		
	
# ----- 补全的代码 ----- # TODO
def writeOffUser(userName: str, userPassword: str) -> None:
	pass
	