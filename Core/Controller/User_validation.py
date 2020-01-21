from Core.Controller import  DB_Handle

class UserValidation:
    """
    Класс валидации состояния пользователя в системе
    """
    def __init__(self, chat):
        """
        :param id:
        """
        self.id = chat.id
        self.name = chat.user_name
        self.handler = DB_Handle.Handler()
        # TODO: добавить имя пользователя в список аргументов

    def check_or_create(self):
        """
        Check what the user exists, else create new one
        :return:
        """
        if self.handler.is_exist_chatid_chat_id(self.id, self.user_name):
            return 1
        else:
            return self.handler.add_chatid(self.id, self.user_name)
