import random

x = random.randint(1, 6)  # prints a random number btw 1 and 6
y = random.random()  # prints a random number btw 0 and 1

janken = ["rock", "paper", "scissors"]
z = random.choice(janken)  # kind of like playing the rock paper scissors game

cards = ["K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, "A"]

random.shuffle(cards)  # shuffles the cards

print(cards)
