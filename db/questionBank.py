import random
import db.question_process as process
from db.DB import DB


def check_repeat(table_name, key, value):
    db = DB()
    if len(db.find_key(table_name, key, value, 'str')) == 0:
        return False
    return True


def cut_str(s: str):
    tp = s.split()
    result = []
    if len(tp) == 1:
        start1 = 0
        end1 = 12
        start2 = 12
        end2 = 24
        if len(tp[0]) < 12:
            end1 = len(tp[0])
            start2 = 0
            end2 = len(tp[0])
        elif len(tp[0]) < 24:
            end2 = len(tp[0])
        result.append(tp[0][start1:end1])
        result.append(tp[0][start2:end2])
    else:
        end1 = 12
        end2 = 12
        if len(tp[0]) < 12:
            end1 = len(tp[0])
        if len(tp[1]) < 12:
            end2 = len(tp[1])
        result.append(tp[0][:end1])
        result.append(tp[1][:end2])
    return tuple(result)

class QuestionBank:
    _instance = None
    _flag = False
    key_list = ('question', 'answer', 'type', 'provider')

    def __init__(self):
        if not QuestionBank._flag:
            self.name = 'question_bank'
            QuestionBank._flag = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_question(self, question_and_answer, provider):
        if check_repeat(self.name, 'question', question_and_answer[0]):
            return False
        db = DB()
        db.insert(self.name, self.key_list, question_and_answer + (provider,))
        return True

    def add_select_question(self, question_and_answer, select_question, provider):
        key_list = ('question', 'answer', 'type', 'select_question', 'A', 'B', 'C', 'D', 'provider')
        db = DB()
        db.insert(self.name, key_list, question_and_answer + select_question + (provider,))

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
        tp = cut_str(s)
        if len(tp) < 2:
            return ()
        db = DB()
        result = db.fuzzy_search(self.name, 'question', tp[0])
        if len(result) == 1:
            return result[0]
        elif len(result) == 0:
            result = db.fuzzy_search(self.name, 'question', tp[1])
            if len(result) == 0:
                return ()
            else:
                return result[0]
        else:
            result2 = db.fuzzy_double_search(self.name, 'question', tp)
            if len(result2) == 0:
                return result[0]
            else:
                return result2[0]

    def get_questions(self, num):
        if num == 0:
            return []
        db = DB()
        questions = db.get_table(self.name)
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
