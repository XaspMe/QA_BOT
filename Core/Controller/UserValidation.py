from Core.Controller import DB_handler
import logging
from telebot import types

class UserValidation:
    """
    Класс валидации состояния пользователя в системе
    """
    def __init__(self, chat_id: int, user: types.User):
        logging.getLogger(__name__)
        logging.debug('Called')
        self.id = chat_id
        self.user = user
        self.handler = DB_handler.Handler()

    def check_or_create(self):
        """
        Check what the user exists, else create new one
        :return: Bool value
        """
        try:
            if self.handler.is_exists_user_acc(self.id):
                return True
            else:
                self.handler.add_user_acc(self.id,
                                          self.user.username,
                                          self.user.first_name,
                                          self.user.last_name)
                return True
        except Exception as e:
            logging.error(e)
            raise e




