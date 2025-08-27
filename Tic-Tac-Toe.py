import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Make window resizable for responsiveness
root.geometry("400x400")
root.minsize(300, 300)

# Current player
current_player = "X"

# Create board
board = [""] * 9

# Check winner function
def check_winner():
    win_combinations = [
        [0,1,2],[3,4,5],[6,7,8], # rows
        [0,3,6],[1,4,7],[2,5,8], # columns
        [0,4,8],[2,4,6]          # diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]
    if "" not in board:
        return "Draw"
    return None

# Button click handler
def button_click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

# Reset board
def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="")

# Create buttons
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=('Arial', 24), command=lambda i=i: button_click(i))
    buttons.append(btn)

# Use grid with sticky to expand buttons
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

for i in range(9):
    buttons[i].grid(row=i//3, column=i%3, sticky="nsew")

# Reset button
reset_btn = tk.Button(root, text="Reset", font=('Arial', 18), bg="lightblue", command=reset_board)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")
root.grid_rowconfigure(3, weight=0)

# Run app
root.mainloop()