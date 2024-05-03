class Board:
    def next_move(self, board, symbol, row, column):
        """Inserts the wanted move to the table"""
        board[row][column] = symbol
        return board

    def check_draw(self, board):
        """ Checks if none of the cells are free if yes game ends with draw """
        return all(cell != ' ' for row in board for cell in row)

    def check_win(self, board, last_move_row, last_move_col):
        """ Checks if there are win (vertically, horizontally and diagonally)"""

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        board_size = len(board)
        symbol = board[last_move_row][last_move_col]

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


    def heuristic_value(self, board):
        return 0
