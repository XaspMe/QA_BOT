from Maintenance.Configuration_Singleton import Configuration
from Core.Controller.DB_Handle import Handler

import os
import platform
import subprocess
import warnings
import logging

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
        logging.getLogger(__name__)
        pass

    def Run(self):
        """
        :return: True or raise exception
        """
        logging.info('Run self diagnostic')
        self._check_configuration()
        self._check_main_files()
        self._ping_addresess()

    def _check_configuration(self):
        logging.info('Check configuration')
        try:
            self.config = Configuration()
            logging.info('Check configuration passed')
        except Exception as e: # уточнить ошибку
            logging.error(e)
            raise e

    def _check_main_files(self):
        logging.info('Verification of main files')
        if not os.path.exists(self.config.get_root_path()):
            logging.warning(f'Path {self.configuration.get_root_path()} not found, check system entirety')

        if not os.path.exists(self.config.db_name):
            logging.warning(f'DB files on {self.config.db_nam} not found, check DB')

        if not os.path.exists(self.config.log_name):
            logging.warning(f'Log file on {self.config.log_name} not found')

        if not os.path.exists(self.config.xml_source):
            logging.warning(f'XML source file on {self.config.xml_source} not found')

        logging.info('Verification of main files completed')

    def _ping_addresess(self):
        """
        Check wan accessibility
        :return:
        """
        """
        TODO: Сделать на список устройств.
        """
        logging.info('Check WAN access')
        param = '-n' if platform.system().lower() == 'windows' else '-c'  # different params for win/linux platform
        for url in self.config.wan_check_adress:
            command = ['ping', param, '1', url]  #
            if subprocess.call(command, stdout=False) == 0:
                logging.info('Check WAN access passed')
                return True
        raise WanCheckError(f"Can't ping {self.configuration.wan_check_adress}")
        logging.error('Check WAN access failed')

    def _check_db_access_and_data(self):
        logging.info('Validating data in database tables')
        if len(Handler().get_sets_count()) == 0:
            logging.warning(f'Connection with DB was established, but there is no question in sets')
        else:
            logging.info('Validating data in database tables passed')

