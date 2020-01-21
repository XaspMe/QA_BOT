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
    print(var.add_set(i['group'], i['question'], i['answer']))
