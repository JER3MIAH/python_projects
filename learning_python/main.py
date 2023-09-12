# my_file = open('text.txt')

# print(my_file.read())

# my_file.close()

try:
    with open('..\\te3xt.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print(err)
