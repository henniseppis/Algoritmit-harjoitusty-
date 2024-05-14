import unittest
from board.board import Board
from UI.ui import UI


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.ui = UI()
        self.create_board = self.ui.create_board()

    def test_next_move(self):
        board = self.ui.create_board()
        self.board.next_move(board,"X", 0, 6)
        self.assertEqual(board[0][6], "X")

    def test_win_check_diagonal(self):
        board = self.ui.create_board()
        self.board.next_move(board,"X", 0, 6)
        self.board.next_move(board,"X", 1, 5)
        self.board.next_move(board,"X", 2, 4)
        self.board.next_move(board,"X", 3, 3)
        self.board.next_move(board,"X", 4, 2)
        win = self.board.check_win(board, 4, 2)
        self.assertEqual(win, True)

    def test_win_check_diagonal_false(self):
        board = self.ui.create_board()
        self.board.next_move(board,"X", 0, 6)
        self.board.next_move(board,"X", 1, 5)
        self.board.next_move(board,"O", 2, 4)
        self.board.next_move(board,"X", 3, 3)
        self.board.next_move(board,"X", 4, 2)
        win = self.board.check_win(board, 4, 2)
        self.assertEqual(win, False)

    def test_win_check_horizontal(self):
        board = self.ui.create_board()
        self.board.next_move(board,"X", 2, 10)
        self.board.next_move(board,"X", 2, 11)
        self.board.next_move(board,"X", 2, 12)
        self.board.next_move(board,"X", 2, 13)
        self.board.next_move(board,"X", 2, 14)
        win = self.board.check_win(board, 2, 14)
        self.assertEqual(win, True)

    def test_win_check_horizontal_false(self):
        board = self.ui.create_board()
        self.board.next_move(board,"X", 2, 10)
        self.board.next_move(board,"X", 2, 11)
        self.board.next_move(board,"X", 2, 12)
        self.board.next_move(board,"O", 2, 13)
        self.board.next_move(board,"X", 2, 14)
        win = self.board.check_win(board, 2, 14)
        self.assertEqual(win, False)

    def test_win_check_vertical(self):
        board = self.ui.create_board()
        self.board.next_move(board,"X", 3, 10)
        self.board.next_move(board,"X", 4, 10)
        self.board.next_move(board,"X", 5, 10)
        self.board.next_move(board,"X", 6, 10)
        self.board.next_move(board,"X", 7, 10)
        win = self.board.check_win(board, 7, 10)
        self.assertEqual(win, True)

    def test_win_check__vertical_false(self):
        board = self.ui.create_board()
        self.board.next_move(board,"X", 3, 10)
        self.board.next_move(board,"X", 4, 10)
        self.board.next_move(board,"X", 5, 10)
        self.board.next_move(board,"O", 6, 10)
        self.board.next_move(board,"X", 7, 10)
        win = self.board.check_win(board, 7, 10)
        self.assertEqual(win, False)

    def test_check_draw(self):
        board = self.ui.create_board()
        for i in range(0, 20):
            for x in range(0, 20):
                board[i][x] = "X"
        draw = self.board.check_draw(board)
        self.assertEqual(draw, True)

    def test_check_draw_false(self):
        board = self.ui.create_board()
        for i in range(0, 18):
            for x in range(0, 20):
                board[i][x] = "X"
        draw = self.board.check_draw(board)
        self.assertEqual(draw, False)

    def test_win_check_five_symbols_row_but_not_next_to_each_other(self):
        board = self.ui.create_board()
        self.board.next_move(board,"X", 1, 2)
        self.board.next_move(board,"X", 1, 3)
        self.board.next_move(board,"X", 1, 5)
        self.board.next_move(board,"X", 1, 6)
        self.board.next_move(board,"X", 1, 7)
        win = self.board.check_win(board, 1, 7)
        self.assertEqual(win, False)

    def test_win_check_five_symbols_row_but_not_above_each_other(self):
        board = self.ui.create_board()
        self.board.next_move(board,"O", 5, 3)
        self.board.next_move(board,"O", 6, 3)
        self.board.next_move(board,"O", 7, 3)
        self.board.next_move(board,"O", 9, 3)
        self.board.next_move(board,"O", 10, 3)
        win = self.board.check_win(board, 10, 3)
        self.assertEqual(win, False)

    def test_win_check_five_symbols_row_but_not_diagonally(self):
        board = self.ui.create_board()
        self.board.next_move(board, "O", 5, 3)
        self.board.next_move(board, "O", 6, 4)
        self.board.next_move(board, "O", 8, 6)
        self.board.next_move(board, "O", 9, 7)
        self.board.next_move(board, "O", 10, 8)
        win = self.board.check_win(board, 10, 8)
        self.assertEqual(win, False)

    
    def test_check_horizontal(self):
        self.create_board[2][3] = "X"
        self.create_board[2][10] = "X"
        self.create_board[2][15] = "O"
        value = self.board.check_horizontal(self.create_board[2], "X")
        self.assertEqual(value, 2)
    
    def test_check_horizontal_four_in_row(self):
        self.create_board[2][3] = "X"
        self.create_board[2][4] = "X"
        self.create_board[2][5] = "X"
        self.create_board[2][6] = "X"
        self.create_board[2][15] = "O"
        value = self.board.check_horizontal(self.create_board[2], "X")
        self.assertEqual(value, 16)
    
    def test_check_vertical(self):
        self.create_board[7][3] = "O"
        self.create_board[8][3] = "X"
        self.create_board[9][3] = "X"
        value = self.board.check_vertical([self.create_board[j][3] for j in range(20)], "X")
        self.assertEqual(value, 4)
    
    def test_check_diagonal(self):
        self.create_board[7][4] = "O"
        self.create_board[8][5] = "X"
        self.create_board[9][6] = "X"
        self.create_board[10][7] = "X"
        value = self.board.check_diagonal(self.create_board, "X")
        self.assertEqual(value, 12)