import pymysql


def initial():
    database_name = '小航搜题'  #数据库名
    connect = pymysql.connect(host='127.0.0.1',
                              port=3306,
                              user='root',
                              password='123456',
                              charset='utf8',
                              autocommit=True)
    cursor = connect.cursor()
    sql = "show databases like '" + database_name + "'"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        sql = 'create database %s default charset utf8' % database_name
        cursor.execute(sql)
        sql = 'use %s' % database_name
        cursor.execute(sql)
        #设置题库表单
        sql = 'CREATE TABLE question_bank(' \
              'question text(1024) not null, ' \
              'answer text(512) not null, ' \
              "type varchar(20) not null DEFAULT '', " \
              "select_question varchar(512) not null DEFAULT '', " \
              "A varchar(256) not null DEFAULT '', " \
              "B varchar(256) not null DEFAULT '', " \
              "C varchar(256) not null DEFAULT '', " \
              "D varchar(256) not null DEFAULT '', " \
              "provider varchar(25) not null DEFAULT '', " \
              "question_id int primary key not null auto_increment)"
        cursor.execute(sql)
        #设置用户表单
        sql = 'CREATE TABLE user(name varchar(25) primary key  not null, ' \
              'password varchar(25) not null, ' \
              'highest_score int not null DEFAULT 0)'
        cursor.execute(sql)
        #载入题库
        table_name = 'question_bank'
        key_list = ('question', 'answer', 'type', 'select_question', 'A', 'B', 'C', 'D', 'provider')
        value_list_list = (('buaa', 'beihang', '主观题', '', '', '', '', '', '原始题库'),
                           ('1+1=--\nA.2\nB.2\nC.1\nD.0', 'A-B', '客观题', '1+1=--', '2', '2', '1', '0', '原始题库'))
        for value_list in value_list_list:
            sql = 'INSERT INTO %s %s VALUES %s' % (table_name, get_key_str(key_list), get_value_str(value_list))
            cursor.execute(sql)

def destroy_database():
    database_name = '小航搜题'  #数据库名
    connect = pymysql.connect(host='127.0.0.1',
                              port=3306,
                              user='root',
                              password='123456',
                              charset='utf8',
                              autocommit=True)
    cursor = connect.cursor()
    sql = 'drop database %s' % database_name
    cursor.execute(sql)


def get_value_str(value_list):
    if len(value_list) > 1:
        return str(value_list)
    else:
        return str(value_list)[:-2] + ')'


def get_key_str(key_list):
    key_str = '(' + key_list[0]
    for i in range(1, len(key_list)):
        key_str = key_str + ',' + key_list[i]
    key_str = key_str + ')'
    return key_str
