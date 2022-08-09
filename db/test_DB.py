import initial as init
from user import User
from questionBank import QuestionBank


if __name__ == '__main__':
    init.destroy_database()
    init.initial()
    user = User()
    qb = QuestionBank()
    user.register('zya', '123456')
    user.login('zya', '123456')
    question = 'buaa'
    answer = 'beihang'
    print(user.name)
    print(qb.search_question(question))
    user.add_data('history', (question, answer))
    user.add_data('history', (question, answer))
    user.add_data('like', (question, answer))
    user.add_data('like', (question, answer))
    user.exit()
    user.login('zya', '123456')
    print(user.get_table('history'))
    print(user.get_table('like'))
    question = 'hello world!'
    answer = '钝角'
    qb.add_question((question, answer), user.name)
    user.exit()
