# index operators [] give access to a sequence's element they include but are not limited to :(str, list, tuples)

name = "Jeremiah Owoade!"

if name[0].islower():  # checks if the first index of 'name' is a lowercase
    name = name.capitalize()  # if yes, capitalize it

first_name = name[0:8].upper()  # using index operator to identify the first name in the name variable
last_name = name[9:].upper()
last_character = name[-1]   # prints the last element in a sequence

print(first_name)
print(last_name)
print(last_character)
