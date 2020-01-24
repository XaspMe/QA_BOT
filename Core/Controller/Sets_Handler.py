from Core.Controller import dh

var = dh.Handler()


class SetsHandler:
    def __init__(self):
        self.db_handler = dh.Handler()

    def get_random_set(self, groups):
        return self.db_handler.