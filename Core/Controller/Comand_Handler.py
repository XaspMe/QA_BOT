from Core.Controller import User_validation, Sets_Handler, DB_Handle
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
<<<<<<< HEAD
        self.set_handler = Sets_Handler.SetsHandler()
        self.message = message
        self.is_prepared = None
=======
        self.message = message
        self.text_response = 'Test'
>>>>>>> Pre-prod

    def handle(self):
        print(self.message.text)
        validate = User_validation.UserValidation(self.message.chat.id, self.message.from_user.username)
        validate.check_or_create()

        if self.message.text == 'Следующий вопрос':
            self.__next_question()

<<<<<<< HEAD
        if self.message.text == 'Показать ответ':
            self.__show_answer()

    def __hello(self):
        pass

    def __next_question(self):
        qa_set = self.set_handler.get_random_set((1, 2, 3, 4))[0]

=======
>>>>>>> Pre-prod
        self.text_response = qa_set.question
        self.markup = tm.QAMarkup().markup
        db.Handler().upd_chat_lastset(self.message.chat.id, qa_set.id)
        self.is_prepared = True

    def __show_answer(self):
        last_set = self.set_handler.get_user_last_set()
        self.text_response = self.set_handler.get_answer_by_set_id(last_set)
        self.markup = tm.QAMarkup().markup
        self.is_prepared = True
        pass





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