import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x600")
        self.root.configure(bg="#1e1e2f")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.scores = {"Player": 0, "AI": 0}
        self.game_mode = "Single Player"  # Default mode

        self.main_menu()

    # ---------------- Main Menu ---------------- #
    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title
        title_label = tk.Label(self.root, text="Tic Tac Toe", font=("Helvetica", 36, "bold"),
                               bg="#1e1e2f", fg="#f3f3f3")
        title_label.pack(pady=30)

        # Single Player Button
        single_button = tk.Button(self.root, text="Single Player", font=("Helvetica", 18),
                                  bg="#4caf50", fg="#ffffff", command=lambda: self.start_game("Single Player"))
        single_button.pack(pady=20, ipadx=30, ipady=10)

        # Two Player Button
        two_player_button = tk.Button(self.root, text="Two Players", font=("Helvetica", 18),
                                       bg="#4caf50", fg="#ffffff", command=lambda: self.start_game("Two Players"))
        two_player_button.pack(pady=20, ipadx=30, ipady=10)

        # Quit Button
        quit_button = tk.Button(self.root, text="Quit", font=("Helvetica", 18),
                                 bg="#ff5722", fg="#ffffff", command=self.root.quit)
        quit_button.pack(pady=20, ipadx=30, ipady=10)

    # ---------------- Game Setup ---------------- #
    def start_game(self, mode):
        self.game_mode = mode
        self.board = [""] * 9
        self.current_player = "X"
        self.create_game_board()

    def create_game_board(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Score Label
        self.score_label = tk.Label(self.root, text=f"Player: {self.scores['Player']}   AI: {self.scores['AI']}",
                                    font=("Helvetica", 16), bg="#1e1e2f", fg="#f3f3f3")
        self.score_label.pack(pady=10)

        # Turn Label
        self.turn_label = tk.Label(self.root, text=f"Player {self.current_player}'s Turn", font=("Helvetica", 18),
                                   bg="#1e1e2f", fg="#f3f3f3")
        self.turn_label.pack(pady=10)

        # Game Board
        self.board_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.board_frame.pack()

        self.buttons = []
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.board_frame, text="", font=("Helvetica", 20, "bold"), height=2, width=5,
                                bg="#28293e", fg="#ffffff", activebackground="#4caf50",
                                command=lambda index=i * 3 + j: self.on_click(index))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(btn)

        # Back to Menu Button
        back_button = tk.Button(self.root, text="Back to Menu", font=("Helvetica", 14),
                                bg="#ff5722", fg="#ffffff", command=self.main_menu)
        back_button.pack(pady=10)

    # ---------------- Button Click Logic ---------------- #
    def on_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                self.update_score(f"{self.current_player}")
                self.end_game(f"Player {self.current_player} wins!")
            elif "" not in self.board:
                self.end_game("It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Player {self.current_player}'s Turn")

                if self.game_mode == "Single Player" and self.current_player == "O":
                    self.ai_turn()

    def ai_turn(self):
        best_move = self.get_best_move()
        self.board[best_move] = "O"
        self.buttons[best_move].config(text="O")

        if self.check_winner():
            self.update_score("AI")
            self.end_game("AI wins!")
        elif "" not in self.board:
            self.end_game("It's a draw!")
        else:
            self.current_player = "X"
            self.turn_label.config(text=f"Player {self.current_player}'s Turn")

    # ---------------- AI Logic (Minimax) ---------------- #
    def get_best_move(self):
        def minimax(board, is_maximizing):
            winner = self.check_winner_for_ai(board)
            if winner == "X":
                return -1
            elif winner == "O":
                return 1
            elif "" not in board:
                return 0

            if is_maximizing:
                best_score = -float("inf")
                for i in range(9):
                    if board[i] == "":
                        board[i] = "O"
                        score = minimax(board, False)
                        board[i] = ""
                        best_score = max(score, best_score)
                return best_score
            else:
                best_score = float("inf")
                for i in range(9):
                    if board[i] == "":
                        board[i] = "X"
                        score = minimax(board, True)
                        board[i] = ""
                        best_score = min(score, best_score)
                return best_score

        best_score = -float("inf")
        move = 0
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = minimax(self.board, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    move = i
        return move

    # ---------------- Helper Functions ---------------- #
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def check_winner_for_ai(self, board):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in winning_combinations:
            if board[a] == board[b] == board[c] != "":
                return board[a]
        return None

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.start_game(self.game_mode)

    def update_score(self, winner):
        if winner == "Player":
            self.scores["Player"] += 1
        elif winner == "AI":
            self.scores["AI"] += 1

# ---------------- Main Program ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
