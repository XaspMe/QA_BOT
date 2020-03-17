from Core.Model.DB.DB_model import Groups, Sets, ChatIDs, ChosenGroups, ChatidSetIntermediate, CommunicationsRecords
from Maintenance import App_configuration_singleton as Config
from peewee import *

import random
import logging


class Handler(Model):
    """
    Handler of all actions under the DB.
    """

    def __init__(self):
        logging.getLogger(__name__)
        self.db = SqliteDatabase(Config.Configuration().db_name)

    def create_db_and_tables(self) -> None:
        """
        Creating database with all tables and constraints. File will be created in app root folder.
        """
        logging.debug('Called')
        with self.db:
            return self.db.create_tables([Groups,
                                          Sets,
                                          ChatIDs,
                                          ChosenGroups,
                                          ChatidSetIntermediate,
                                          CommunicationsRecords])  # Create the tables.

    """
    Action under the user accounts below
    """
    def get_user_last_qa_set(self, user_id: int) -> ChatIDs.last_set:
        """
        Get user last question and answer set.
        """
        logging.debug('Entry')
        result = ChatIDs.select(ChatIDs.last_set).where(ChatIDs.chat_id == user_id).execute()[0].last_set
        logging.debug('Возвращаемый результат ' + repr(result))
        return result

    def add_user_acc(self, user_id : int, username: str, first_name: str, last_name: str):
        """
        Add new user to table
        """
        logging.debug('Called')
        try:
            return ChatIDs.insert({
                                   ChatIDs.chat_id: user_id,
                                   ChatIDs.user_name: username,
                                   ChatIDs.first_name: first_name,
                                   ChatIDs.last_name: last_name
                                   }
                                  ).execute()
        except Exception as e:
            logging.error(e)

    def is_exists_user_acc(self, chat_id):
        """
        Check what the user is exist in DB
        :param chat_id: int (T_Chat_ID)
        :return: bool type
        """
        logging.debug('Called')
        try:
            with self.db.atomic():
                return ChatIDs.select().where(ChatIDs.chat_id == chat_id).exists()
        except Exception as e:
            logging.error(e)

    def upd_chat_lastset(self, chat_id, setid):
        """

        :param chat_id: int (T_Chat_ID)
        :param setid: id of last set
        :return:
        """
        logging.debug('Called')
        try:
            with self.db.atomic():
                ChatIDs.update({ChatIDs.last_set: setid}).where(ChatIDs.chat_id == chat_id).execute()
        except Exception as e:
            logging.error(e)

    def get_chatid_name_by_id(self, chat_id):
        """
        TODO: Упрлс?
        :param chat_id:
        :return: number of affected rows
        """
        logging.debug('Called')
        with self.db.atomic():
            try:
                return ChatIDs.select(ChatIDs.user_name).where(ChatIDs.chat_id == chat_id).execute()
            except OperationalError as e:
                logging.error(e)

    def make_user_admin(self, chat_id):
        logging.debug('Called')
        try:
            return ChatIDs.update({ChatIDs.is_admin: True}).where(ChatIDs.chat_id == chat_id).execute()
        except Exception as e:
            logging.error(e)

    def user_is_admin(self, chat_id):
        logging.debug('Called')
        try:
            return ChatIDs.select(ChatIDs.is_admin).where(ChatIDs.chat_id == chat_id).execute()[0].is_admin
        except Exception as e:
            logging.error(e)

    """
    ACTION UNDER THE ChosenGroups
    """
    def is_group_chosen(self, chat_id, group_id):
        if len(ChosenGroups.select().where((ChosenGroups.chat == chat_id) \
                                                 & (ChosenGroups.group == group_id)).execute()) > 0:
            return True
        else:
            return False

    def get_chosenGroups_by_chatids_id(self, chat_id):
        return ChosenGroups.select(ChosenGroups.group, ChosenGroups.group_id).where(ChosenGroups.chat == chat_id).execute()

    def invert_chosen(self, chatid, chosentext):
        print(chosentext)
        chosenids = None
        chosenids = Groups.select(Groups.id).where(Groups.name == chosentext).execute()[0].id
        if self.is_group_chosen(chatid, chosenids):
            ChosenGroups.delete().where((ChosenGroups.chat == chatid) & (ChosenGroups.group == chosenids)).execute()
        else:
            self.add_chosen(chatid, (chosenids,))


    def add_chosen(self, chatid, chosenids):
        """
        Users select them favorite groups
        :param chatid: int (T_Chat_ID)
        :param chosenids: iterable collection PK of groups
        :return:
        """
        try:
            with self.db.atomic():
                for ids in chosenids:
                    if not self.is_group_chosen(chatid, ids):
                        ChosenGroups.insert({ChosenGroups.chat : chatid, ChosenGroups.group: ids}).execute()
        except Exception:
            # :TODO добавить запись ошибки в лог и уточнение ошибок по PEP8.
            raise
            pass

    def del_chosen_for_chatid(self, chatid):
        """
        Del all chosen groups for current chatid
        :param chatid: int (T_Chat_ID)
        :return: Number of affected rows or err
        """
        return ChosenGroups.delete().where(ChosenGroups.chat == chatid).execute()

    def upd_chosen(self, chatid, chosenids):
        """
        Del all chosen groups, then add another
        :param chatid: int (T_Chat_ID)
        :param chosenids:
        :return: Number of affected rows
        """
        self.del_chosen_for_chatid(chatid)
        return self.add_chosen(chatid, chosenids)



    """
    ACTION UNDER THE Groups
    """
    def add_group(self, data):
        """
        Add
        :param data:
        :return:
        """
        with self.db.atomic():
            return Groups.insert_many(data).execute()


    def get_groups(self):
        return Groups.select().execute()



    def get_group_name_by_id(self, id):
        return Groups.select().where(Groups.id == id).execute()[0].name

    def get_group_name_by_set_id(self, id):
        set_id = Sets.select(Sets.qa_group).where(Sets.id == id).execute()
        if len(set_id) > 0:
            return self.get_group_name_by_id(set_id[0].qa_group)
        else:
            #TODO: Добавить кастомное исключение
            pass




    """
    ACTION UNDER THE Sets
    """
    def get_sets_count(self):
        cnt = Sets.select().execute()
        return cnt

    def add_set(self, group, question, answer):
        return Sets.insert({Sets.qa_group: group, Sets.question: question, Sets.answer: answer}).execute()

    def remove_set(self, id):
        return Sets.delete().where(Sets.id == id).execute()

    def get_random_set_by_groups(self, groups):
        random_group = random.choice(groups)
        return Sets.select(Sets.id, Sets.question).where(Sets.qa_group == random_group).order_by(fn.Random()).execute()

    def get_answer_by_set_id(self, last_set):
        return Sets.select(Sets.answer).where(Sets.id == last_set).execute()[0].answer


    """
    Actions under the groups
    """

    def get_groups(self):
        return Groups.select(Groups.name, Groups.id).execute()

    def add_group(self, id, name):
        return Groups.insert({Groups.id: id, Groups.name: name}).execute()

    """
    Actions under the ChatidSetIntermediate
    """
    def is_set_chosen(self, chat_id, set_id):
        if len(ChatidSetIntermediate.select().where((ChatidSetIntermediate.chat == chat_id) \
                                                 & (ChatidSetIntermediate.set == set_id)).execute()) > 0:
            return True
        else:
            return False

    def add_to_ChatidSetIntermediate(self, chat_id: int, set_id: int) -> None:
        if self.is_set_chosen(chat_id, set_id):
            pass
        else:
            ChatidSetIntermediate.insert({ChatidSetIntermediate.chat: chat_id, ChatidSetIntermediate.set: set_id}).execute()

    def get_ChatidSetIntermediate_sets_ids(self, chat_id):
        return ChatidSetIntermediate.select(ChatidSetIntermediate.set).where(ChatidSetIntermediate.chat == chat_id).execute()

    def del_ChatidSetIntermediate_by_setId(self, chat_id, set_id):
        return ChatidSetIntermediate.delete().where((ChatidSetIntermediate.chat == chat_id) \
                                                & (ChatidSetIntermediate.set == set_id)).execute()

    """
    Actions under the CommunicationsRecords table
    """
    def add_communications_record(self, chat_id, user_message, bot_response):
        try:
            CommunicationsRecords.insert({CommunicationsRecords.user_message: user_message,
                                          CommunicationsRecords.bot_response: bot_response,
                                          CommunicationsRecords.chat: chat_id}).execute()
        except Exception as e:
            logging.error(e)







