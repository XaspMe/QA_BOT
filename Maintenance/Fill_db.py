from Maintenance import XML_Reader
from Core.Controller import DB_Handle
import os
from pathlib import Path

var = DB_Handle.Handler()
var.create_db_and_tables()

ROOT_DIR = os.path.abspath(os.curdir)
PathToFile = Path(ROOT_DIR)
data = XML_Reader.get(PathToFile / "QASource.xml")

data = sorted(data, key=lambda x: x['group'])

for i in data:
    DB_Handle.Handler().add_set(i['group'], i['question'], i['answer'])

DB_Handle.Handler().add_group(1, 'ООП, Паттерны, проектирование')
DB_Handle.Handler().add_group(2, 'C#')
DB_Handle.Handler().add_group(3, 'Базовые вопросы по разработке')
DB_Handle.Handler().add_group(4, 'Python')


for x in range(10):
    print(DB_Handle.Handler().add_chatid(107+x, 'user'))

DB_Handle.Handler().upd_chat_lastset(107, 11)





# for i in data:
#     v
#     print(i['question'])
#     print(i['answer'])



#var = db_handler.Handler()
#var.create_db_and_tables() # path = 1создание бд

