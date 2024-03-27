import unittest
from UI.ui import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.ui = UI()
        
    def test_board_is_printed_in_correct_size(self):
        board = self.ui.create_board()
        self.assertEqual(len(board), 20)
    
    
