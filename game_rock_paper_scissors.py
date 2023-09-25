import random

choices = ["rock", "paper", "scissors"]


while True:
    computer = random.choice(choices)
    #print(computer)

    player = None
    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player==computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
        elif computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lost!")

    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
        elif computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lost!")

    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
        elif computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lost!")

    play_again = input("Play again? (yes/no)").lower()

    if play_again != "yes":
        break

print("Bye!")