from Core.Model.DB.DB_Model import Groups, Sets, ChatIDs, ChosenGroups
from Core import Configuration as cf
from peewee import *

import random



class Handler(Model):
    """
    Класс контекста базы данных (ORM)
    """
    db = SqliteDatabase(cf.Configuration().db_name)

    def create_db_and_tables(self):
        """
        Создание базы данных и необходимых таблиц из DB_MODEL.
        """
        with self.db:
            return self.db.create_tables([Groups, Sets, ChatIDs, ChosenGroups]) # Create the tables.


    """
    ACTION UNDER THE ChatIDS
    """
    def add_chatid(self, id, username):
        """
        Add new user to table
        :param id: int (T_Chat_ID)
        :param username: string (T_User_Name first+last)
        :return: Code 0 - id exist, Code 1 - OK, Code 3 - wrapped exception
        """
        try:
            return ChatIDs.insert({ChatIDs.chat_id: id, ChatIDs.user_name: username}).execute()
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
    def add_chosen(self, chatid, chosenids):
        """
        Users select them favorite groups
        :param chatid: int (T_Chat_ID)
        :param chosenids: iterable collection PK of groups
        :return:
        """
        try:
            with self.db.atomic():
                for y in chosenids:
                    ChosenGroups.insert({ChosenGroups.chat : chatid, ChosenGroups.group: y}).execute()
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
        return (Groups.select())


    """
    ACTION UNDER THE Sets
    """
    def add_set(self, group, question, answer):
        return Sets.insert({Sets.qa_group: group, Sets.question : question, Sets.answer: answer}).execute()

    def get_random_set_by_groups(self, groups):
        random_group = random.choice(groups)
        return Sets.select(Sets.id, Sets.question).where((Sets.qa_group == random_group)).order_by(fn.Random()).execute()

