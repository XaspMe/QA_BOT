from peewee import *
from Maintenance import App_configuration_singleton as cf
import datetime


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase(cf.Configuration().db_name)


class Groups(BaseModel):
    """
    Represent Groups of questions, for example (OOP, C#, PYTHON, GENERAL DEV QUESTION)
    """
    id = IntegerField(unique=True)  # PK
    name = TextField(unique=True, null=False)  # group name


class Sets(BaseModel):
    """
    Represent sets of questions and answers
    """
    id = AutoField()  # PK
    question = TextField(null=False)
    answer = TextField(default='Истина рядом. Ответа пока нет, но можно предложить свой вариант через Report', null=False)
    qa_group = ForeignKeyField(Groups, null=False)  # Relation with some group (1 to 1)
    is_hidden = BooleanField(default=False, null=False)  # Do not show question in prod


class ChatIDs(BaseModel):
    """
    Save all users to table and them step/state of using
    """
    id = AutoField()  # PK
    chat_id = TextField(null=False)  # Telegram chat ID
    user_name = TextField(null=True)  # NickName
    first_name = TextField(null=True)
    last_name = TextField(null=True)
    is_admin = BooleanField(null=False, default=False)
    last_set = ForeignKeyField(Sets, null=True)  # Last set of conversation.


class ChosenGroups(BaseModel):
    """
    User selected groups
    """
    id = AutoField()  # PK
    chat = ForeignKeyField(ChatIDs, null=False)  # chat FK
    group = ForeignKeyField(Groups, null=False)  # group FK


class ChatidSetIntermediate(BaseModel):
    """
    User chosen set
    """
    id = AutoField()
    chat = ForeignKeyField(ChatIDs, null=False)  # chat FK
    set = ForeignKeyField(Sets, null=False)  # set FK


class CommunicationsRecords(BaseModel):
    """
    All conversation record
    """
    id = AutoField()
    chat = ForeignKeyField(ChatIDs, null=False)  # chat FK
    user_message = TextField(null=True, default='_')
    bot_response = TextField(null=True, default='_')
    time_stamp = DateTimeField(null=False, default = datetime.datetime.now) #