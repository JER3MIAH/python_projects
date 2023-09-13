# *args is a parameter that will pack all arguments into a tuple
#

def multiply(*mult):  # the name doesn't matter as long as the asterisk(*) is attached
    result = 1
    for i in mult:
        result = result * i
    return result  # with this for loop, ant amount of arguments can be passed when the function is called


print(multiply(2, 2, 3))
