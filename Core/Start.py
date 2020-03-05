from Core.Self_check import Diagnostics
import Maintenance.Logger_configuration
from Core.Controller.Command_Handler_Strategy import Messages_hanlder
from Maintenance.App_configuration_singleton import Configuration
from telebot import *
import logging
import requests


if __name__ == '__main__':
    try:
        Diagnostics().run()
    except Exception as e:
        print(e)

    bot = TeleBot(Configuration().token)

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def handle_messages(message):
        handler = Messages_hanlder().Operate(message)
        handler.template_handler_method()
        bot.send_message(message.chat.id, handler.text_response, reply_markup=handler.markup)

    try:
        bot.polling()
    except requests.exceptions.SSLError as e:
        logging.error('No connection with telegram')

    logging.info(('-' * 20) + 'App work done' + ('-' * 20))

"""
Все запросы адресовать в Command handler, 
он должен сам обрабатывать запрос и присылать экземпляр View сюда через (Return).
Возможно требуется создать класс хранящий данные ответа.
"""



