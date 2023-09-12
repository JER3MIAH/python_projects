# str.format() is an optional method that gives users more control when displaying output

beast = 'phoenix'
item = 'house'

print("The "+beast+" burnt the "+item+" to cinders")
print("The {} burnt the {} to cinders".format(beast, item))  # parameters have to be in order
print("The {1} burnt the {0} to cinders".format(item, beast))  # you can specify the order[positional arguments]
print("The {beast} burnt the {item} to cinders".format(beast='phoenix', item='house'))  # keyword arguments

text = "The {} burnt the {} to cinders"
print(text.format(beast, item))

print()
print("********************************")
#  How to add a padding to a string when we display it with the format method
name = "Jeremiah"

print("My name is {}. Nice to meet you".format(name))
print("My name is {:19}. Nice to meet you".format(name))  # left align by default
print("My name is {:<19}. Nice to meet you".format(name))  # left align
print("My name is {:>19}. Nice to meet you".format(name))  # right align
print("My name is {:^19}. Nice to meet you".format(name))  # center align

print()
print("********************************")
# lets format some numbers

num = 3000000000.00000

print("The number pi is {:.2f}".format(num))
print("The number pi is {:,}".format(num))
