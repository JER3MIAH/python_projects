# how to delete files using python

import os
import shutil

path = "emptfolder"

try:
    #os.rmdir(path)  # delete a folder
    # shutil.rmtree(path)  # removes a directory along with its contents
except FileNotFoundError as e:
    print(e)
    print("File not found")
else:
    print(+path+" was deleted")
