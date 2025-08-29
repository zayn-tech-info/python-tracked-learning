import sys
from enum import Enum
import random
class RPS(Enum):
    rock = 1
    paper = 2
    scissors = 3

playagain = True

while playagain:
    print("\nEnter...")
    print("1 for Rock\n2 for Paper\n3 for Scissors")
    userChoice = int(input("\nEnter a number to start playing: \n"))

    computerChoice = random.choice([1, 2, 3])
    print("You chose " + RPS(userChoice).name + ".")
    print("Computer chose " + RPS(computerChoice).name + ".")

    if userChoice > 3 or userChoice < 1:
        print("Please enter a number between 1 to 3")
        sys.exit()

    if userChoice == 1 and computerChoice == 2:
        print("\nYahh, you won!")
    elif userChoice == 3 and computerChoice == 2:
        print("\nYahh, You won")
    elif userChoice == 1 and computerChoice == 3:
        print("\nyahh, You won")
    elif userChoice ==  computerChoice:
        print("\nTie game, Try again")
    else:
        print("\nComputer wins!")
    
    playagain = input('Enter "Y" to play again\n"Q" to quit\n\n')

    if playagain.lower() == "y":
        continue
    else:
        print("Thank you for playing")
        break
sys.exit("Bye !")