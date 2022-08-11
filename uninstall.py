import db.initial


if __name__ == '__main__':
    db.initial.destroy_database()
    print("您已成功删除数据库!")
