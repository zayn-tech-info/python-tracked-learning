import sys
from enum import Enum
import random

class RPS(Enum):
    rock = 1
    paper = 2
    scissors = 3

playagain = True

while playagain:
    print("1 is Rock")
    print("2 is Paper")
    print("3 is sicssors")
    userChoice = int(input("Enter a number to start playing: "))

    computerChoice = int(random.choice("123"))

    print("You chose " + RPS(userChoice).name + ".")
    print("Computer chose " + RPS(computerChoice).name + ".")

    if userChoice > 3 or userChoice < 1:
        print("Please enter a number between 1 to 3")
        sys.exit()

    if userChoice == 1 and computerChoice == 2:
        print("Yahh, you won!")
    elif userChoice == 3 and computerChoice == 2:
        print("Yahh, You won")
    elif userChoice == 1 and computerChoice == 3:
        print("yahh, You won")
    elif userChoice ==  computerChoice:
        print("Tie game, Try again")
    else:
        print("Computer wins!")
    
    playagain = input('Enter "Y" to play again\n"Q" to quit\n\n')

    if playagain .lower() == "y":
        continue
    else:
        break
        print("Thank you for playing")
        playagain  == False
sys.exit("Bye !")