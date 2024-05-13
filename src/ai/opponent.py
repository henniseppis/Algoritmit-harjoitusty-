import copy 

class Opponent():
    def __init__(self, board):
        self.board = board

    def find_nearest_free_cells(self, board, row, col):
        """ This functions finds the nearest free cells which are max 2 cells away in every direction from the last move made
        and adds them to the list. It stars with the closest ones of the last move. """

        smallest_col = col - 2
        smallest_row = row - 2
        

        nearest_cells = []
        for row in range(smallest_row, smallest_row + 4):
            for col in range(smallest_col, smallest_col + 4):
                if (row < 0 or row >= 20 or col < 0 or col >= 20 or board[row][col] != " "):
                    pass
                else:
                    nearest_cells.append((row, col))

        smallest_col += 1
        smallest_row += 1

        for row in range(smallest_row, smallest_row + 2):
            for col in range(smallest_col, smallest_col + 2):
                if (row < 0 or row >= 20 or col < 0 or col >= 20 or board[row][col] != " "):
                    pass
                else:
                    if (row, col) not in nearest_cells:
                        nearest_cells.append((row, col))
        return nearest_cells

    def minmax(self, board, depth, max_depth, last_row, last_col, maxi, alpha, beta, cells_to_investigate):
        """ The function counts the best possible move for AI.

        If maximizing so if we are looking for the best possible move we can create, 
        we imaginarely import move to the board and check what would happen 
        if we proceed with that move. It recursively calls itself to check which cell from list would be the best move. 
        If minimazing it checks which moves AI could make so the human player had less chances to win.
        
        We use alpha beta pruning to improve algorithm's efficiency at it cuts off moves which can be proved to be worse than already checked.

        """
                 
        if self.board.check_win(board, last_row, last_col):
            if maxi:
                return (float("-inf"), last_row, last_col)
            return (float("inf"), last_row, last_col)

        if self.board.check_draw(board):
            return 0, None, None
        
        if depth == max_depth:
            if maxi:
                heuristic_value = self.board.heuristic_value(board, "O")
                return (heuristic_value, None, None)
            else:
                heuristic_value = self.board.heuristic_value(board, "X")
                return (-heuristic_value, None, None)
                
                        
        if maxi:
            max_value = float("-inf")
            best = None
            for i in range(len(cells_to_investigate)-1,-1,-1):
                row, col = cells_to_investigate[i]
                if board[row][col] == " ":
                    board[row][col] = "O"
                    cells_to_investigate_copy = copy.copy(cells_to_investigate)
                    nearest_cells = self.find_nearest_free_cells(board, row, col)
                    for move in nearest_cells:
                        if move in cells_to_investigate_copy:
                            cells_to_investigate_copy.remove(move)
                        cells_to_investigate_copy.append(move)
                    value, _, _ = self.minmax(board, depth + 1, max_depth, row, col, False, alpha, beta, cells_to_investigate_copy)
                    board[row][col] = " "
                    if value > max_value:
                        best = (row,col)
                        max_value = value
                        alpha = value
                    if beta <= alpha:
                        break
            
            if best is None:
                return (max_value, last_row, last_col)
            return (max_value, best[0], best[1])

        else:
            min_value = float("inf")
            best = None
            for i in range(len(cells_to_investigate)-1,-1,-1):
                row, col = cells_to_investigate[i]
                if board[row][col] == " ":
                    board[row][col] = "X"
                    cells_to_investigate_copy = copy.copy(cells_to_investigate)
                    nearest_cells = self.find_nearest_free_cells(board, row, col)
                    for move in nearest_cells:
                        if move in cells_to_investigate_copy:
                            cells_to_investigate_copy.remove(move)
                        cells_to_investigate_copy.append(move)
                    value, _, _ = self.minmax(board, depth + 1, max_depth, row, col, True, alpha, beta, cells_to_investigate_copy)
                    board[row][col] = " "
                    if value < min_value:
                        best = (row,col)
                        min_value = value
                        beta = value
                    if beta <= alpha:
                        break
            
            if best is None:
                return (min_value, last_row, last_col)
            return (min_value, best[0], best[1])
