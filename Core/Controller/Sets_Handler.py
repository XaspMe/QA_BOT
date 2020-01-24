from Core.Controller import DB_Handle as dh

var = dh.Handler()


class SetsHandler:
    def __init__(self):
        self.db_handler = dh.Handler()

    def get_random_set(self, groups):
        return self.db_handler.get_random_set_by_groups(groups)