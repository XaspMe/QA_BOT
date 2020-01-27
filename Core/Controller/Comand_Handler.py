from Core.Controller import DB_Handle, User_validation
from Core.View import Telegram_Markups as tm
from Core.Controller import DB_Handle as db
from telebot import *

"""
Паттерн цепочка обязанностей для обработки сообщения.
Петтерн посредник для обработки операций в зависимости от
Перкидывать запросы в нужные модули, в конце цепочки нужная View
"""

"""
Сюда приходят команды пользователя, в зависимости от текста возвращается View с instance ответа.
"""


class Handler:
    def __init__(self, message):
        self.message = message
        self.is_prepared = None

    def handle(self):
        print(self.message.text)
        validate = User_validation.UserValidation(self.message.chat.id, self.message.from_user.username)
        validate.check_or_create()

        if self.message.text == 'Следующий вопрос':
            self.__next_question()

        if self.message.text == 'Показать ответ':
            self.__show_answer()

        if self.message.text == 'Меню' or \
                self.message.text == 'start' or \
                self.message.text == 'help' or \
                self.message.text == '/help':
            self.__go_to_menu()

        if self.message.text == 'Перейти к вопросам':
            self.__next_question()

        if self.message.text == 'Добавить в избранное':
            self.__add_to_chosen()

        if self.message.text == 'Удалить из избранного':
            self.__rem_from_chosen()

    def __go_to_menu(self):
        self.text_response = 'Основное меню.'
        self.markup = tm.Menu().markup
        self.is_prepared = True

    def __next_question(self):
        self.set_handler = DB_Handle.Handler()
        qa_set = self.set_handler.get_random_set_by_groups((1, 2, 3, 4))[0]
        self.set_handler.upd_chat_lastset(self.message.chat.id, qa_set.id)
        self.text_response = qa_set.question + '\n qqqqq'
        if self.set_handler.is_set_chosen(self.message.chat.id, qa_set):
            self.markup = tm.QAMarkupSetChosen().markup
        else:
            self.markup = tm.QAMarkup().markup
        self.is_prepared = True

    def __show_answer(self):
        self.set_handler = DB_Handle.Handler()
        last_set = self.set_handler.get_user_last_set(self.message.chat.id)
        self.text_response = self.set_handler.get_answer_by_set_id(last_set)
        self.markup = tm.QAMarkup().markup
        self.is_prepared = True

    def ___add_to_chosen(self):
        self.set_handler = DB_Handle.Handler()
        last_user_set = self.set_handler.get_user_last_set(self.message.chat.id)
        self.set_handler.add_to_ChatidSetIntermediate(self.message.chat.id, last_user_set)
        self.text_response = 'Вопрос добавлен в избранное'
        self.markup = tm.QAMarkupSetChosen().markup
        self.is_prepared = True

    def __rem_from_chosen(self):
        self.set_handler = DB_Handle.Handler()
        last_user_set = self.set_handler.get_user_last_set(self.message.chat.id)
        self.set_handler.del_ChatidSetIntermediate_by_setIdself.message.chat.id, last_user_set
        self.text_response = 'Вопрос удален из избранного'
        self.markup = tm.QAMarkup().markup
        self.is_prepared = True




# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, 'Привет! Выбери один из пунктов меню.' + message.from_user.id, reply_markup=Menu.markup)
#
#
#
# @bot.message_handler(func= lambda message: True, content_types=['text'])
# def main_menu(message):
#    if var.is_exist_chatid_chat_id(message.chat.id) == 0:
#        name = 'NoName' if message.from_user.first_name == None else message.from_user.first_name
#        surname = 'NoSoname' if message.from_user.last_name == None else message.from_user.last_name
#        var.add_chatid(message.chat.id, name + ' ' + surname)
#    bot.reply_to(message, 'Привет! Выбери один из пунктов меню.', reply_markup=Menu.markup)