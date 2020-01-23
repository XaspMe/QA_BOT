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
    def __init__(self, chat):
        self.chat = chat


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Выбери один из пунктов меню.' + message.from_user.id, reply_markup=Menu.markup)



@bot.message_handler(func= lambda message: True, content_types=['text'])
def main_menu(message):
   if var.is_exist_chatid_chat_id(message.chat.id) == 0:
       name = 'NoName' if message.from_user.first_name == None else message.from_user.first_name
       surname = 'NoSoname' if message.from_user.last_name == None else message.from_user.last_name
       var.add_chatid(message.chat.id, name + ' ' + surname)
   bot.reply_to(message, 'Привет! Выбери один из пунктов меню.', reply_markup=Menu.markup)