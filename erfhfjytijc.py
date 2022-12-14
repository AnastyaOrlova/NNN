import datetime
import  os
import datetime

id = int(1)
path = r"notes/" + str(id) + ".txt"
time_c = datetime.datetime.fromtimestamp(os.path.getctime(path))
time_u = os.path.getmtime(path)

print(time_c)
print(time_u)