# Tic-Tac-Toe AI

## Overview

This project is a **Tic-Tac-Toe game** where the user plays as **"X"** and the AI plays as **"O"**. The AI is **unbeatable** because it uses the **Minimax algorithm** to make optimal moves.

## How It Works

1. **Minimax Algorithm**
   - AI evaluates all possible moves and picks the best one.
   - If AI is maximizing, it picks the move with the highest score.
   - If the player is minimizing, they pick the lowest score.
2. **Game Conditions**
   - The game detects wins, losses, and draws.
   - If the board is full and no one wins, it declares a **draw**.
3. **GUI Interface**
   - Users click on cells to make a move.
   - AI moves automatically after the player.

## Technologies Used

- **Python**
- **Tkinter (GUI)**
- **Minimax Algorithm** (AI Decision-Making)
- **Game Logic (Win/Loss Conditions)**

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/AI-Internship-Tasks.git
   cd AI-Internship-Tasks/tic-tac-toe-ai
   ```
2. **Run the script:**
   ```bash
   python tic_tac_toe.py
   ```

## Usage Guide

1. Click on an empty cell to place `"X"`.
2. AI automatically places `"O"` using Minimax.
3. The game detects wins, losses, and draws.
4. Click **"Reset Game"** to play again.

## Expected Output

- AI always **makes the best moves**.
- **Game declares a winner, a draw, or continues playing.**

## Future Improvements

- Add **difficulty levels** (Easy, Medium, Hard).
- Improve the **GUI design**.
- Implement **multiplayer mode**.

## License

This project is open-source and available under the MIT License.
