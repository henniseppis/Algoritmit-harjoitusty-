import unittest
from ai.opponent import Opponent
from UI.ui import UI


class TestOpponentd(unittest.TestCase):
    def setUp(self):
        self.ui = UI()
        self.board = self.ui.create_board()
        self.opponent = Opponent(self.board)
       
    
    def test_find_nearest_cells(self):
        self.board[5][7] = "X"
        cells = self.opponent.find_nearest_free_cells(self.board, 5, 7)
        self.assertEqual(cells, [(3, 5), (3, 6),(3, 7),(3, 8),(4, 5),(4, 6),(4, 7),(4, 8),(5, 5),(5, 6),(5, 8),(6, 5),(6, 6),(6, 7),(6, 8)])        
    
    
    def test_find_nearest_free_cells_wont_add_occupied_cells_to_list(self):
        self.board[5][7] = "X"
        cells = self.opponent.find_nearest_free_cells(self.board, 5, 7)
        self.assertEqual(cells, [(3, 5), (3, 6),(3, 7),(3, 8),(4, 5),(4, 6),(4, 7),(4, 8),(5, 5),(5, 6),(5, 8),(6, 5),(6, 6),(6, 7),(6, 8)])
        self.board[6][7] = "X"
        cells = self.opponent.find_nearest_free_cells(self.board, 6, 7)
        self.assertEqual(cells, [(4, 5),(4, 6),(4, 7),(4, 8),(5, 5),(5, 6),(5, 8),(6, 5),(6, 6),(6, 8), (7, 5),(7, 6),(7, 7),(7, 8)])
   
    
