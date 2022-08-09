import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import *
from matplotlib import pyplot as plt
from ui.Analyse import Ui_AnalyseForm
from db.user import User
import cv2


class Analyse_controller(QtWidgets.QMainWindow):
	goBackToHistorySignal = pyqtSignal()
	
	def __init__(self, userName: str, userPassword: str, question: str, answer: str, question_id: int, table_id: int):
		super(Analyse_controller, self).__init__()
		self.ui = Ui_AnalyseForm()
		self.ui.setupUi(self)
		self.userName = userName
		self.userPassword = userPassword
		self.question = question
		self.answer = answer
		self.question_id = question_id
		self.table_id = table_id
		self.setup_control()
	
	def _draw(self):
		x, y = [], getQuestionPoints(self.question_id)
		for i in range(1, len(y) + 1):
			x.append(i)
		plt.plot(x, y, color='green', label='All previous scores', linewidth=2, marker='o', markerfacecolor='black', markersize=4)
		plt.xlabel('times')
		plt.ylabel('scores')
		plt.title('Current Question Scores Analyse')
		plt.legend()
		plt.savefig("../img/historyPoints.png", dpi=600)
		plt.close()
		# plt.show()
	
	def _show(self):
		self.img = cv2.imread('../img/historyPoints.png')
		height, width, channel = self.img.shape
		bytesPerline = 3 * width
		self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
		self.qpixmap = QPixmap.fromImage(self.qimg)
		# self.qpixmap_height = self.qpixmap.height()
		self.ui.label.setPixmap(QPixmap.fromImage(self.qimg))
		# initial
		self.qpixmap_height = 580
		scaled_pixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
		self.ui.label.setPixmap(scaled_pixmap)
	
	def zoomInButtonClicked(self):
		self.qpixmap_height -= 100
		self._imgResize()
	
	def zoomOutButtonClicked(self):
		self.qpixmap_height += 100
		self._imgResize()
	
	def _imgResize(self):
		scaled_pixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
		# print(self.qpixmap_height)
		self.ui.label.setPixmap(scaled_pixmap)
	
	def setup_control(self):
		self.setWindowIcon(QIcon("../img/放大镜.jpg"))
		self.ui.userNamelabel.setText("用户名：" + self.userName)
		self.ui.goBackButton.clicked.connect(self.goBackButtonClicked)
		info = getQuestionInfor(self.question_id, self.table_id)
		self.ui.scoreLineEdit.setText('暂无' if info[0] == -1 else str(info[0]))
		self.ui.typeLineEdit.setText('暂无' if info[1] == '' else info[1])
		self.ui.hishtoryCheckBox.setCheckState(Qt.Checked if info[2] else Qt.Unchecked)
		self.ui.favoriteCheckBox.setCheckState(Qt.Checked if info[3] else Qt.Unchecked)
		self.ui.wrongCheckBox.setCheckState(Qt.Checked if info[4] else Qt.Unchecked)
		self.ui.reciteCheckBox.setCheckState(Qt.Checked if info[5] else Qt.Unchecked)
		self.ui.hishtoryCheckBox.setDisabled(True)
		self.ui.favoriteCheckBox.setDisabled(True)
		self.ui.reciteCheckBox.setDisabled(True)
		self.ui.wrongCheckBox.setDisabled(True)
		self.ui.sourceLineEdit.setText(info[6])
		self.ui.timesLineEdit.setText('非练习' if info[7] == -1 else str(info[7]))
		self.ui.memoryLineEdit.setText(info[8])
		self.ui.zoomOutButton.clicked.connect(self.zoomOutButtonClicked)
		self.ui.zoomInButton.clicked.connect(self.zoomInButtonClicked)
		self.ui.scrollArea.setWidgetResizable(True)
		self.ui.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self._draw()
		self._show()
	
	def goBackButtonClicked(self):
		# os.remove('../img/historyPoints.png')
		self.goBackToHistorySignal.emit()
	

def getQuestionInfor(question_id: int, table_id: int) -> (int, str, bool, bool, bool, bool, int, str):
	"""
	:param question_id:
	:param table_id:
	:return: 1.题目分数（如果此次记录是搜索返回-1）；2.题目类型：主观题，客观题；（没有返回''）
			3.4.5.6.我的历史记录（直接True），我喜欢的问题，我的错题本，我的背题集
			7.题目来源：原始题库/用户名
			8.当前是第几次完成(小练习，如果是搜索就-1)！！！
			9.搜索题目/小练习
	"""
	user = User()
	return user.get_question_infor(question_id, table_id)


def getQuestionPoints(question_id: int) -> list:
	"""
	:param question_id:
	:return: 返回该题从app建立到现在的所有分数，不去重，没有返回空，搜索记录返回0就好 远 ---> 近
	"""
	user = User()
	return user.get_history_score(question_id)

# finish
