import dataclasses
from datetime import datetime as DT 
current=DT.today()
print(current)
#manipulations
now_time=DT.now()
print(now_time.strftime("%m-%d-%y %H-%M-%S"))
