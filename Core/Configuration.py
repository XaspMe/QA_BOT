from pathlib import Path

class Configuration:
    """
    Represent application configuration.
    TODO: Создать config.ini файл для чтения конфигурации из него.
    """

    def __init__(self):
        path_to_core = Path(str(Path().cwd())[:str(Path().cwd()).index('QA_BOT') + 6])
        self.db_name = path_to_core / 'QA_DB.db'  # Имя базы данных.
        self.log_name = ""
        self.log_path = ""
        self.token = "698296687:AAFQl6Po6wpxBFXH-qHcrlii9BQCxFDkUJk"  # Telebot token
        self.wan_check_adress = {'8.8.8.8', '09.185.108.134', '209.185.108.135', '209.185.108.138', '209.185.108.139'}

    def init_db_path(self):
        pass
