"""
Represent logging configuration
"""

import logging
import sys
from telebot import util
import telebot
import peewee
from  pathlib import  Path
import os
from logging.handlers import RotatingFileHandler
from Maintenance.App_configuration_singleton import Configuration


logging.basicConfig(format='%(asctime)s | %(levelname)s | %(filename)s | %(module)s | func:%(funcName)s | line:%(lineno)d | %(message)s',
                    handlers=[RotatingFileHandler(Path(os.path.dirname(__file__)).parent / Configuration().log_name,
                              maxBytes=2000000,
                              backupCount=5),
                              logging.StreamHandler(stream=sys.stdout)],
                    level=logging.DEBUG
                    )


util.logger.setLevel(logging.ERROR)
telebot.logger.setLevel(logging.ERROR)
peewee.logger.setLevel(logging.ERROR)
logging.getLogger('urllib3').setLevel(logging.ERROR)
