import unittest
from logic.opponent import Opponent
from board.board import Board

class TestOpponentd(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=20)
    
    