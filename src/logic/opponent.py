import copy 

class Opponent():
    def __init__(self, board):
        self.board = board

    def find_nearest_free_cells(self, board, row, col):
        """ This functions finds the ne marest free cells which are max 2 cells away in every direction from the last move made
        and adds them to the list """

        smallest_col = col - 1
        smallest_row = row - 1

        nearest_cells = []
        for r in range(smallest_row, smallest_row + 3):
            for c in range(smallest_col, smallest_col + 4):
                if (r < 0 or r >= 20 or c < 0 or c >= 20 or board[r][c] != " "):
                    pass
                else:
                    nearest_cells.append((r, c))

        smallest_col -= 1
        smallest_row -= 1

        for r in range(smallest_row, smallest_row + 4):
            for c in range(smallest_col, smallest_col + 4):
                if (r < 0 or r >= 20 or c < 0 or c >= 20 or board[r][c] != " "):
                    pass
                else:
                    if (r, c) not in nearest_cells:
                        nearest_cells.append((r, c))

        return nearest_cells

    def minmax(self, board, depth, max_depth, last_row, last_col, maxi, alpha, beta, cells_to_investigate):
        """ First it checks possible win or draw. If human player has won it returns -1, 
        if AI has won it returns 1 or if all the cells are full 
        and there is no win it returns 0 or if the maximum depth
        (how far we check the moves forward) has exceeded)

        It goes through the nearest_cells list which includes all 
        the cells which are 2 cells away from the previous move. 

        If maximizing so if we are looking for the best possible move we can create, 
        we imaginarely import move to the board and check what would happen 
        if we proceed with that move. It recursively calls itself to check which cell from list would be the best move. 
        If minimazing it checks which moves AI could make so the human player had less chances to win.

        """
                 
        if self.board.check_win(board, last_row, last_col):
            if maxi:
                return -100000 + depth, last_row, last_col
            return 100000 - depth, last_row, last_col

        if self.board.check_draw(board):
            return 0, None, None
        
        if depth == max_depth:
            return self.board.heuristic_value(board), None, None
                
        if maxi:
            max_value = -1000000
            best = None
            for i in range(len(cells_to_investigate)-1,-1,-1):
                row, col = cells_to_investigate[i]
                cells_to_investigate_copy = copy.copy(cells_to_investigate)
                nearest_cells = self.find_nearest_free_cells(board, row, col)
                for move in nearest_cells:
                    if board[move[0]][move[1]] == " ":
                        if move in cells_to_investigate_copy:
                            cells_to_investigate_copy.remove(move)
                        cells_to_investigate_copy.append(move)
                board[row][col] = "O"
                value = self.minmax(board, depth + 1, max_depth,row,col, False, alpha, beta, cells_to_investigate_copy)[0]
                board[row][col] = " "
                if value > max_value:
                    best = (row,col)
                    max_value = value
                    alpha = value
                if beta <= alpha:
                    break
                
            return max_value, best[0], best[1]

        else:
            min_value = 1000000
            best = None
            for i in range(len(cells_to_investigate)-1,-1,-1):
                row, col = cells_to_investigate[i]
                cells_to_investigate_copy = copy.copy(cells_to_investigate)
                nearest_cells = self.find_nearest_free_cells(board, row, col)
                for move in nearest_cells:
                    if board[move[0]][move[1]] == " ":
                        if move in cells_to_investigate_copy:
                            cells_to_investigate_copy.remove(move)
                        cells_to_investigate_copy.append(move)
                board[row][col] = "X"
                value = self.minmax(board, depth + 1, max_depth, row, col, True, alpha, beta, cells_to_investigate_copy)[0]
                board[row][col] = " "
                if value < min_value:
                    best = (row,col)
                    min_value = value
                    beta = value
                if beta <= alpha:
                    break
            return min_value, best[0], best[1]
