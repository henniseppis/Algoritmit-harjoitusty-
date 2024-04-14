class Opponent():
    def __init__(self, board):
        self.board = board
        self.calculated_moves = {}

    def ai_create_move(self, board, last_move_row, last_move_col, max_depth):
        """Chooses the best move to make in that turn. Returns the coordinates of the best move as tuple"""

        coordinates = self.find_nearest_free_cells(board, last_move_row, last_move_col)
        best_eval = -float('inf')
        best_move = None

        evaluate = self.minmax(board, 0, max_depth, last_move_row, last_move_col, True, -float("inf"), float("inf"))

        print("BEST: ", evaluate)

        return evaluate[1]

    def find_nearest_free_cells(self, board, last_move_row, last_move_col):
        """ This functions finds the nearest free cells which are max 2 cells away in every direction from the last move made
        and adds them to the list """

        smallest_col = last_move_col - 2
        smallest_row = last_move_row - 2

        nearest_cells=[]
        for row in range(smallest_row, smallest_row + 5):
            for col in range(smallest_col, smallest_col + 5):
                if (row < 0 or row >= self.board.board_size or col < 0 or col >= self.board.board_size  or
                          board[row][col] != " "):
                    pass
                else:
                    nearest_cells.append((row,col))
        return nearest_cells
    
    def minmax(self, board, depth, max_depth, last_move_row, last_move_col, maxi, alpha, beta):
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
        
        TODO:: TARKASTELEE KOKO TILANNETTA EIKÄ KESKITY VAIN VIIMEISIMMÄN SIIRRON LÄHEISYYTEEN
        
        """

        if self.board.check_win(board, last_move_row, last_move_col, "X"):
            return -100 + depth, (last_move_row,last_move_col)
        if self.board.check_win(board, last_move_row, last_move_col, "O"):
            return 100 - depth, (last_move_row,last_move_col)
        if self.board.check_draw(board) or depth == max_depth:
            return 0, (last_move_row,last_move_col)

        nearest_cells = self.find_nearest_free_cells(board, last_move_row, last_move_col)
        print(nearest_cells)

        if maxi:
            max_value = -float('inf')
            best=None
            for move in nearest_cells:
                board[move[0]][move[1]] = "O"
                value = self.minmax(board, depth + 1, max_depth, move[0], move[1], False, alpha, beta)[0]
                board[move[0]][move[1]] = " "

                if value > max_value:
                    best=move
                    max_value=value
                alpha = max(alpha, max_value)
                if beta <= alpha:
                    print("PRUNEEED",depth, move, alpha, beta)
                    return max_value, best 
            print("LASTMAX", depth, move, alpha, beta)
            return max_value, best 

        else:
            min_value = float('inf')
            best=None
            for move in nearest_cells:
                board[move[0]][move[1]] = "X"
                value = self.minmax(board, depth + 1, max_depth, move[0], move[1], True, alpha, beta)[0]
                board[move[0]][move[1]] = " "

                if min_value > value:
                    best=move
                    min_value=value
                beta = min(beta, min_value)
                if beta <= alpha:
                    print("PRUNEEED",depth, move, alpha, beta)
                    return min_value, best  
            print("LAST", depth, move, alpha, beta)
            return min_value, best 
     