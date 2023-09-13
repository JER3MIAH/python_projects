# how to write files in python

text = "\nHave a nice day"

with open("C:\\users\\hp\\desktop\\trial.txt", 'a') as file:  # 'a' to append and 'w' to overwrite
    file.write(text)
