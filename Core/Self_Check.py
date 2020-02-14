from Core.Configuration_Singleton import Configuration
from Core.Controller.DB_Handle import Handler

import os
import platform
import subprocess
import warnings

class DbFileNotFound(Exception): pass # Исключение не найден файл базы данных.
class WanCheckError(Exception): pass # Исключение нет связи с WAN

"""
Цепочка примерно следующая:
Производится попытка сформировать конфиг через конструктор
Проверяется что на месте все файлы
Проверятся что база не пустая (в этом случае запрос по таблице sets)
Проверятся что есть доступ к сети
"""

class Diagnostics:
    """
    Class to diagnose all nodes in System
    """

    def __init__(self):
        pass

    def Run(self):
        """
        :return: True or raise exception
        """
        self._check_configuration()
        self._check_main_files()
        self._ping_addresess()

    def _check_configuration(self):
        try:
            self.config = Configuration()
        except Exception as e: # уточнить ошибку
            raise e

    def _check_main_files(self):
        if not os.path.exists(self.config.get_core_path()):
            raise FileNotFoundError(f'Path {self.configuration.get_core_path()} not found, check system entirety')
        if not os.path.exists(self.config.db_name):
            raise FileNotFoundError(f'DB files on {self.config.db_nam} not found, check DB')
        if not os.path.exists(self.config.log_name):
            warnings.warn(f'Log file on {self.config.log_name} not found')
        if not os.path.exists(self.config.xml_source):
            warnings.warn(f'XML source file on {self.config.xml_source} not found')

    def _ping_addresess(self):
        """
        Check wan accessibility
        :return:
        """
        """
        TODO: Сделать на список устройств.
        """
        param = '-n' if platform.system().lower() == 'windows' else '-c'  # different params for win/linux platform
        for url in self.config.wan_check_adress:
            command = ['ping', param, '1', url]  #
            if subprocess.call(command, stdout=False) == 0:
                return True
        raise WanCheckError(f"Can't ping {self.configuration.wan_check_adress}")

    def _check_db_access_and_data(self):
        if len(Handler().get_sets_count()) == 0:
            warnings.warn(f'Connection with DB was established, but there is no question in sets')

