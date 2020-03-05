from Core.Controller import DB_handler as dh
import logging

var = dh.Handler()


class SetsHandler:
    def __init__(self):
        logging.getLogger(__name__)
        logging.debug('Initiated')
        self.db_handler = dh.Handler()

    def get_random_set(self, groups):
        logging.debug('Called')
        return self.db_handler.get_random_set_by_groups(groups)