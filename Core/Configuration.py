from pathlib import Path

class Configuration:
    """
    Represent application configuration.
    TODO: Создать config.ini файл для чтения конфигурации из него.
    """

    def __init__(self):
        self.db_path = Path.cwd() # TODO: Хранить бд в корне приложения
        self.db_name = self.db_path / 'QA_DB.db'  # Имя базы данных.
        self.log_name = ""
        self.log_path = ""
        self.token = "698296687:AAFQl6Po6wpxBFXH-qHcrlii9BQCxFDkUJk"  # Telebot token
        self.wan_check_adress = '8.8.8.8'

    def init_db_path(self):
        pass
