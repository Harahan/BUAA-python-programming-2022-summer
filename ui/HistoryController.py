from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from ui.History import Ui_HistoryForm
from ui.AnalyseController import Analyse_controller
from db.user import User
import re


class History_controller(QtWidgets.QMainWindow):
    goBackToMainSignal = pyqtSignal(int)
    digit = re.compile(r'^\d+$')

    def __init__(self, userName: str, userPassword: str):
        super(History_controller, self).__init__()
        self.historyAnalyze_ui = None
        self.historyAnalyze_ui: Analyse_controller
        self.ui = Ui_HistoryForm()
        self.ui.setupUi(self)
        self.userName = userName
        self.userPassword = userPassword
        self.historyQuestionAndAnswer = getHistoryQuestionAndAnswer()
        self.currentPage = 1
        self.flag = False
        self.setup_control()

    def _checkNumber(self, number: int):
        maxNumber = len(self.historyQuestionAndAnswer)
        if number > maxNumber:
            self.ui.scheduleTipsLabel.setText("已经到底了，什么也没有了。。。")
            self.ui.questionTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
            self.ui.answerTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
        elif number <= 0:
            self.ui.scheduleTipsLabel.setText("没有更近的记录了。。。")
            self.ui.questionTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
            self.ui.answerTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
        else:
            return True
        return False

    def _showQuestionAndAnswer(self, number: int):
        self.ui.scheduleTipsLabel.clear()
        self.ui.questionTextEdit.clear()
        self.ui.answerTextEdit.clear()
        self.ui.questionTextEdit.setStyleSheet("background-image:url(); font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.ui.answerTextEdit.setStyleSheet("background-image:url(); font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.currentPage = number
        self.ui.questionNumberLineEdit.setText(str(number))
        if self._checkNumber(number):
            self.ui.questionTextEdit.setText(self.historyQuestionAndAnswer[number - 1][0])
            self.ui.answerTextEdit.setText(self.historyQuestionAndAnswer[number - 1][1])

    def _initParameter(self):
        # self.ui.questionTextEdit.setStyleSheet("background-image:url(../img/notFound.png)")
        self._showQuestionAndAnswer(1)
        self.ui.totQuestionLabel.setText('/' + str(len(self.historyQuestionAndAnswer)))
        # self.ui.questionNumberLineEdit.clear()
        self.ui.scheduleTipsLabel.clear()

    def _reshow(self):
        self.historyAnalyze_ui: Analyse_controller
        self.historyAnalyze_ui.close()
        self.flag = True
        self.show()

    def setup_control(self):
        self._initParameter()
        self.ui.questionTextEdit.setReadOnly(True)
        self.ui.answerTextEdit.setReadOnly(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
        self.setWindowIcon(QtGui.QIcon("../img/放大镜.jpg"))
        self.ui.changeQuestionButton.setIcon(QIcon("../img/rightArrow.jpg"))
        self.ui.changeQuestionButton.setIconSize(QSize(15, 15))
        self.ui.userNamelabel.setText("用户名：" + self.userName)
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
        if self._checkNumber(self.currentPage):
            question = self.historyQuestionAndAnswer[self.currentPage - 1][0]
            answer = self.historyQuestionAndAnswer[self.currentPage - 1][1]
            question_id = self.historyQuestionAndAnswer[self.currentPage - 1][2]
            table_id = self.historyQuestionAndAnswer[self.currentPage - 1][3]
            self.historyAnalyze_ui = Analyse_controller(self.userName, self.userPassword,
                                                        question, answer, question_id, table_id)
            self.historyAnalyze_ui.goBackToHistorySignal.connect(self._reshow)
            self.hide()
            self.historyAnalyze_ui.show()

    def clearCurrentQuestionButtonClicked(self):
        if self._checkNumber(self.currentPage):
            if clearCurrentSearchingHistoryQuestion(self.historyQuestionAndAnswer[self.currentPage - 1]):
                self.ui.scheduleTipsLabel.setText("清除成功，下一次进来它就消失了！")
            else:
                self.ui.scheduleTipsLabel.setText("该题在刚才已被清除！")

    def nextQuestionButtonClicked(self):
        if self.currentPage < len(self.historyQuestionAndAnswer):
            self._showQuestionAndAnswer(self.currentPage + 1)
        else:
            self._showQuestionAndAnswer(1)

    def preQuestionButtonClicked(self):
        if self.currentPage >= 2:
            self._showQuestionAndAnswer(self.currentPage - 1)
        else:
            self._showQuestionAndAnswer(len(self.historyQuestionAndAnswer))

    def addToFavoriteQuestionButtonClicked(self):
        if self._checkNumber(self.currentPage):
            if addToFavoriteQuestion(self.historyQuestionAndAnswer[self.currentPage - 1]):
                self.ui.scheduleTipsLabel.setText("已成功加入我喜欢的问题！")
            else:
                self.ui.scheduleTipsLabel.setText("该题在我喜欢的问题中已存在！")

    def addToReciteQuestionButtonClicked(self):
        if self._checkNumber(self.currentPage):
            if addToReciteQuestion(self.historyQuestionAndAnswer[self.currentPage - 1]):
                self.ui.scheduleTipsLabel.setText("已成功加入我的背题集！")
            else:
                self.ui.scheduleTipsLabel.setText("该题在我的背题集中已存在！")

    def addToWrongQuestionButtonClicked(self):
        if self._checkNumber(self.currentPage):
            if addToWrongQuestion(self.historyQuestionAndAnswer[self.currentPage - 1]):
                self.ui.scheduleTipsLabel.setText("已成功加入我的错题本！")
            else:
                self.ui.scheduleTipsLabel.setText("该题在我的错题本中已存在！")

    def goBackButtonClicked(self):
        self.goBackToMainSignal.emit(0)

    def changeQuestionButtonClicked(self):
        p = self.ui.questionNumberLineEdit.text()
        if re.match(self.digit, p):
            number = int(p)
            self._showQuestionAndAnswer(number)

    def showEvent(self, a0: QtGui.QShowEvent):
        if not self.flag:
            self.historyQuestionAndAnswer = getHistoryQuestionAndAnswer()
            self._initParameter()
        else:
            self.flag = False
        a0.accept()


def getHistoryQuestionAndAnswer() -> ((str, str, int, int)):  # question, answer, question_id, table_id
    user = User()
    return user.get_history_table()


def addToFavoriteQuestion(questionAndAnswer: (str, str, int, int)) -> bool:
    user = User()
    return user.add_like(questionAndAnswer[2])


def addToReciteQuestion(questionAndAnswer: (str, str, int, int)) -> bool:
    user = User()
    return user.add_recite(questionAndAnswer[2])


def addToWrongQuestion(questionAndAnswer: (str, str, int, int)) -> bool:
    user = User()
    return user.add_wrong_no_answer(questionAndAnswer[2])


def clearCurrentSearchingHistoryQuestion(questionAndAnswer: (str, str, int, int)) -> bool:
    user = User()
    return user.delete_history(questionAndAnswer[3])

# finish
