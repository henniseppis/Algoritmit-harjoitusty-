import random
import string

class Opponent():
    def create_move(self, board):
        while True:
            row = random.randint(0,19)
            column = random.choice('abcdefghijklmnopqrst')
            column = string.ascii_uppercase.index(column.upper())
            if board[row][column] == " ":
                return row, column
            else:
                continue


     