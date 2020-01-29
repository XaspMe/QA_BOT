from Core.Controller import DB_Handle, User_validation
from Core.View import Telegram_Markups as tm
import emoji
from Core.Controller.Comands import Command_Factory
from Core.Controller import DB_Handle as db
from telebot import *

"""
Сюда приходят команды пользователя, в зависимости от текста возвращается View с instance ответа.
"""


class Handler:
    def Operate(self, message: str) -> Command_Factory.AbstractHandler:
        if message.text == 'Следующий вопрос':
            if len(db.Handler().get_chosenGroups_by_chatids_id(message.chat.id)) > 0:
                return Command_Factory.NextQuestion(message)
            else:
                return Command_Factory.NotCHosenGroups(message)

        elif message.text == 'Показать ответ':
            return Command_Factory.Answer(message)

        elif message.text == 'Меню' or \
                message.text == 'start' or \
                message.text == 'help' or \
                message.text == '/start' or \
                message.text == '/help':
            return Command_Factory.Menu(message)

        elif message.text == 'Перейти к вопросам':
            if len(db.Handler().get_chosenGroups_by_chatids_id(message.chat.id)) > 0:
                return Command_Factory.NextQuestion(message)
            else:
                return Command_Factory.NotCHosenGroups(message)

        elif message.text == 'Добавить в избранное' or \
                message.text == 'Удалить из избранного':
            return Command_Factory.InvertChosen(message)

        elif message.text == 'Выбрать темы' or \
                '👍' in message.text or \
                '👎' in message.text:
            return Command_Factory.Themes(message)

        else:
            return Command_Factory.Nothing(message)