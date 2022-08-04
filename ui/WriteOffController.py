from WriteOff import Ui_WriteOffForm
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *


class WriteOffController(QtWidgets.QMainWindow):
	goBackToLoginSignal = pyqtSignal()
	
	def __init__(self):
		super(WriteOffController, self).__init__()
		self.ui = Ui_WriteOffForm()
		self.ui.setupUi(self)
		self.setup_control()
		
	def setup_control(self):
		self.setWindowFlags(Qt.CustomizeWindowHint)
		self.ui.writeOfflabel.clear()
		self.ui.writeOfflabel.setStyleSheet("background-image:url(../img/再会.png)")
		self.ui.confirmButton.clicked.connect(self.confirmButtonClicked)
		
	def confirmButtonClicked(self):
		self.goBackToLoginSignal.emit()
		self.close()
	