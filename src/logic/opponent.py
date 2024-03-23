import random
import string

class Opponent():
    def create_move(self):
        row = random.randint(1,20)
        column = random.choice('abcdefghijklmnopqrst')
        column = string.ascii_uppercase.index(column.upper())
        return row, column