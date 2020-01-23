from Core.Controller import DB_Handle

class UserValidation:
    """
    Класс валидации состояния пользователя в системе
    """
    def __init__(self, id, name):
        """
        :param id:
        """
        self.id = id
        self.user_name = name
        self.handler = DB_Handle.Handler()
        # TODO: Добавить обновление имени пользоваетеля.

    def check_or_create(self):
        """
        Check what the user exists, else create new one
        :return: Bool value
        """
        try:
            if self.handler.is_exist_chatid_chat_id(self.id, self.user_name):
                return True
            else:
                self.handler.add_chatid(self.id, self.user_name)
                return True
        except Exception as e:
            raise e


