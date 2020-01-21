from telebot import types



class QAMarkup():
    """
    Класс QA (Основной набор кнопок) ответа от бота
    """
    markup = types.ReplyKeyboardMarkup()

    def __init__(self):
        itemnext = types.KeyboardButton('Следующий вопрос')
        itemanswer = types.KeyboardButton('Показать ответы')
        itemmenu = types.KeyboardButton('Меню')
        self.markup.row(itemnext, itemanswer)
        self.markup.row(itemmenu)

class Menu():
    """
    Класс меню ответа от бота
    """
    markup = types.ReplyKeyboardMarkup()

    def __init__(self):
        itemquestions = types.KeyboardButton('Перейти к вопросам')
        itemfavourites = types.KeyboardButton('Избранные вопросы')
        itemgroups = types.KeyboardButton('Выбрать темы')
        self.markup.row(itemquestions, itemfavourites)
        self.markup.row(itemgroups)