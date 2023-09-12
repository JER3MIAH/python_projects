# Write a program that prints the result of the addition of all arguments
# The output should be the result of the addition of all arguments, followed by a new line
# You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
# Your code should not be executed when imported
import sys

def add(args):
    result = 0
    for i in args:
        try:
            num = int(i)
            result = result + num
        except ValueError:
            print("Invalid argument")
    return result


if __name__ == "__main__":
    arg = sys.argv[1:]

    res = add(arg)
    print(res)