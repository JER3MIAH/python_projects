# an exception is an event detected during execution that interrupts the normal flow of a program

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero")
except ValueError as e:
    print(e)
    print("Enter numbers only")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:      # This gets executed whether we encounter an exception or not
    print("******************")
