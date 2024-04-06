#import unittest
#import string 
#from board.board import Board
#
#
#class BoardStubb:
#    def create_board_test(self):
#        self.board = [[" " for _ in range(20)] for _ in range(20)]
#    
#    def print_board_test(self, board):
#        """Prints the board to command line"""
#        alpha = "  " + "   ".join(string.ascii_uppercase[:20])
#        print(alpha)
#
#        for i, row in enumerate(board):
#            print(f"{i+1}", end=" ")
#            print(" | ".join(row))
#            print(" " * 3 + "-" * (4 * len(board)))
#
#
#class TestBoard(unittest.TestCase):
#    def setUp(self):
#        self.board = BoardStubb()
#        self.board_functions = Board(size=20)
#        
#    def test_next_move(self):
#        board = self.board.create_board_test()
#        self.board_functions.next_move("X", 0, 6)
#        self.assertEqual(board[0][6], "X")
#    