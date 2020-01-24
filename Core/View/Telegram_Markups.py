from telebot import types



class QAMarkup():
    """
    Класс QA (Основной набор кнопок) ответа от бота
    """

    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup()
        itemnext = types.KeyboardButton('Следующий вопрос')
        itemanswer = types.KeyboardButton('Показать ответ')
        itemmenu = types.KeyboardButton('Меню')
        self.markup.row(itemnext, itemanswer)
        self.markup.row(itemmenu)

class Menu():
    """
    Класс меню ответа от бота
    """

    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup()
        itemquestions = types.KeyboardButton('Перейти к вопросам')
        itemfavourites = types.KeyboardButton('Избранные вопросы')
        itemgroups = types.KeyboardButton('Выбрать темы')
        self.markup.row(itemquestions, itemfavourites)
        self.markup.row(itemgroups)
