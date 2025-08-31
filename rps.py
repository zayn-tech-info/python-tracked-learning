import sys
from enum import Enum
import random
 
game_count = 0
def play_rps(): 
    class RPS(Enum):
        rock = 1
        paper = 2
        scissors = 3

    print("\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissors")
    playerChoice = int(input("\nEnter a number to start playing: \n"))
    if playerChoice not in [1, 2, 3] :
        print("Please enter a number between 1 to 3")
        play_rps()

    computerChoice = random.choice([1, 2, 3])
    print("You chose " + RPS(playerChoice).name + ".")
    print("Computer chose " + RPS(computerChoice).name + ".")

    def handle_winner(player, computer): 
        if  player == 1 and computer == 2:
            return "\nYahh, you won!"
        elif  player == 3 and computer == 2:
            return "\nYahh, You won"
        elif  player == 1 and computer == 3:
            return "\nyahh, You won"
        elif  player ==  computer:
            return "\nTie game, Try again"
        else:
            return "\nComputer wins!"
    
    game_result = handle_winner(playerChoice, computerChoice)
    print(game_result)
    global game_count
    game_count += 1
    print("\nGame result: " + str(game_count))

    print("\nPlay again?")
    while True:
        playagain = input('\nEnter "Y" to play again\n"Q" to quit\n\n')
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
       return play_rps()
    else:
        print("Thank you for playing")
        sys.exit("Bye !")
play_rps()