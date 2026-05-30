import random

option = input("Enter 1 to exit or other character to play: ")
while option != "1" :
    userChoice = input("Enter \"rock\" or \"paper\" or \"scissors\": ")
    if userChoice != "rock" and userChoice != "paper" and userChoice != "scissors":
        print("You entered an invalid option: ", userChoice)
        continue
    comRand = random.choice(["rock", "paper", "scissors"])
    print("Computer choice: ", comRand)
    if userChoice == comRand:
        print("Tied!")
    elif userChoice == "rock" and comRand == "paper":
        print("You lose!")
    elif userChoice == "paper" and comRand == "scissors":
        print("You win!")
    elif userChoice == "scissors" and comRand == "rock":
        print("You lose!")
    elif userChoice == "scissors" and comRand == "paper":
        print("You win!")
    elif userChoice == "paper" and comRand == "rock":
        print("You win!")
    else: #userChoice == "paper" and comRand == "scissors":
        print("You lose!")
    option = input("Enter 1 to exit or other character to play: ")

print("Thank you for playing!")
