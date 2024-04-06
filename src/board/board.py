
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
        self.board[row][column] = symbol
        return self.board

    def check_draw(self, board):
        """ Checks if none of the cells are free if yes game ends with draw """
        return all(cell != ' ' for row in board for cell in row)

    def check_win(self, board, last_move_row, last_move_col, symbol):
        """ 
        We use directions multiplied from 1 to 5 (5 because you need 5 same symbols following each other to win) to investigate if the last move has created a winning line. 
        It checks every direction (horizontally, vertically and diagonally) for possible win. 

        Parameters:
        board = board including all the previous moves
        last_move_row = row coordinate of the last move
        last_move_col = column coordinate of the last move
        symbol = X or O depending who had the previous turn. If the win is detected the one who plays with this symbol is announced to be the winner.

        Returns:
        either True if win or False if no win        
        """
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dir_row, dir_col in directions:
            count = 1
            for n in range(1, 5):
                check_row_plus = last_move_row + dir_row * n
                check_col_plus = last_move_col + dir_col * n

                check_row_minus = last_move_row - dir_row * n
                check_col_minus =  last_move_col - dir_col * n

                if (check_row_plus< 0 or check_row_plus >= self.board_size or check_col_plus < 0 or check_col_plus >= self.board_size  or
                          board[check_row_plus][check_col_plus] != symbol):
                    pass
                else:
                    count += 1

                if (check_row_minus < 0 or check_row_minus >= self.board_size or check_col_minus < 0 or check_col_minus >= self.board_size  or
                          board[check_row_minus][check_col_minus] != symbol):
                    pass
                else:
                    count += 1
            if count == 5:
                return True

        return False
    


        
        