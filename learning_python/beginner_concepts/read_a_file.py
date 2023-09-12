# how to read the content of a file in python
try:
    with open("C:\\users\\hp\\desktop\\trial.txt") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("File not found")
