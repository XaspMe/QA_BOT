from Core.Configuration import Configuration
import os


class DbFileNotFound(Exception): pass # Исключение не найден файл базы данных.


class Diagnostics:
    """
    Class to diagnose all nodes in System
    """

    def __init__(self, configuration):
        self.configuration = configuration
        pass

    def start(self):
        """
        Responsibility chain.
        :return: True or raise exception
        """
        return self._check_db(self.configuration.db_name)
        pass

    def _check_db(self):
        """
        Check that file from path is exist
        :param path: path to db file
        :return: True or DbFileNotFound(exception)
        """
        if os.path.exists(self.configuration.path): # Function exist return bool
            return True
        else:
            raise DbFileNotFound(f'On path {self.configuration.db_name}')  # тут используется интерполяция строк

    def _ping_telegram(self):
        """
         TODO: Создать метод возвращающий True, если 'address' доступен командой 'Ping', иначе вызывать 'свое' искючение.

         Пример, в функции выше, raise вызывает ошибку которая описана в начале файла.
         Ошибка наследуется от Exception, вместе с ее конструктором, полями и т.д
        """

        address = self.configuration.wan_check_adress
        pass


