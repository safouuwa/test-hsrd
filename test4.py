import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()

        self.current_player = 'X'
        self.game_over = False
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.label = tk.Label(self, text="Player {}'s turn".format(self.current_player))
        self.label.pack()

        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack()

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.grid_frame, text=" ", width=10, height=5, command=lambda i=i, j=j: self.button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def button_click(self, i, j):
        if self.game_over:
            return

        button = self.buttons[i][j]
        if button["text"] == " ":
            button["text"] = self.current_player
            if self.check_for_win():
                self.label["text"] = "{} wins!".format(self.current_player)
                self.game_over = True
            elif self.check_for_draw():
                self.label["text"] = "It's a draw!"
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.label["text"] = "Player {}'s turn".format(self.current_player)

    def check_for_win(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != " ":
                return True
        for i in range(3):
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != " ":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != " ":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != " ":
            return True
        return False

    def check_for_draw(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == " ":
                    return False
        return True

if __name__ == "__main__":
    app = TicTacToe()
    app.title("Tic Tac Toe")
    app.geometry("300x300")
    app.mainloop()
