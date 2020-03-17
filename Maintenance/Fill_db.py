from Maintenance import XML_Reader
from Core.Controller import DB_handler
import os
from pathlib import Path


def dump_qa(qa_list):
    import json

    data = {
        'questions': []
        }

    for x in qa_list:
        data['questions'].append({'group': x['group'], 'question': x['question'], 'answer': x['answer']})

    print(data)

    with open('QA.json', 'w', encoding='windows-1251') as outfile:
        json.dump(data, outfile)

var = DB_handler.Handler()

var.create_db_and_tables()

ROOT_DIR = os.path.abspath(os.curdir)
PathToFile = Path(ROOT_DIR)
data = XML_Reader.get(PathToFile / "QASource.xml")

data = sorted(data, key=lambda x: x['group'])

dump_qa(data)
for i in data:
    DB_handler.Handler().add_set(i['group'], i['question'], i['answer'])

DB_handler.Handler().add_group(1, 'ООП, Паттерны, проектирование')
DB_handler.Handler().add_group(2, 'C#')
DB_handler.Handler().add_group(3, 'Базовые вопросы по разработке')
DB_handler.Handler().add_group(4, 'Python')

class user:
    username = None
    first_name = None
    last_name = None

y = user

for x in range(10):
    print(DB_handler.Handler().add_user_acc(107 + x, y.username, y.first_name, y.last_name))

DB_handler.Handler().upd_chat_lastset(107, 11)





# for i in data:
#     v
#     print(i['question'])
#     print(i['answer'])



#var = db_handler.Messages_hanlder()
#var.create_db_and_tables() # path = 1создание бд

