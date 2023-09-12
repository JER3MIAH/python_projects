# nested function calls are function calls inside other function calls
#   the innermost function calls are resolved first
#   returned value is used as argument for the other function

num = input("Enter a number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

# we can shorten the above code to one line using nested function calls

print(round(abs(float(input("Enter a number: ")))))
