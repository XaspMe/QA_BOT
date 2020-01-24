from Core.Self_Check import *
from Core.Configuration import Configuration
from Core.Controller.Sets_Handler import SetsHandler as sh
from pathlib import Path

var = Diagnostics(Configuration())


for x in range(1000):
    print(sh().get_random_set((1,2,3,4))[0].id)






