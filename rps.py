import sys
from enum import Enum
import random

def play_rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    class RPS(Enum):
        rock = 1
        paper = 2
        scissors = 3

    while True:
        try:
            print("\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissors")
            playerChoice = int(input("\nEnter a number to start playing: \n"))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if playerChoice not in [1, 2, 3]:
            print("Please enter a number between 1 to 3")
            continue

        computerChoice = random.choice([1, 2, 3])
        print(f"You chose {RPS(playerChoice).name}.")
        print(f"Computer chose {RPS(computerChoice).name}.")

        def handle_winner(player, computer):
            nonlocal player_wins, computer_wins
            if player == computer:
                return "\nTie game, Try again"
            if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
                player_wins += 1
                return "\nYahh, you won!"
            else:
                computer_wins += 1
                return "\nComputer wins!"

        game_result = handle_winner(playerChoice, computerChoice)
        print(game_result)

        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"Player wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")

        playagain = input('\nEnter "Y" to play again or "Q" to quit: \n')
        if playagain.lower() == "y":
            continue
        elif playagain.lower() == "q":
            print("Thank you for playing")
            sys.exit("Bye !")
        else:
            print("Invalid input. Exiting.")
            sys.exit("Bye !")


if __name__ == "__main__":
    play_rps()