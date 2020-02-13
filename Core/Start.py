from telebot.apihelper import _convert_markup

import Core.Controller.DB_Handle as db_handler
import Core.Controller.Command_Handler_Strategy as ch
from Core.Configuration import *
from Core.Self_Check import Diagnostics
from telebot import *
from telebot import types
from pathlib import  Path
from Core.Controller.Comands import Command_Factory as hm


try:
    diagnostic = Diagnostics(Configuration()).start()
except Exception as e:
    print(e)




bot = TeleBot(Configuration().token)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_messages(message):
    # handler = ch.Handler().Operate(message)
    # handler.template_handler_method()
    # bot.send_message(message.chat.id, handler.text_response, reply_markup=handler.markup)

    sti = open('Static/index.webp', 'rb')
    # bot.send_message(message.chat.id, Path().cwd())
    markup = types.InlineKeyboardMarkup(row_width=2)
    bt1 = types.InlineKeyboardButton('good', callback_data='good_rep')
    bt2 = types.InlineKeyboardButton('bad', callback_data='bad_rep')
    markup.add(bt1, bt2)
    bot.send_sticker(message.chat.id, sti, reply_markup=markup)

@bot.callback_query_handler(func= lambda call: True)
def claback_inline(call):
    print(call.message)

    markup = types.InlineKeyboardMarkup(row_width=2)
    bt1 = types.InlineKeyboardButton('good1', callback_data='good_rep')
    bt2 = types.InlineKeyboardButton('bad1', callback_data='bad_rep')
    print('run')
    bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  reply_markup=markup)


bot.polling()

"""
Все запросы адресовать в Command handler, 
он должен сам обрабатывать запрос и присылать экземпляр View сюда через (Return).
Возможно требуется создать класс хранящий данные ответа.
"""

"""
Реализовать логгирование всех действий этого файла с ротацией логов, путь к логу хранится в файле конфига
"""

