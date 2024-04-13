
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
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        board_size = len(board)

        for dir_row, dir_col in directions:
            count = 1

            for n in range(1, 5):
                check_row = last_move_row + dir_row * n
                check_col = last_move_col + dir_col * n
                if (0 <= check_row < board_size and 0 <= check_col < board_size and
                        board[check_row][check_col] == symbol):
                    count += 1
                else:
                    break  

            for n in range(1, 5):
                check_row = last_move_row - dir_row * n
                check_col = last_move_col - dir_col * n
                if (0 <= check_row < board_size and 0 <= check_col < board_size and
                        board[check_row][check_col] == symbol):
                    count += 1
                else:
                    break

            if count >= 5:
                return True

        return False

        


        
        