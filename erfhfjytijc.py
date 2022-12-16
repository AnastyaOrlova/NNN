import datetime
import linecache
import  os
import datetime
import random
import string

#id = int(1)
#path = r"notes/" + str(id) + ".txt"
#time_c = datetime.datetime.fromtimestamp(os.path.getctime(path))
#time_u = os.path.getmtime(path)

#print(time_c)
#print(time_u)

#letters = string.ascii_lowercase
#token = ''.join(random.sample(letters, 4))
#t = open("tokens.txt", "a")
#id = 11
#line = str('\n' + str(id) + ". " + token)
#t.write(line)

#token = str("rrrr")
#t = linecache.getline('tokens.txt', 1)
#t = t.split()
#t = t[1]
#if token == t:
#    print(t)
n = 1
e = 1
token = str('guiy')
file1 = open("tokens.txt", "r")
id = 1
lines = file1.readlines()
for line in lines:
    a = line.split(". ")
    if a[0] == str(id):
        t = str(a[1])
        print(t)

print(type(t))
print(type(token))
if token == t:
    print("уже")
else:
    print("хуйня")
