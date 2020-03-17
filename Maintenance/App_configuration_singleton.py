from __future__ import annotations
from threading import Lock, Thread
from typing import Optional
from pathlib import Path

import os.path
from configparser import ConfigParser

class SingletonMeta(type):

    _instance: Optional[Configuration] = None

    def __call__(self) -> Configuration:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self.path_to_app_root = self.get_root_path()
        self.read_config()

    def read_config(self):
        self.config_ini_path = self.path_to_app_root / 'config.ini'
        self.config = ConfigParser()
        self.config.read(self.config_ini_path)
        self.token = self.config.get('Telegram', 'Token')
        self.log_name = self.path_to_app_root / 'Logs' / self.config.get('application', 'Log_name')
        self.communication_log_name = self.path_to_app_root / 'Logs' / self.config.get('application', 'Communication_log_name')
        self.db_name = self.path_to_app_root / self.config.get('DB', 'DB_name')
        self.wan_check_adress = self.config.get('application', 'WAN_check_addresses').split(';')
        self.xml_source = self.path_to_app_root / 'Maintenance' / self.config.get('application', 'XML_QA_source_name')

    def get_root_path(self) -> Path:
        """
        :return: string: path representation
        """

        path = os.path.dirname(__file__)
        while True:
            if 'QA_BOT' in path:
                temp_path = os.path.dirname(path)
                if 'QA_BOT' in temp_path:
                    path = temp_path
                else:
                    break
            else:
                raise ValueError(f'There is no QA_BOT folder in current path {path}')
        return Path(path)