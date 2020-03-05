from telebot import types


class QAMarkup:
    """
    Основная разметка для работы с вопросами
    """

    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_next = types.KeyboardButton('Следующий вопрос')
        item_answer = types.KeyboardButton('Показать ответ')
        self.markup.row(item_next, item_answer)
        item_star = types.KeyboardButton('Добавить в избранное')
        item_menu = types.KeyboardButton('Меню')
        self.markup.row(item_menu, item_star)


class QAMarkupSetChosen:
    """
    Разметка для вопроса, который добавлен в избранные
    """

    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_next = types.KeyboardButton('Следующий вопрос')
        item_answer = types.KeyboardButton('Показать ответ')
        self.markup.row(item_next, item_answer)
        item_star = types.KeyboardButton('Удалить из избранного')
        item_menu = types.KeyboardButton('Меню')
        self.markup.row(item_menu, item_star)


class Menu:
    """
    Разметка меню
    """
    def __init__(self):
        """
        Конструктор
        """
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем переменную, разрешить резайз (подгон по размеру)
        item_questions = types.KeyboardButton('Перейти к вопросам')  # Переменная хранит кнопку клавиатуры
        item_favourites = types.KeyboardButton('Избранные вопросы')  # Переменная хранит кнопку клавиатуры
        self.markup.row(item_questions, item_favourites)  # Добавляем строку кнопок, передаем в нее две кнопки
        item_groups = types.KeyboardButton('Выбрать темы')  # Переменная хранит кнопку клавиатуры
        self.markup.row(item_groups)  # Добавляем строку кнопок, передаем в одну кнопку


class GroupList:
    """
    Разметка выводит все группы строками кнопок, через переданный аргумент
    """
    def __init__(self, groups_list):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for group in groups_list:
            item = types.KeyboardButton(group)
            self.markup.row(item)
        item_menu = types.KeyboardButton('Меню')
        self.markup.row(item_menu)


class AdminMenu:
    """
    Разметка меню администратора
    """
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_how_many_questions = types.KeyboardButton('Показать кол-во вопросов')
        item_how_many_groups = types.KeyboardButton('Показать кол-во групп')
        self.markup.row(item_how_many_questions, item_how_many_groups)

        item_send_to_all = types.KeyboardButton('Сообщение всем пользователям')
        item_show_all_users=types.KeyboardButton('Показать всех пользователей')
        self.markup.row(item_send_to_all, item_show_all_users)

        item_add_question = types.KeyboardButton('Добавить вопрос')
        item_add_group = types.KeyboardButton('Добавить группу')
        self.markup.row(item_add_question, item_add_group)

        item_correct_question = types.KeyboardButton('Корректировать вопрос')
        item_users_corrects = types.KeyboardButton('Корректировки пользователей')
        self.markup.row(item_correct_question, item_users_corrects)
