from __future__ import annotations
from threading import Lock, Thread
from typing import Optional
from pathlib import Path

import os.path
import configparser

class SingletonMeta(type):

    _instance: Optional[Configuration] = None

    def __call__(self) -> Configuration:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self.path_to_core = self.get_core_path()
        self.path_to_app_root = Path(self.path_to_core).parent
        self.read_config()

    def read_config(self):
        self.config_ini_path = self.path_to_app_root / 'config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.config_ini_path)
        self.log_name = self.path_to_app_root / self.config.get('application', 'Log_name')
        self.db_name = self.path_to_app_root / self.config.get('DB', 'DB_name')
        self.token = self.config.get('Telegram', 'Token')
        self.wan_check_adress = self.config.get('application', 'WAN_check_addresses').split(';')

    def get_core_path(file_name: str = __file__) -> str:
        """

        :return: string: path representation
        """

        path = str(Path.cwd())
        while True:
            if 'Core' in path:
                temp_path = os.path.dirname(path)
                if 'Core' in temp_path:
                    path = temp_path
                else:
                    break
            else:
                raise ValueError(f'There is no "{file_name}" file in current path {path}')
        return path