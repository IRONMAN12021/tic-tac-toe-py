import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.current_player = 'X'
        self.board = ['' for _ in range(9)]
        self.buttons = []
        self.create_widgets()
        self.start_new_game()

    def create_widgets(self):
        # Create a 3x3 grid of buttons
        for i in range(9):
            button = tk.Button(self.root, text='', font=('Arial', 24), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # Create a label to display messages
        self.message_label = tk.Label(self.root, text="Player X's turn", font=('Arial', 16))
        self.message_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Create a restart button
        self.restart_button = tk.Button(self.root, text="Restart Game", font=('Arial', 16), command=self.start_new_game)
        self.restart_button.grid(row=4, column=0, columnspan=3)

    def on_button_click(self, index):
        if self.board[index] == '' and not self.check_winner() and not self.check_draw():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.message_label.config(text=f"Player {self.current_player} wins!")
                self.show_message(f"Player {self.current_player} wins!")
            elif self.check_draw():
                self.message_label.config(text="It's a draw!")
                self.show_message("It's a draw!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.message_label.config(text=f"Player {self.current_player}'s turn")
                if self.current_player == 'O':
                    self.ai_move()

    def ai_move(self):
        available_moves = [i for i, mark in enumerate(self.board) if mark == '']
        if available_moves:
            move = random.choice(available_moves)
            self.board[move] = 'O'
            self.buttons[move].config(text='O')
            if self.check_winner():
                self.message_label.config(text="AI wins!")
                self.show_message("AI wins!")
            elif self.check_draw():
                self.message_label.config(text="It's a draw!")
            else:
                self.current_player = 'X'
                self.message_label.config(text="Player X's turn")

    def check_winner(self):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]               # Diagonal
        ]
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] and self.board[pattern[0]] != '':
                return True
        return False

    def check_draw(self):
        return '' not in self.board

    def show_message(self, message):
        messagebox.showinfo("Game Over", message)

    def start_new_game(self):
        self.current_player = 'X'
        self.board = ['' for _ in range(9)]
        for button in self.buttons:
            button.config(text='')
        self.message_label.config(text="Player X's turn")

# Create the application window
root = tk.Tk()
app = TicTacToeApp(root)
root.mainloop()
