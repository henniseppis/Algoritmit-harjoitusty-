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
    def test_choose_move_valid_input(self, mocked_input):
        move = self.ui.choose_next_move(self.board)
        self.assertEqual(move, (0, 0))
        
    def test_game_won_X_wins(self):
        winner = self.ui.game_won("X")
        self.assertEqual(winner, "Peli päättyi. Onnea voitit pelin!")
    
    def test_game_won_O_wins(self):
        winner = self.ui.game_won("O")
        self.assertEqual(winner,  "Peli päättyi. AI vei voiton tällä kertaa")

        
        
        
        

        