import unittest
from board.board import Board
from UI.ui import UI


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=20)
        self.ui =  UI()
        
    def test_next_move(self):
        board = self.board.create_board()
        self.board.next_move("X", 0, 6)
        self.assertEqual(board[0][6], "X")

    def test_win_check_diagonal(self):
        board = self.board.create_board()
        self.board.next_move("X", 0, 6)
        self.board.next_move("X", 1, 5)
        self.board.next_move("X", 2, 4)
        self.board.next_move("X", 3, 3)
        self.board.next_move("X", 4, 2)
        win = self.board.check_win(board, 4,2,"X")
        self.assertEqual(win , True)

    def test_win_check_diagonal_false(self):
        board = self.board.create_board()
        self.board.next_move("X", 0, 6)
        self.board.next_move("X", 1, 5)
        self.board.next_move("O", 2, 4)
        self.board.next_move("X", 3, 3)
        self.board.next_move("X", 4, 2)
        win = self.board.check_win(board, 4,2,"X")
        self.assertEqual(win , False)

    def test_win_check_horizontal(self):
        board = self.board.create_board()
        self.board.next_move("X", 2, 10)
        self.board.next_move("X", 2, 11)
        self.board.next_move("X", 2, 12)
        self.board.next_move("X", 2, 13)
        self.board.next_move("X", 2, 14)
        win = self.board.check_win(board, 2,14,"X")
        self.assertEqual(win , True)


    def test_win_check_horizontal_false(self):
        board = self.board.create_board()
        self.board.next_move("X", 2, 10)
        self.board.next_move("X", 2, 11)
        self.board.next_move("X", 2, 12)
        self.board.next_move("O", 2, 13)
        self.board.next_move("X", 2, 14)
        win = self.board.check_win(board, 2,14,"X")
        self.assertEqual(win , False)
    
    def test_win_check__vertical(self):
        board = self.board.create_board()
        self.board.next_move("X", 3, 10)
        self.board.next_move("X", 4, 10)
        self.board.next_move("X", 5, 10)
        self.board.next_move("X", 6, 10)
        self.board.next_move("X", 7, 10)
        win = self.board.check_win(board, 7,10,"X")
        self.assertEqual(win , True)


    def test_win_check__vertical_false(self):
        board = self.board.create_board()
        self.board.next_move("X", 3, 10)
        self.board.next_move("X", 4, 10)
        self.board.next_move("X", 5, 10)
        self.board.next_move("O", 6, 10)
        self.board.next_move("X", 7, 10)
        win = self.board.check_win(board, 7,10,"X")
        self.assertEqual(win , False)
    
    def test_check_draw(self):
        board = self.board.create_board()
        for i in range(0,20):
            for x in range(0,20):
                board[i][x] = "X"
        draw = self.board.check_draw(board)
        self.assertEqual(draw , True)
    
    def test_check_draw_false(self):
        board = self.board.create_board()
        for i in range(0,18):
            for x in range(0,20):
                board[i][x] = "X"
        draw = self.board.check_draw(board)
        self.assertEqual(draw , False)

    def test_win_check_five_symbols_row_but_not_next_to_each_other(self):
        board = self.board.create_board()
        self.board.next_move("X", 1, 2)
        self.board.next_move("X", 1, 3)
        self.board.next_move("X", 1, 5)
        self.board.next_move("X", 1, 6)
        self.board.next_move("X", 1, 7)
        win = self.board.check_win(board, 1,7,"X")
        self.assertEqual(win , False)
    
    def test_win_check_five_symbols_row_but_not_above_each_other(self):
        board = self.board.create_board()
        self.board.next_move("O", 5, 3)
        self.board.next_move("O", 6, 3)
        self.board.next_move("O", 7, 3)
        self.board.next_move("O", 9, 3)
        self.board.next_move("O", 10, 3)
        win = self.board.check_win(board, 10,3,"O")
        self.assertEqual(win , False)



    