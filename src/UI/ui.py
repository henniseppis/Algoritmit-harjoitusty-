import string
from board.board import Board
from logic.opponent import Opponent

class UI:
    def __init__(self):
        self.board = Board(size=20)
        self.size = 20
        self.op = Opponent()

    def start(self):
        while True:
            print("Tervetuloa pelaamaan ristinollaa\n")
            print("1. Aloita peli")
            
            choice = input("Valitse ylläolevista vaihtoehdoista: ")

            if choice == "1":
                self.start_game()
                break

    def create_board(self):
            board = self.board.create_board()
            self.print_board(board)
            return board       
    
    def start_game(self):
        board = self.create_board()
        while True:
        #    if symbol == "X" or symbol == "O":
            symbol_gamer = "X"
            symbol_ai = "O"
            row, column = self.choose_next_move()
            board = self.board.next_move(symbol_gamer, row, column)     
            self.print_board(board)
            ai_row, ai_col = self.op.create_move()
            board = self.board.next_move(symbol_ai, ai_row, ai_col) 
            self.print_board(board)
    
    def print_board(self, board):
        alpha = "  " + "   ".join(string.ascii_uppercase[:self.size])
        print(alpha)

        for i, row in enumerate(board):
            print(f"{i+1}", end=" ")
            print(" | ".join(row))
            print(" " * 3 + "-" * (4 * len(board)))
    
    def choose_next_move(self):
        while True:
            try:
                position = input("Valitse seuraava siirtosi (esim. C5 or F15): ").strip().upper()
                if len(position) < 2:
                    raise ValueError("Virhe. Syötäthän siirtosi esim. C5 or F15 ")
                column = string.ascii_uppercase.index(position[0])
                row = int(position[1:]) - 1
                return row, column
            except (ValueError, IndexError):
                print("Virhe. Syötäthän siirtosi esim. C5 or F15")
    
    def wrong_move(self):
        print("Ruudussa on jo nappula. Valitse toinen ruutu")

            
       




            