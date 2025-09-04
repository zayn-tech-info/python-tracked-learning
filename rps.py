import sys
from enum import Enum
import random

def play_rps(playername="PlayerX"):
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
            playerChoice = int(input(f"\n{playername}, Enter a number to start playing: \n"))
        except ValueError:
            print(f"{playername}, Please enter a valid number.")
            continue

        if playerChoice not in [1, 2, 3]:
            print(f"{playername}, Please enter a number between 1 to 3")
            continue

        computerChoice = random.choice([1, 2, 3])
        print(f"{playername} you chose {RPS(playerChoice).name}.")
        print(f"Computer chose {RPS(computerChoice).name}.")

        def handle_winner(player, computer):
            nonlocal player_wins, computer_wins
            if player == computer:
                return "\nTie game, Try again"
            if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
                player_wins += 1
                return f"\nYahh, {playername} you won!"
            else:
                computer_wins += 1
                return "\nComputer wins!"

        game_result = handle_winner(playerChoice, computerChoice)
        print(game_result)

        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"{playername} wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")

        playagain = input('\nEnter "Y" to play again or "Q" to quit: \n')
        if playagain.lower() == "y":
            continue
        elif playagain.lower() == "q":
            print(f"Thank you for playing {playername}")
            sys.exit(f"Bye {playername}!")
        else:
            print("Invalid input. Exiting.")
            sys.exit(f"Bye {playername}!")
    return play_rps()

if __name__ == "__main__":
    import argparse

    parser =  argparse.ArgumentParser(
        description= "Provide a player name for the game."
    )
    parser.add_argument(
        "-pn", "--playername", metavar="Playername",
        help="Provide a name for player", required= True
    )
    args = parser.parse_args()
    play_rps(args.playername)
