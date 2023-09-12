# how to move a file in python

import os

source = "testing.py"
destination = "C:\\users\\hp\\desktop\\testing.py"

try:
    if os.path.exists(destination):
        print("There is a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print("File not found")