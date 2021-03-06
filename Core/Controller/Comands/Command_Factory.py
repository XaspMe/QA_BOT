from abc import ABC, abstractmethod
from Core.Controller import DB_handler, UserValidation
from Core.View import Telegram_Markups as ViewMarkups
from Core.Exceptions import *
import logging


class AbstractHandler(ABC):
    """
    Abstract handler for all message handlers.
    """

    def __init__(self, message) -> None:
        logging.getLogger(__name__)
        self.message = message
        self.text_response = ''
        self.prepared = False

    def template_handler_method(self) -> None:
        """
        Template for processing all messages
        """
        self.check_user()
        self.log_question()
        self.prepare_text()
        self.log_answer()
        self.prepare_markup()
        self.write_communictaion_record()

    def check_user(self) -> None:
        """
        Determine account state in database, create new account if not exists in DB.
        """
        validate = UserValidation.UserValidation(self.message.chat.id,
                                                 self.message.from_user)
        validate.check_or_create()

    def log_question(self):
        print(f'Вопрос пользователя: {self.message.text}')
        # TODO: Организовать логгирование

    def init_prepare_result(self, prepared: bool) -> None:
        self.is_prepared = prepared

    @abstractmethod
    def prepare_text(self) -> None:
        pass

    def log_answer(self):
        print(f'Ответ бота: {self.text_response}')
        # TODO: Организовать логгирование

    @abstractmethod
    def prepare_markup(self) -> None:
        pass

    def write_communictaion_record(self):
        try:
            DB_handler.Handler().add_communications_record(user_message=self.message.text,
                                                           bot_response=self.text_response,
                                                           chat_id=self.message.chat.id)
        except Exception as e:
            logging.error(e)

class AdminComandsHandler(AbstractHandler, ABC):

    def check_user(self) -> None:
        validate = UserValidation.UserValidation(self.message.chat.id, self.message.from_user.username)
        validate.check_or_create()
        set_handler = DB_handler.Handler()
        if not set_handler.user_is_admin(self.message.chat.id):
            raise UserAccessError('User is not admin')
    pass

class AdminPanel(AdminComandsHandler):
    def __init__(self, message):
        super().__init__(message)

    def prepare_text(self) -> None:
        self.text_response = 'Панель администраттора'

    def prepare_markup(self):
        self.markup = ViewMarkups.AdminMenu().markup


class NotChosenGroups(AbstractHandler):
    def __init__(self, message):
        super().__init__(message)
        self.set_handler = DB_handler.Handler()

    def prepare_text(self) -> None:
        self.text_response = 'Для перехода к вопросам нужно выбрать хотябы одну группу из тем.'

    def prepare_markup(self) -> None:
        self.groups_list = []
        for theme in self.set_handler.get_groups():
            if self.set_handler.is_group_chosen(self.message.chat.id, theme.id):
                self.groups_list.append('👍 ' + theme.name)
            else:
                self.groups_list.append('👎 ' + theme.name)
        self.markup = ViewMarkups.GroupList(self.groups_list).markup


class NextQuestion(AbstractHandler):
    """
    Обычно конкретные классы переопределяют только часть операций базового
    класса.
    """
    def __init__(self, message):
        super().__init__(message)
        super().init_prepare_result(True)

    def prepare_text(self) -> None:
        self.set_handler = DB_handler.Handler()
        self.selected = []
        for x in self.set_handler.get_chosenGroups_by_chatids_id(self.message.chat.id):
            self.selected.append(x.group_id)
        self.qa_set = self.set_handler.get_random_set_by_groups(self.selected)[0]
        self.set_handler.upd_chat_lastset(self.message.chat.id, self.qa_set.id)
        set_theme = self.set_handler.get_group_name_by_set_id(self.qa_set)
        self.text_response = f'Раздел: {set_theme} \n{self.qa_set.question}'

    def prepare_markup(self) -> None:
        if self.set_handler.is_set_chosen(self.message.chat.id, self.qa_set):
            self.markup = ViewMarkups.QAMarkupSetChosen().markup
        else:
            self.markup = ViewMarkups.QAMarkup().markup


class Themes(AbstractHandler):
    def __init__(self, message):
        super().__init__(message)
        self.set_handler = DB_handler.Handler()

        if '👍' in self.message.text or \
                '👎' in self.message.text:
            self.set_handler.invert_chosen(self.message.chat.id, self.message.text[2:])
        super().init_prepare_result(True)

    def prepare_text(self) -> None:
        self.groups_list = []
        for theme in self.set_handler.get_groups():
            if self.set_handler.is_group_chosen(self.message.chat.id, theme.id):
                self.groups_list.append('👍 ' + theme.name)
            else:
                self.groups_list.append('👎 ' + theme.name)
        self.text_response = 'Выберите группу'

    def prepare_markup(self) -> None:
        self.markup = ViewMarkups.GroupList(self.groups_list).markup


class Menu(AbstractHandler):
    def __init__(self, message):
        super().__init__(message)
        super().init_prepare_result(True)

    def prepare_markup(self) -> None:
        self.markup = ViewMarkups.Menu().markup

    def prepare_text(self) -> None:
        self.text_response = 'Основное меню.'


class Answer(AbstractHandler):
    def __init__(self, message):
        super().__init__(message)
        super().init_prepare_result(True)
        self.set_handler = DB_handler.Handler()

    def prepare_text(self) -> None:
        self.last_set = self.set_handler.get_user_last_qa_set(self.message.chat.id)
        self.text_response = self.set_handler.get_answer_by_set_id(self.last_set)

    def prepare_markup(self) -> None:
        if self.set_handler.is_set_chosen(self.message.chat.id, self.last_set):
            self.markup = ViewMarkups.QAMarkupSetChosen().markup
        else:
            self.markup = ViewMarkups.QAMarkup().markup


class InvertChosen(AbstractHandler):
    def __init__(self, message):
        super().__init__(message)
        self.set_handler = DB_handler.Handler()
        last_user_set = self.set_handler.get_user_last_qa_set(self.message.chat.id)
        self.set_chosen = None
        if self.set_handler.is_set_chosen(self.message.chat.id, last_user_set):
            self.set_handler.del_ChatidSetIntermediate_by_setId(self.message.chat.id, last_user_set)
            self.set_chosen = False
        else:
            self.set_handler.add_to_ChatidSetIntermediate(self.message.chat.id, last_user_set)
            self.set_chosen = True
        super().init_prepare_result(True)

    def prepare_text(self) -> None:
        if self.set_chosen:
            self.text_response = 'Вопрос добавлен в избранное'
        else:
            self.text_response = 'Вопрос удален из избранного'

    def prepare_markup(self) -> None:
        if self.set_chosen:
            self.markup = ViewMarkups.QAMarkupSetChosen().markup
        else:
            self.markup = ViewMarkups.QAMarkup().markup


class Nothing(AbstractHandler):
    def __init__(self, message):
        super().__init__(message)

    def prepare_text(self) -> None:
        self.text_response = 'Я еще пока не знаю такой команды, но вот меню.'

    def prepare_markup(self) -> None:
        self.markup = ViewMarkups.Menu().markup
