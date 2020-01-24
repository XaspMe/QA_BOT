from telebot.apihelper import _convert_markup

import Core.Controller.DB_Handle as db_handler
import Core.Controller.Comand_Handler as ch
from Core.Configuration import *
from Core.Self_Check import Diagnostics
from telebot import *



try:
    diagnostic = Diagnostics(Configuration()).start()
except Exception as e:
    print(e)




bot = TeleBot(Configuration().token)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_messages(message):
    handler = ch.Handler(message)
    handler.handle()
    bot.send_message(message.chat.id, handler.text_response, reply_markup=handler.markup)


bot.polling()

"""
Все запросы адресовать в Command handler, 
он должен сам обрабатывать запрос и присылать экземпляр View сюда через (Return).
Возможно требуется создать класс хранящий данные ответа.
"""

"""
Реализовать логгирование всех действий этого файла с ротацией логов, путь к логу хранится в файле конфига
"""

