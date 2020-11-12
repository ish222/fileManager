import os
from pathlib import Path

cur = input("Do you want to run this program for its directory? 'Yes' or 'No' ")
if cur.lower() == "yes":
    curDir = os.getcwd()
else:
    curDir = input("Please input the directory of the files you want to manage: ")
print(curDir)

manage = "." + input("What type of file do you want to manage? E.g. jpeg, exe, mp3...")
print(manage)
content = os.listdir(curDir)
print("Content of file: ", content)
contype = {}
for i in content:
    length = len(i)
    index = -1
    while abs(index) < length:
        if i[index] == ".":
            contype[i[:index]] = i[index:]
            break
        else:
            index -= 1
print("Dictionary: ", contype)
if manage[1:] not in content:
    os.mkdir(curDir+"/"+manage[1:])
for x in contype:
    print(x)
    print("File Type: ", contype[x])
    if contype[x] == manage[1:]:
        print(contype[x])
        os.replace(curDir+"/"+x+manage, curDir+"/"+manage[1:]+x+manage)

        