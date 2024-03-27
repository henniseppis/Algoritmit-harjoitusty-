
class Board():
    def __init__(self, size):
        self.board_size = size
        self.board = None

    def create_board(self):
        """Creates the frame of the board of wanted size"""
        self.board = [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]
        return self.board

    def next_move(self, symbol, row, column):
        """Inserts the wanted move to the table"""
        if self.board[row][column] == " ":
            self.board[row][column] = symbol
            return self.board
            