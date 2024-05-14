import unittest
from unittest.mock import patch
from UI.ui import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.ui = UI()
        self.board = self.ui.create_board()
        
    def test_board_is_printed_in_correct_size(self):
        self.assertEqual(len(self.board), 20)

    @patch('builtins.input', side_effect=["A1"])
    def test_choose_move_valid_input(self, input):
        move = self.ui.choose_next_move(self.board)
        self.assertEqual(move, (0, 0))
    
    @patch('builtins.input', side_effect=["X","8B","B2"])
    def test_choose_move_wont_return_invalid_move(self, input):
        """ This test returns only the last inputs coordinates 1,1 """
        
        move = self.ui.choose_next_move(self.board)
        self.assertEqual(move, (1,1))
    
    @patch('builtins.input', side_effect=["B2","B3"])
    def test_choose_move_wont_return_occupied_cell_coordinate(self, input):
        self.board[1][1] = "O"
        move = self.ui.choose_next_move(self.board)
        self.assertEqual(move, (2,1))
        
    def test_game_won_X_wins(self):
        winner = self.ui.game_won("X")
        self.assertEqual(winner, "Peli päättyi. Onnea voitit pelin!")
    
    def test_game_won_O_wins(self):
        winner = self.ui.game_won("O")
        self.assertEqual(winner,  "Peli päättyi. AI vei voiton tällä kertaa")

        
        
        
        

        