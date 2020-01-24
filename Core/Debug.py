from Core.Self_Check import *
from Core.Configuration import Configuration
from pathlib import Path

var = Diagnostics(Configuration())

p = r'C:\Users\S.Tsutsulenko\Documents\Git\QA_BOT\Coresdfsdfdsf'
print(Path(p[:p.index('Core')+4]))


