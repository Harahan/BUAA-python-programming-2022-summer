import pymysql


def get_key_str(key_list):
    key_str = '(' + key_list[0]
    for i in range(1, len(key_list)):
        key_str = key_str + ',' + key_list[i]
    key_str = key_str + ')'
    return key_str


def get_value_str(value_list):
    if len(value_list) > 1:
        return str(value_list)
    else:
        return str(value_list)[:-2] + ')'


class DB():
    _instance = None
    _flag = False

    def __init__(self):
        if not DB._flag:
            self.connect = pymysql.connect(host='127.0.0.1',
                                           port=3306,
                                           user='root',
                                           password='123456',
                                           charset='utf8',
                                           database='小航搜题',
                                           autocommit=True)
            self.cursor = self.connect.cursor()
            DB._flag = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_table(self, table_name, key_list, type_list):
        sql = 'CREATE TABLE %s (' % table_name
        sql = sql + key_list[0] + ' ' + type_list[0]
        for i in range(1, len(key_list)):
            sql = sql + ', ' + key_list[i] + ' ' + type_list[i]
        sql = sql + ')'
        self.cursor.execute(sql)

    def insert(self, table_name, key_list, value_list):
        sql = 'INSERT INTO %s %s VALUES %s' % (table_name, get_key_str(key_list), get_value_str(value_list))
        self.cursor.execute(sql)

    def get_table(self, table_name):
        sql = 'SELECT * FROM %s' % table_name
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_table_by_key(self, table_name, key_list):
        sql = 'SELECT %s FROM %s' % (get_key_str(key_list)[1:-1], table_name)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_one_by_int(self, table_name, key, value):
        sql = "SELECT * FROM %s where %s= %d" % (table_name, key, value)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_one_by_str(self, table_name, key, value):
        sql = "SELECT * FROM %s where %s= '%s'" % (table_name, key, value)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def find_key(self, table_name, key, value, _type):
        sql = ''
        if _type == 'str':
            sql = "SELECT * FROM %s where %s= '%s'" % (table_name, key, value)
        elif _type == 'int':
            sql = "SELECT * FROM %s where %s= %d" % (table_name, key, value)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def delete_data(self, table_name, key, value):
        sql = "DELETE FROM %s where %s= '%s'" % (table_name, key, value)
        self.cursor.execute(sql)

    def delete_table(self, table_name):
        sql = 'DROP TABLE IF EXISTS %s' % table_name
        self.cursor.execute(sql)

    def get_union_table(self, table_name):
        table1_name = 'question_bank'
        table2_name = table_name
        sql = 'SELECT * FROM %s RIGHT  JOIN %s ON %s.question_id= %s.question_id ' % \
                    (table1_name, table2_name, table1_name, table2_name)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def fuzzy_search(self, table_name, key, value):
        sql = "SELECT * FROM %s where %s like '%s'" % (table_name, key, '%' + value + '%')
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def fuzzy_double_search(self, table_name, key, value_list):
        sql = "SELECT * FROM %s where %s like '%s' and %s like '%s'" % \
              (table_name, key, '%' + value_list[0] + '%', key, '%' + value_list[1] + '%')
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_union_table_all(self, table1_name, table2_name, table1_key, table2_key, key_list):
        sql = 'SELECT %s FROM %s , %s WHERE %s.%s= %s.%s' % \
              (get_key_str(key_list)[1:-1], table1_name, table2_name, table1_name, table1_key,
               table2_name, table2_key)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update_one(self, table_name, find_key, find_key_value, key, new_value):
        sql = "UPDATE %s SET %s = '%s' WHERE %s = '%s'" % (table_name, key, new_value, find_key, find_key_value)
        self.cursor.execute(sql)

    def get_max(self, table_name, key):
        sql = 'select max(%s) from %s' % (key, table_name)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_max_select(self, table_name, key, find_key, find_value) -> int:
        sql = 'select max(%s) from %s where %s= %d' % (key, table_name, find_key, find_value)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result[0] is None:
            return 0
        else:
            return result[0]