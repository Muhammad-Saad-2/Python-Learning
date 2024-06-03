import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.window, text="", font=("Helvetica", 16), width=6, height=2,
                                   command=lambda r=i, c=j: self.on_button_click(r, c))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.game_mode_var = tk.StringVar()
        self.game_mode_var.set("2 Players")
        mode_menu = tk.OptionMenu(self.window, self.game_mode_var, "2 Players", "vs Computer")
        mode_menu.grid(row=3, column=0, columnspan=3, pady=10)

    def on_button_click(self, row, col):
        if self.game_mode_var.get() == "2 Players":
            self.play_2_players(row, col)
        else:
            self.play_vs_computer(row, col)

    def play_2_players(self, row, col):
        if self.board[row * 3 + col] == "" and not self.check_winner():
            self.board[row * 3 + col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def play_vs_computer(self, row, col):
        if self.board[row * 3 + col] == "" and not self.check_winner():
            self.board[row * 3 + col] = "X"
            self.buttons[row][col].config(text="X")

            if self.check_winner():
                messagebox.showinfo("Game Over", "You win!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.make_computer_move()

    def make_computer_move(self):
        available_moves = [i for i, value in enumerate(self.board) if value == ""]
        if available_moves:
            computer_move = random.choice(available_moves)
            row, col = divmod(computer_move, 3)
            self.board[computer_move] = "O"
            self.buttons[row][col].config(text="O")

            if self.check_winner():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_board()

    def check_winner(self):
        for i in range(3):
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != "":
                return True
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return True

        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True

        return False

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i * 3 + j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
