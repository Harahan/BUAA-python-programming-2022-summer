import random
import db.question_process as process
from db.DB import DB
import Levenshtein


def check_repeat(table_name, key, value):
    db = DB()
    if len(db.find_key(table_name, key, value, 'str')) == 0:
        return False
    return True


def get_questions():
    db = DB()
    return list(db.get_table('question_bank'))


class QuestionBank:
    _instance = None
    _flag = False
    key_list = ('question', 'answer', 'type', 'provider')

    def __init__(self):
        if not QuestionBank._flag:
            self.name = 'question_bank'
            self.questions = get_questions()
            self.last_question_id = self.questions[len(self.questions) - 1][9]
            QuestionBank._flag = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_question(self, question_and_answer, provider):
        if self.check_repeat(question_and_answer[0]):
            return False
        db = DB()
        db.insert(self.name, self.key_list, question_and_answer + (provider,))
        self.last_question_id = self.last_question_id + 1
        self.questions.append(db.get_one_by_int(self.name, 'question_id', self.last_question_id))
        return True

    def add_select_question(self, question_and_answer, select_question, provider):
        if self.check_repeat(question_and_answer[0]):
            return False
        key_list = ('question', 'answer', 'type', 'select_question', 'A', 'B', 'C', 'D', 'provider')
        db = DB()
        db.insert(self.name, key_list, question_and_answer + select_question + (provider,))
        self.last_question_id = self.last_question_id + 1
        self.questions.append(db.get_one_by_int(self.name, 'question_id', self.last_question_id))
        return True

    def get_question(self, question_id):
        db = DB()
        return db.get_one_by_int(self.name, 'id', question_id)

    def get_id(self, question):
        db = DB()
        result = db.find_key(self.name, 'question', question, 'str')
        if len(result) == 0:
            return -1
        return result[0][3]

    def search_question(self, s):
        d_min1 = Levenshtein.distance(s, self.questions[0][0])
        place = 0
        for i in range(1, len(self.questions)):
            d = Levenshtein.distance(s, self.questions[i][0])
            if d < d_min1:
                d_min1 = d
                place = i
        result1 = (self.questions[place], d_min1)
        d_min2 = Levenshtein.distance(s, self.questions[0][3])
        place = 0
        for i in range(1, len(self.questions)):
            d = Levenshtein.distance(s, self.questions[i][3])
            if d < d_min2:
                d_min2 = d
                place = i
        result2 = (self.questions[place], d_min2)
        if result1[1] > result2[1]:
            return result2
        return result1

    def get_questions(self, num):
        if num == 0:
            return []
        db = DB()
        questions = self.questions
        random_list = random.sample(range(0, len(questions)), num)
        result = []
        for i in random_list:
            if questions[i][2] == '客观题':
                to_add = (questions[i][2], questions[i][3], questions[i][4:8],
                          process.ans_process(questions[i][1]), questions[i][9])
                result.append(to_add)
            else:
                to_add = (questions[i][2], questions[i][0], questions[i][1], questions[i][9])
                result.append(to_add)
        return result

    def check_repeat(self, question):
        search_result = self.search_question(question)
        if search_result[1] > 5:
            return False
        return True
