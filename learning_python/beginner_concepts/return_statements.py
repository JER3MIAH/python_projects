# return statements are used within functions to send values/objects back to the caller

def add(num1, num2):
    outcome = num1 + num2
    return outcome


x = add(30, 20)  # to see the value returned by the function, you need to assign the fuction to a variable
#                   or print the function directly

print(x)
