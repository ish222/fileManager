import os

def directory():
    cur = input("Do you want to run this program for its directory? 'Yes' or 'No' Type exit to exit the program!")
    if cur.lower() == "exit":
        print("Thanks for using this file manager!")
        exit()
    global curDir
    if cur.lower() == "yes":
        curDir = os.getcwd()
    else:
        curDir = input("Please input the directory of the files you want to manage: Leave empty to go back!")
        if curDir == "":
            directory()
    print(f"The directory you are working in is: {curDir}")
    move_Files()

def move_Files():
    manage = "." + input("What type of file do you want to manage? E.g. jpeg, exe, mp3... Leave empty to go back!")
    if manage == ".":
        directory()
    # print(manage)
    content = os.listdir(curDir)
    # print("Content of file: ", content)
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
    # print("Dictionary: ", contype)
    if manage[1:] not in content:
        os.mkdir(curDir+"/"+manage[1:])
    print(contype)
    if manage not in contype:
        print("The file type you input doesn't exist, please input another file type!")
        move_Files()
    for x in contype:
        if contype[x] == manage:
            # print(contype[x])
            os.replace(curDir+"/"+x+manage, curDir+"/"+manage[1:]+"/"+x+manage)
    run_again = input("Do you have more files to manage in this directory? 'Yes' or 'No' ")
    def rerun():
        if run_again.lower() == "yes":
            move_Files()
        elif run_again.lower() == "no":
            directory()
        else:
            print("Wrong input, rerun the program to start again!")
            rerun()
    rerun()


directory()
