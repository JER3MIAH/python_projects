import os

path = "C:\\Users\\HP\\Desktop\\trial.txt"

if os.path.exists(path):  # checks is the location exists
    print("That location exists")
    if os.path.isfile(path):  # checks is the indicated is a file
        print("That is a file")
    elif os.path.isdir(path):  # checks is the indicated is a directory
        print("That is a directory")
else:
    print("That location doesn't exist")
