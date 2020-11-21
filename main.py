import os


def directory():  # Obtains working directory from user
    cur = input("Do you want to run this program for its directory? 'Yes' or 'No' Type exit to exit the program!")
    if cur.lower() == "exit":
        print("Thanks for using the file manager!")
        exit()
    global curDir
    if cur.lower() == "yes":
        curDir = os.getcwd()
    elif curDir.lower() == "no":
        curDir = input("Please input the directory of the files you want to manage: Leave empty to go back!")
        if not os.path.exists(curDir):  # Checks if input path exists
            print("You input an invalid directory! Please try again.")
            directory()
        if curDir == "":
            directory()
    else:
        print("Invalid input, please try again.")
        directory()
    print(f"\nThe directory you are working in is: {curDir}\n")
    move_Files()


def move_Files():
    manage = "." + input("What type of file do you want to manage? E.g. jpg, exe, mp3... Leave empty to go back!")
    if manage == ".":
        directory()
    print(manage)
    content = os.listdir(curDir)  # Creates a list of all the content in that directory
    print("Content of directory: ", content)
    contype = {}  # Creates a dictionary to store each file name in the directory as the key and the file type as the value
    for i in content:  # Loops through the content to separate the files into their names and file extensions
        length = len(i)
        index = -1
        while abs(index) < length:
            if i[index] == ".":
                contype[i[:index]] = i[index:]
                break
            else:
                index -= 1
    print("Dictionary: ", contype)
    if (manage in contype.values()) and (manage[1:] not in content):  # If the file type doesn't have a complementary folder, a new one is created
        os.mkdir(curDir+"/"+manage[1:])
    # print(contype)
    elif not (manage in contype.values()):
        print("The file type you input doesn't exist, please input another file type!")
        move_Files()
    for x in contype:  # This for loop iterated through each file that matches the file type and moves it to its corresponding folder
        if contype[x] == manage:
            # print(contype[x])
            os.replace(curDir+"/"+x+manage, curDir+"/"+manage[1:]+"/"+x+manage)
    run_again = input("Do you have more files to manage in this directory? 'Yes' or 'No' ")

    def rerun():  # Allows user to rerun the program
        if run_again.lower() == "yes":
            move_Files()
        elif run_again.lower() == "no":
            directory()
        else:
            print("Wrong input, rerun the program to start again!")
            rerun()
    rerun()


directory()
