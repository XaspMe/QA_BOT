from Core.Controller import DB_handler


DB_handler.Handler().remove_set(113)

while True:
    print('Введите номер группы')
    gr = input()
    print('Введите вопрос')
    question = input()
    print('Введите ответ')
    answer = input()
    DB_handler.Handler().add_set(gr, question, answer)