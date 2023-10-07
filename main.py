# import tkinter as tk
#
# class DictionaryApp:
#     def __init__(self, master):
#         self.master = master
#         self.dict = {}
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.key_entry = tk.Entry(self.master)
#         self.key_entry.pack()
#
#         self.value_entry = tk.Entry(self.master)
#         self.value_entry.pack()
#
#         self.add_button = tk.Button(self.master, text="Add", command=self.add_to_dict)
#         self.add_button.pack()
#
#         self.show_button = tk.Button(self.master, text="Show", command=self.show_dict)
#         self.show_button.pack()
#
#     def add_to_dict(self):
#         key = self.key_entry.get()
#         value = self.value_entry.get()
#         self.dict[key] = value
#
#     def show_dict(self):
#         result = ""
#         for key, value in self.dict.items():
#             result += f"{key}: {value}\n"
#         tk.messagebox.showinfo("Dictionary", result)
#
# root = tk.Tk()
# app = DictionaryApp(root)
# root.mainloop()



import random
import time

# Define the game board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Define the possible winning combinations
winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

# Define the players
players = ['X', 'O']

# Get the current player
current_player = random.choice(players)

# Start the game loop
while True:

    # Display the game board
    print_board(board)

    # Get the player's move
    move = get_move(current_player, board)

    # Update the game board
    board[move[0]][move[1]] = current_player

    # Check if the current player has won
    if has_won(current_player, board):
        print(f"{current_player} has won!")
        break

    # Check if the game is a draw
    if is_draw(board):
        print("The game is a draw!")
        break

    # Switch to the next player
    current_player = get_next_player(current_player)

# Define the function to print the game board
def print_board(board):
    for row in board:
        print(' | '.join(row))

# Define the function to get the player's move
def get_move(player, board):
    while True:
        move = input("Enter your move (1-9): ")
        move = int(move) - 1
        if 0 <= move < 9 and board[move][0] == ' ':
            break
    return [move // 3, move % 3]

# Define the function to check if the current player has won
def has_won(player, board):
    for winning_combination in winning_combinations:
        if all(board[i][j] == player for i, j in winning_combination):
            return True
    return False

# Define the
