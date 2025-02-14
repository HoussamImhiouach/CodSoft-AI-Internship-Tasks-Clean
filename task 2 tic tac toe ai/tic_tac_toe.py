import tkinter as tk
from tkinter import messagebox
import math

# Tic-Tac-Toe Board Initialization
board = [["" for _ in range(3)] for _ in range(3)]
player = "X"
ai = "O"

# Function to check if the board has a winner
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    return None

# Function to check if the board is full (draw)
def is_full():
    return all(board[row][col] != "" for row in range(3) for col in range(3))

# Minimax Algorithm (AI's Decision Making)
def minimax(board, depth, is_maximizing):
    winner = check_winner()
    if winner == ai:
        return 1
    elif winner == player:
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = ai
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ""
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = player
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ""
                    best_score = min(best_score, score)
        return best_score

# Function to find the AI's best move
def best_move():
    best_score = -math.inf
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = ai
                score = minimax(board, 0, False)
                board[row][col] = ""
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

# Function to handle button clicks (Player's Turn)
def on_click(row, col):
    if board[row][col] == "" and check_winner() is None:
        board[row][col] = player
        buttons[row][col].config(text=player, state="disabled")
        
        # Check for draw **before** checking for a winner
        if is_full():
            if check_winner() is None:  # Ensure no winner before declaring a draw
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_board()
                return
        
        # Check for a winner
        if check_winner():
            messagebox.showinfo("Game Over", f"{player} wins!")
            reset_board()
            return
        
        # AI's Turn
        ai_move = best_move()
        if ai_move:
            board[ai_move[0]][ai_move[1]] = ai
            buttons[ai_move[0]][ai_move[1]].config(text=ai, state="disabled")

            # Check for draw again after AI's move
            if is_full():
                if check_winner() is None:
                    messagebox.showinfo("Game Over", "It's a draw!")
                    reset_board()
                    return

            # Check if AI won
            if check_winner():
                messagebox.showinfo("Game Over", f"{ai} wins!")
                reset_board()
                return

    if board[row][col] == "" and check_winner() is None:
        board[row][col] = player
        buttons[row][col].config(text=player, state="disabled")
        
        if check_winner():
            messagebox.showinfo("Game Over", f"{player} wins!")
            reset_board()
            return
        
        if is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
            return
        
        # AI's Turn
        ai_move = best_move()
        if ai_move:
            board[ai_move[0]][ai_move[1]] = ai
            buttons[ai_move[0]][ai_move[1]].config(text=ai, state="disabled")

            if check_winner():
                messagebox.showinfo("Game Over", f"{ai} wins!")
                reset_board()
                return
            
            if is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_board()
                return

# Function to reset the board
def reset_board():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state="normal")

# Creating GUI
root = tk.Tk()
root.title("Tic-Tac-Toe AI")

buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                                      command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_board)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
