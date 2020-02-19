from Core.Self_Check import Diagnostics
import Maintenance.Logger_Configuration
from Core.Controller.Command_Handler_Strategy import Messages_hanlder
from Maintenance.Configuration_Singleton import Configuration
from telebot import *
import logging
import requests



if __name__ == '__main__':

    logging.getLogger(__name__)
    logging.info(('-' * 20) + 'Start app' + ('-' * 20))

    try:
        Diagnostics().Run()
    except Exception as e:
        print(e)

    util.logger.setLevel(
        logging.CRITICAL)  # Mute all logs from util because it can spam with more less level than basic.

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



