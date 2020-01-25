from Core.Configuration import Configuration
import os
import platform
import subprocess


class DbFileNotFound(Exception): pass # Исключение не найден файл базы данных.
class WanCheckError(Exception): pass # Исключение нет связи с WAN


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
        Check wan accessibility
        :return:
        """
        """
        TODO: Сделать на список устройств.
        """
        param = '-n' if platform.system().lower() == 'windows' else '-c'  # different params for win/linux platform
        for url in self.configuration.wan_check_adress:
            command = ['ping', param, '1', url]  #
            if subprocess.call(command, stdout=False) == 0:
                return True
        raise WanCheckError(f"Can't ping {self.configuration.wan_check_adress}")
