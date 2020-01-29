from Core.Model.DB.DB_Model import Groups, Sets, ChatIDs, ChosenGroups, ChatidSetIntermediate
from Core import Configuration as cf
from peewee import *

import random

class ChatidSetIntermediateException(Exception): pass


class Handler(Model):
    """
    Класс контекста базы данных (ORM)
    """
    db = SqliteDatabase(cf.Configuration().db_name)

    def create_db_and_tables(self) -> int:
        """
        Создание базы данных и необходимых таблиц из DB_MODEL.
        """
        with self.db:
            return self.db.create_tables([Groups, Sets, ChatIDs, ChosenGroups, ChatidSetIntermediate])  # Create the tables.


    """
    ACTION UNDER THE ChatIDS
    """
    def get_user_last_set(self, userid):
        return ChatIDs.select(ChatIDs.last_set).where(ChatIDs.chat_id == userid).execute()[0].last_set

    def add_chatid(self, id, username):
        """
        Add new user to table
        :param id: int (T_Chat_ID)
        :param username: string (T_User_Name first+last)
        :return: Code 0 - id exist, Code 1 - OK, Code 3 - wrapped exception
        """
        try:
            return ChatIDs.insert({ChatIDs.chat_id: id}).execute()
        except Exception:
            # :TODO добавить запись ошибки в лог и уточнение ошибок по PEP8.
            raise

    def _is_exist_chat_id(self, chat_id):
        """
        Check what the user is exist in DB
        :param chat_id: int (T_Chat_ID)
        :return: bool type
        """
        try:
            with self.db.atomic():
                return ChatIDs.select().where(ChatIDs.chat_id == chat_id).exists()
        except Exception:
            # :TODO добавить запись ошибки в лог и уточнение ошибок по PEP8.
            raise

    def upd_chat_lastset(self, chat_id, setid):
        """

        :param chat_id: int (T_Chat_ID)
        :param setid: id of last set
        :return:
        """
        try:
            with self.db.atomic():
                ChatIDs.update({ChatIDs.last_set: setid}).where(ChatIDs.chat_id == chat_id).execute()
        except Exception:
            # :TODO добавить запись ошибки в лог и уточнение ошибок по PEP8.
            raise

    def get_chatid_name_by_id(self, chat_id):
        """
        TODO: Упрлс?
        :param chat_id:
        :return: number of affected rows
        """
        with self.db.atomic():
            try:
                return ChatIDs.select(ChatIDs.user_name).where(ChatIDs.chat_id == chat_id).execute()
            except OperationalError:
                raise


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
    def add_set(self, group, question, answer):
        return Sets.insert({Sets.qa_group: group, Sets.question: question, Sets.answer: answer}).execute()

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








