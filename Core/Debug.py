from Core.Self_Check import *
from Core.Configuration import Configuration
from Core.Controller import Sets_Handler, DB_Handle
from pathlib import Path

var = Diagnostics(Configuration())

#print(DB_Handle.Handler().get_answer_by_set_id().answer)
print(DB_Handle.Handler().get_user_last_set(107))

var = DB_Handle.Handler()

var.add_chosen(107, (1,2,3,4))





