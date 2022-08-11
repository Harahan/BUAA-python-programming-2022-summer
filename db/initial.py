import os.path

import sqlite3


database_name = '小航搜题'  # 数据库名

def get_data_path(name):
    this_dir = os.path.dirname(__file__)
    result = this_dir + '_dir/' + name + '.db'
    return result


def get_data_dir_path(name):
    this_dir = os.path.dirname(__file__)
    result = this_dir + '_dir'
    return result


def get_base():
    this_dir = os.path.dirname(__file__)
    result = this_dir + '_data/questions.db'
    return result


def initial():
    data_path = get_data_path(database_name)
    data_dir_path = get_data_dir_path(database_name)
    if not os.path.exists(data_dir_path):
        os.makedirs(data_dir_path)         # 创建路径
    if not os.path.exists(data_path):
        connect = sqlite3.connect(data_path)
        cursor = connect.cursor()
        #设置题库表单
        sql = 'CREATE TABLE question_bank(' \
              'question varchar(1024) not null, ' \
              'answer varchar(512) not null, ' \
              "type varchar(20) not null DEFAULT '', " \
              "select_question varchar(512) not null DEFAULT '', " \
              "A varchar(256) not null DEFAULT '', " \
              "B varchar(256) not null DEFAULT '', " \
              "C varchar(256) not null DEFAULT '', " \
              "D varchar(256) not null DEFAULT '', " \
              "provider varchar(25) not null DEFAULT '', " \
              "question_id integer PRIMARY KEY autoincrement)"
        cursor.execute(sql)
        #设置用户表单
        sql = 'CREATE TABLE user(name varchar(25) primary key  not null, ' \
              'password varchar(25) not null, ' \
              'highest_score int not null DEFAULT 0)'
        cursor.execute(sql)
        # 载入题库
        add_question_bank(connect, cursor)
        connect.commit()
    return data_path


def destroy_database():
    data_path = get_data_path(database_name)
    if os.path.exists(data_path):
        os.remove(data_path)


def get_key_str(key_list):
    key_str = '(' + key_list[0]
    for i in range(1, len(key_list)):
        key_str = key_str + ',' + key_list[i]
    key_str = key_str + ')'
    return key_str


def get_table(table_name):
    conn = sqlite3.connect(get_base())
    cur = conn.cursor()
    sql = "SELECT * FROM %s" % table_name
    cur.execute(sql)
    return cur.fetchall()


def get_question(t):
    s = t[0] + '\n' + 'A.' + t[1] + '\n' + 'B.' + t[2] + '\n' + 'C.' + t[3] + '\n' + 'D.' + t[4]
    return s


def add_question_bank(connect, cursor):
    key_list = ('question', 'answer', 'type', 'select_question', 'A', 'B', 'C', 'D', 'provider')
    t1 = get_table('question_bank')
    for t in t1:
        question = t[0]
        answer = t[1]
        type = t[2]
        select_question = t[3]
        A = t[4]
        B = t[5]
        C = t[6]
        D = t[7]
        provider = t[8]
        value_str = "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %\
                    (question, answer, type, select_question, A, B, C, D, provider)
        sql = 'INSERT INTO %s %s VALUES %s' % ('question_bank', get_key_str(key_list), value_str)
        cursor.execute(sql)
        connect.commit()
