"""
Represent logging configuration
"""

import logging
import sys
from  pathlib import  Path
import os
from logging.handlers import RotatingFileHandler
from Maintenance.Configuration_Singleton import Configuration


logging.basicConfig(format='%(asctime)s | %(levelname)s | %(filename)s | %(module)s | func:%(funcName)s | line:%(lineno)d | %(message)s',
                    handlers=[RotatingFileHandler(Path(os.path.dirname(__file__)).parent / Configuration().log_name,
                                                  maxBytes=2000000,
                                                  backupCount=5),
                              logging.StreamHandler(stream=sys.stdout)],
                    level=logging.INFO
                    )
