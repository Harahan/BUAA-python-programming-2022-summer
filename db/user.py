import random

from db.DB import DB
from db.questionBank import QuestionBank
import db.question_process as process


def check_repeat(table_name, key, value, _type):
    db = DB()
    if len(db.find_key(table_name, key, value, _type)) == 0:
        return False
    return True


def hasname(name):
    return check_repeat('user', 'name', name, 'str')


class User:
    _instance = None
    _flag = False

    #0, 1, 2代表history, like, recite 3, 4代表wrong和test_history
    def __init__(self):
        if not User._flag:
            self.name = ''
            self.table_list = ('_like', '_recite', '_wrong', '_history')
            self.like_recite_key = ('question_id', 'table_id')
            self.like_recite_type = ('int not null', 'int primary key not null auto_increment')
            self.history_key = ('question_id', 'table_id', 'answer', 'score', 'practice_time', 'history_type')
            self.history_type = ('int not null', 'int primary key not null auto_increment', "varchar(512) not null DEFAULT ''",
                                 'float not null DEFAULT -1', 'int not null DEFAULT 0', 'varchar(20) not null')
            self.wrong_key = ('question_id', 'table_id', 'last_answer')
            self.wrong_type = ('int not null', 'int primary key not null auto_increment', "varchar(512) not null DEFAULT ''")
            self.user_key = ('name', 'password')
            User._flag = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def register(self, name, password):
        if len(name) > 6 or len(password) > 12 or len(name) == 0 or hasname(name):
            return False
        else:
            value = (name, password)
            db = DB()
            db.insert('user', self.user_key, value)
            for i in range(len(self.table_list)):
                table_name = name + self.table_list[i]
                if i < 2:
                    db.create_table(table_name, self.like_recite_key, self.like_recite_type)
                elif i == 2:
                    db.create_table(table_name, self.wrong_key, self.wrong_type)
                else:
                    db.create_table(table_name, self.history_key, self.history_type)
        return True

    def login(self, name, password):
        if len(name) > 6 or len(password) > 12 or len(name) == 0 or not hasname(name):
            return False
        db = DB()
        result = db.find_key('user', 'name', name, 'str')
        if result[0][1] == password:
            self.name = name
            return True
        else:
            return False

    def exit(self):
        self.name = ''
        return

    def add_data(self, table, question_answer):
        table_name = self.name + '_' + table
        qb = QuestionBank()
        db = DB()
        question_id = qb.get_id(question_answer[0])
        if table == 'history' or table == 'test_history':
            db.insert(table_name, self.key_list[:-1], (question_id,))
            return True
        else:
            if not check_repeat(table_name, 'question_id', question_id, 'int'):
                db.insert(table_name, self.key_list[:-1], (question_id,))
                return True
        return False

    def get_table_name(self, table):
        return self.name + self.table_list[table]

    '''def add_test_history(self, value_list):
        table_name = self.get_table_name(4)
        if not check_repeat(table_name, 'question', value_list[0]):
            db = DB()
            db.insert(table_name, value_list)
            return True
        return False
'''

    def get_history_table(self):
        table_name = self.name + self.table_list[3]
        db = DB()
        question = 'question_bank.question'
        answer = 'question_bank.answer'
        question_id = table_name + '.question_id'
        table_id = table_name + '.table_id'
        key_list = (question, answer, question_id, table_id)
        result = list(db.get_union_table_all(table_name, 'question_bank', 'question_id', 'question_id', key_list))
        result.reverse()
        return result

    def get_question_infor(self, question_id, table_id):
        table_name = self.name + self.table_list[3]
        db = DB()
        test_infor = db.get_one_by_int(table_name, 'table_id', table_id)
        question_infor = db.get_one_by_int('question_bank', 'question_id', question_id)
        like = check_repeat(self.get_table_name(0), 'question_id', question_id, 'int')
        wrong = check_repeat(self.get_table_name(2), 'question_id', question_id, 'int')
        recite = check_repeat(self.get_table_name(1), 'question_id', question_id, 'int')
        result = [test_infor[3], question_infor[2], True, like, wrong, recite, question_infor[8],
                  test_infor[4], test_infor[5]]
        return result

    def get_history_score(self, question_id):
        table_name = self.get_table_name(3)
        db = DB()
        key_list = ('question_id', 'score')
        all_score = db.get_table_by_key(table_name, key_list)
        result = []
        for o in all_score:
            if o[0] == question_id and o[1] > -1:
                result.append(o[1])
        result.reverse()
        return result

    def get_like_table(self):
        table_name = self.get_table_name(0)
        db = DB()
        question = 'question_bank.question'
        answer = 'question_bank.answer'
        question_id = table_name + '.question_id'
        key_list = (question, answer, question_id)
        result = list(db.get_union_table_all(table_name, 'question_bank', 'question_id', 'question_id', key_list))
        result = result.reverse()
        return result

    def get_recite_table(self):
        table_name = self.get_table_name(1)
        db = DB()
        question = 'question_bank.question'
        answer = 'question_bank.answer'
        question_id = table_name + '.question_id'
        key_list = (question, answer, question_id)
        result = list(db.get_union_table_all(table_name, 'question_bank', 'question_id', 'question_id', key_list))
        result.reverse()
        return result

    def get_wrong_table(self):
        table_name = self.get_table_name(2)
        db = DB()
        question = 'question_bank.question'
        answer = 'question_bank.answer'
        last_answer = table_name + '.last_answer'
        question_id = table_name + '.question_id'
        key_list = (question, answer, last_answer, question_id)
        result = list(db.get_union_table_all(table_name, 'question_bank', 'question_id', 'question_id', key_list))
        result.reverse()
        return result

    def get_question_number(self):
        db = DB()
        history = len(db.get_table(self.get_table_name(3)))
        like = len(db.get_table(self.get_table_name(0)))
        wrong = len(db.get_table(self.get_table_name(2)))
        recite = len(db.get_table(self.get_table_name(1)))
        bank = len(db.get_table('question_bank'))
        return (history, like, wrong, recite, bank)

    def get_tetris_score(self):
        db = DB()
        my_score = db.get_one_by_str('user', 'name', self.name)[2]
        highest_score = db.get_max('user', 'highest_score')[0]
        return (highest_score, my_score)

    def get_questions(self, table, num):
        if num == 0:
            return []
        table_name = self.name + '_' + table
        db = DB()
        questions = db.get_union_table(table_name)
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

    def add_like(self, question_id):
        table_name = self.name + self.table_list[0]
        if check_repeat(table_name, 'question_id', question_id, 'int'):
            return False
        db = DB()
        key_list = ('question_id',)
        value_list = (question_id,)
        db.insert(table_name, key_list, value_list)
        return True

    def add_recite(self, question_id):
        table_name = self.name + self.table_list[1]
        if check_repeat(table_name, 'question_id', question_id, 'int'):
            return False
        db = DB()
        key_list = ('question_id',)
        value_list = (question_id,)
        db.insert(table_name, key_list, value_list)
        return True

    def add_wrong_no_answer(self, question_id):
        table_name = self.name + self.table_list[2]
        if check_repeat(table_name, 'question_id', question_id, 'int'):
            return False
        db = DB()
        key_list = ('question_id',)
        value_list = (question_id,)
        db.insert(table_name, key_list, value_list)
        return True

    def add_wrong_with_answer(self, question_id, my_answer):
        table_name = self.get_table_name(2)
        db = DB()
        if check_repeat(table_name, 'question_id', question_id, 'int'):
            db.update_one(table_name, 'question_id', question_id, 'last_answer', my_answer)
        else:
            key_list = ('question_id', 'last_answer')
            value_list = (question_id, my_answer)
            db.insert(table_name, key_list, value_list)

    def add_search_history(self, question_id):
        table_name = self.get_table_name(3)
        db = DB()
        key_list = ('question_id', 'history_type')
        value_list = (question_id, '搜索题目')
        db.insert(table_name, key_list, value_list)
        return True

    def add_test_history(self, question_id, my_answer, score):
        # 'question_id', 'table_id', 'answer', 'score', 'practice_time', 'history_type'
        table_name = self.get_table_name(3)
        db = DB()
        key_list = ('question_id', 'answer', 'score', 'practice_time', 'history_type')
        practice_time = db.get_max_select(table_name, 'practice_time', 'question_id', question_id) + 1
        value_list = (question_id, my_answer, score, practice_time, '小练习')
        db.insert(table_name, key_list, value_list)
        return True

    def add_tetris_score(self, score):
        db = DB()
        db.update_one('user', 'name', self.name, 'highest_score', score)

    def delete_history(self, table_id):
        table_name = self.name + self.table_list[3]
        if not check_repeat(table_name, 'table_id', table_id, 'int'):
            return False
        db = DB()
        db.delete_data(table_name, 'table_id', table_id)
        return True

    def delete_data(self, table, question_id):
        table_name = self.name + '_' + table
        if not check_repeat(table_name, 'question_id', question_id, 'int'):
            return False
        db = DB()
        db.delete_data(table_name, 'question_id', question_id)
        return True

    '''def delete_history(self, value):
        table_name = self.get_table_name(0)
        if check_repeat(table_name, 'question', value):
            return False
        else:
            db = DB()
            db.delete_data(table_name, 'question', value)
        return True
'''

    def destroy(self):
        if len(self.name) > 0:
            db = DB()
            for i in range(4):
                table_name = self.get_table_name(i)
                db.delete_table(table_name)
            db.delete_data('user', 'name', self.name)
            self.exit()

    '''def test_once(self, ):
'''