from telebot import types
import emoji


class QAMarkup:
    """
    Класс QA (Основной набор кнопок) ответа от бота
    """

    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup()
        item_next = types.KeyboardButton('Следующий вопрос')
        item_answer = types.KeyboardButton('Показать ответ')
        self.markup.row(item_next, item_answer)
        item_star = types.KeyboardButton('Добавить в избранное')
        item_menu = types.KeyboardButton('Меню')
        self.markup.row(item_menu, item_star)


class QAMarkupSetChosen:
    """
    Класс QA (Основной набор кнопок) ответа от бота
    """

    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup()
        item_next = types.KeyboardButton('Следующий вопрос')
        item_answer = types.KeyboardButton('Показать ответ')
        self.markup.row(item_next, item_answer)
        item_star = types.KeyboardButton('Удалить из избранного')
        item_menu = types.KeyboardButton('Меню')
        self.markup.row(item_menu, item_star)


class Menu:
    """
    Класс меню ответа от бота
    """

    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup()
        item_questions = types.KeyboardButton('Перейти к вопросам')
        item_favourites = types.KeyboardButton('Избранные вопросы')
        self.markup.row(item_questions, item_favourites)
        item_groups = types.KeyboardButton('Выбрать темы')
        self.markup.row(item_groups)


class GroupList:
    """
    """
    def __init__(self, groups_list):
        self.markup = types.ReplyKeyboardMarkup()
        for group in groups_list:
            item = types.KeyboardButton(group)
            self.markup.row(item)
        item_menu = types.KeyboardButton('Меню')
        self.markup.row(item_menu)
