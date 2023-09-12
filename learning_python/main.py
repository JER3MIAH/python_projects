import sys
import random

first = int(sys.argv[1])
last = int(sys.argv[2])

numb = random.randint(first, last)

while True:
    guess = input('Guess the number(1-20): ')
    try:
        if numb == int(guess):
            print(numb)
            print('You guessed right')
            break
        elif guess != numb:
            print(f'{guess} is not the right number')
            continue
    except ValueError:
        print('please enter a number')
