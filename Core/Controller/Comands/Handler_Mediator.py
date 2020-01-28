from abc import ABC, abstractmethod
from Core.Controller import DB_Handle, User_validation
from Core.View import Telegram_Markups as tm
import emoji
from Core.Controller import DB_Handle as db
from telebot import *


class AbstractHandler(ABC):

    def __init__(self, message) -> None:
        self.message = message
        self.text_response = ''
        self.prepared = False

    def template_handler_method(self) -> None:
        self.check_user()
        self.print_question()
        self.prepare_text()
        self.print_answer()
        self.prepare_markup()
        self.init_prepare_result()

    # Эти операции уже имеют реализации.

    def check_user(self) -> None:
        validate = User_validation.UserValidation(self.message.chat.id, self.message.from_user.username)
        validate.check_or_create()

    def print_question(self):
        print(f'Ответ бота: {self.message.text}')
        # TODO: Организовать логгирование

    @abstractmethod
    def prepare_text(self) -> None:
        pass

    def print_answer(self):
        print(f'Ответ бота: {self.answer}')
        # TODO: Организовать логгирование

    @abstractmethod
    def prepare_markup(self) -> None:
        pass

    @abstractmethod
    def init_prepare_result(self):
        pass


class NextQuestion(AbstractHandler):
    """
    Обычно конкретные классы переопределяют только часть операций базового
    класса.
    """
    def __init__(self, message):
        super().__init__(message)

    def prepare_text(self) -> None:
        self.set_handler = DB_Handle.Handler()
        self.selected = []
        for x in self.set_handler.get_chosen_by_chatids_id(self.message.chat.id):
            self.selected.append(x.group_id)
        if not len(self.selected) < 1:
            self.qa_set = self.set_handler.get_random_set_by_groups(self.selected)[0]
            self.set_handler.upd_chat_lastset(self.message.chat.id, self.qa_set.id)
            set_theme = self.set_handler.get_group_name_by_set_id(self.qa_set)
            self.text_response = f'Раздел: {set_theme} \n{self.qa_set.question}'
        else:
            self.__chose_themes()

    def prepare_markup(self) -> None:
        if not len(self.selected) < 1:
            if self.set_handler.is_set_chosen(self.message.chat.id, self.qa_set):
                self.markup = tm.QAMarkupSetChosen().markup
            else:
                self.markup = tm.QAMarkup().markup
        else:
            self.__chose_themes()

    def init_prepare_result(self):
        self.is_prepared = True



