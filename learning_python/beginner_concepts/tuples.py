# A tuple is like a list, but they are ordered and unchangeable

developer = ("Jeremiah", 20, "male", "male")

print(developer.index("Jeremiah"))  # shows the index(location) of the value entered
print(developer.count("male"))  # counts number of times a value appears in the tuple

for x in developer:  # printing out the entire tuple with a for loop
    print(x, end=" | ")

if "Jeremiah" in developer:  # checks if a value exists within the tuple
    print("Jeremiah is here")
