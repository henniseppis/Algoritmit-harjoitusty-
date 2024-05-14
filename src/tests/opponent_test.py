import unittest
from ai.opponent import Opponent
from UI.ui import UI


class TestOpponent(unittest.TestCase):
    def setUp(self):
        self.ui = UI()
        self.test_board = self.ui.create_board()
        self.opponent = Opponent(self.test_board)
       
    
    def test_find_nearest_cells(self):
        self.test_board[5][7] = "X"
        cells = self.opponent.find_nearest_free_cells(self.test_board, 5, 7)
        self.assertEqual(cells, [(3, 5), (3, 6),(3, 7),(3, 8),(4, 5),(4, 6),(4, 7),(4, 8),(5, 5),(5, 6),(5, 8),(6, 5),(6, 6),(6, 7),(6, 8)])        
    
    
    def test_find_nearest_free_cells_wont_add_occupied_cells_to_list(self):
        self.test_board[5][7] = "X"
        cells = self.opponent.find_nearest_free_cells(self.test_board, 5, 7)
        self.assertEqual(cells, [(3, 5), (3, 6),(3, 7),(3, 8),(4, 5),(4, 6),(4, 7),(4, 8),(5, 5),(5, 6),(5, 8),(6, 5),(6, 6),(6, 7),(6, 8)])
        self.test_board[6][7] = "X"
        cells = self.opponent.find_nearest_free_cells(self.test_board, 6, 7)
        self.assertEqual(cells, [(4, 5),(4, 6),(4, 7),(4, 8),(5, 5),(5, 6),(5, 8),(6, 5),(6, 6),(6, 8), (7, 5),(7, 6),(7, 7),(7, 8)])
   
    
    def test_ai_block_human_player_4_same_vertical(self):
        board = self.ui.create_board()
        board[7][4] = "X"
        board[8][4] = "X"
        board[9][4] = "X"
        board[10][4] = "X"
        board[11][4] = "O"
        _, row, col = self.opponent.minmax(board, 0, 3, 7 ,4, True, float("-inf"), float("inf"), [(6, 2), (5, 3), (5, 2), (10, 3), (9, 3), (11, 5), (6, 5), (7, 5), (12, 5), (8, 2), (10, 5), (6, 4), (5, 5), (12, 2), (11, 2), (11, 3), (7, 3), (9, 2), (10, 2), (12, 4), (8, 5), (5, 4), (9, 5), (6, 3)])
        self.assertEqual((row,col), (6,4))
    
    def test_ai_block_human_player_4_same_horizontal(self):
        board = self.ui.create_board()
        board[7][4] = "X"
        board[7][5] = "X"
        board[7][6] = "X"
        board[7][7] = "X"
        board[7][8] = "O"
        _, row, col = self.opponent.minmax(board, 0, 3, 7 ,4, True, float("-inf"), float("inf"), [(5, 2), (5, 3), (5, 4), (5, 5), (6, 2), (6, 3), (6, 4), (6, 5), (7, 2), (7, 3), (8, 2), (8, 3), (8, 4), (8, 5), (5, 6), (6, 6), (8, 6), (5, 7), (6, 7),(8, 7),(5, 8), (6, 8), (8, 8),(5, 9), (6, 9), (7, 9),(8, 9)])
        self.assertEqual((row,col), (7,3))
    
    
    def test_ai_block_human_player_4_same_diagonal(self):
        board = self.ui.create_board()
        board[7][4] = "X"
        board[8][5] = "X"
        board[9][6] = "X"
        board[10][7] = "X"
        board[11][8] = "O"
        _, row, col = self.opponent.minmax(board, 0, 3, 7 ,4, True, float("-inf"), float("inf"), [(5, 2), (5, 3), (5, 4), (5, 5), (6, 2), (6, 3), (6, 4), (6, 5), (7, 2), (7, 3), (7, 5), (8, 2), (8, 3), (8, 4),(6, 6), (7, 6), (8, 6), (9, 3), (9, 4), (9, 5),(7, 7), (8, 7), (9, 7), (10, 4), (10, 5), (10, 6), (8, 8), (9, 8), (10, 8), (11, 5), (11, 6), (11, 7),(9, 9),(10, 9), (11, 9), (12, 6), (12, 7), (12, 8), (12, 9)])
        self.assertEqual((row,col), (6,3))
    
    
    
