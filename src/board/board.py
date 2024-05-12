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
    
    
    def heuristic_value(self, board, symbol):
        """ Evaluates the game states. It calls functions to count the score for horizontal, vertical and diagonal"""
        board_size = len(board)
        score = 0  

        for i in range(board_size):
            row = board[i]
            column = [board[j][i] for j in range(board_size)]
            
            check_score_rows = self.check_horizontal(row,symbol)
            score += check_score_rows
            
            check_score_column = self.check_vertical(column, symbol)
            score += check_score_column

        check_score_diagonal = self.check_diagonal(board, symbol)
        score += check_score_diagonal

        return score

    def check_horizontal(self, row, symbol):
        """Used to count game score horizontally. It checks symbols row by row"""
        line_score = 0
        count = 0
        for i in range(len(row)):
            if row[i] == symbol:
                count += 1
            elif row[i] == " " and (i == 0 or row[i - 1] == symbol):
                line_score += count * count
                count = 0
            else:
                count = 0
        line_score += count * count
        return line_score
    
    def check_vertical(self, column, symbol):
        """ Used to count game score vertically. It checks symbols column by column (up to down)"""
        line_score = 0
        count = 0
        for i in range(len(column)):
            if column[i] == symbol:
                count += 1
            elif column[i] == " " and (i == 0 or column[i - 1] == symbol):
                line_score += count * count
                count = 0
            else:
                count = 0
        line_score += count * count
        return line_score
    
    def check_diagonal(self, board, symbol):
        """ Checks score on diagonal sides. The first diagonal's direction is top left to bottom right and the second is top right to bottom left"""
        board_size = len(board)
        diagonal_score = 0
        
        for diag_i in range(-board_size + 1, board_size):
            l_to_r = [board[i][i + diag_i] for i in range(board_size) if 0 <= i + diag_i < board_size]
            r_to_l = [board[i][board_size - 1 - i + diag_i] for i in range(board_size) if 0 <= board_size - 1 - i + diag_i < board_size]

            line_score = 0
            count = 0
            for i in range(len(l_to_r)):
                if l_to_r[i] == symbol:
                    count += 1
                elif l_to_r[i] == " " and (i == 0 or l_to_r[i - 1] == symbol):
                    line_score += count * count
                    count = 0
                else:
                    count = 0
            line_score += count * count
            diagonal_score += line_score

            line_score = 0
            count = 0
            for i in range(len(r_to_l)):
                if r_to_l[i] == symbol:
                    count += 1
                elif r_to_l[i] == " " and (i == 0 or r_to_l[i - 1] == symbol):
                    line_score += count * count
                    count = 0
                else:
                    count = 0
            line_score += count * count
            diagonal_score += line_score
            
        return diagonal_score

 