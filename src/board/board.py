
class Board():
    def __init__(self, size):
        self.board_size = size
        self.board = None

    def create_board(self):
        self.board = [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]
        return self.board

    def next_move(self, symbol, row, column):
            if self.board[row][column] == " ":
                self.board[row][column] = symbol
                return self.board
            