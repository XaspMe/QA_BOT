from Core.Self_Check import *
from Core.Configuration import Configuration
from Core.Controller import Sets_Handler, DB_Handle
from pathlib import Path

c1 = Configuration()

for x in c1.wan_check_adress:
    print(x)
c2 = Configuration()

if id(c1) == id(c2):
    print('ok')




