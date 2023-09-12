import random

while True:
    player = None
    choices = ["rock", "paper", "scissors"]

    while player not in choices:
        player = input("rock, paper, or scissors? ").lower()
    if player in choices:
        computer = random.choice(choices)
        print("Player: "+player)
        print("Computer: "+computer)
    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer == "rock":
        print("you win")
    elif player == "scissors" and computer == "paper":
        print("you win")
    elif player == "paper" and computer == "scissors":
        print("you lose")
    elif player == "rock" and computer == "paper":
        print("you lose")
    elif player == "scissors" and computer == "rock":
        print("you lose")
    answer = input("wanna play again?(y/n) ").lower()
    if answer != "y":
        break
