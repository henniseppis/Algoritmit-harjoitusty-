import string
import copy
from board.board import Board
from ai.opponent import Opponent


class UI:
    def __init__(self):
        self.board = Board()
        self.op = Opponent(self.board)

    def start(self):
        """Starts the app and gives a menu for player to choose from"""

        while True:
            print("Tervetuloa pelaamaan ristinollaa\n")
            print("1. Aloita peli")
            print("2. Peliohjeet")
            print("3. Lopeta")
            choice = input("Valitse ylläolevista vaihtoehdoista: ")
            if choice == "1":
                self.start_game()
                break

            if choice == "2":
                self.game_rules()
                return

            if choice == "3":
                break

    def create_board(self):
        """Calls function in board.py to create frame of the board of asked size """

        board = [[" " for _ in range(20)]
                      for _ in range(20)]
        
        self.print_board(board)
        return board

    def start_game(self):
        """ Loop jumps between player making the move and AI making the move. 
        After every move there is a check for possible win. After making new move its closest cells are added to the cells_to_investigate list. 
        if list already contains a move we are trying to add, we first remove it and then add it to the end of the list due to the list is iterated backwards in minmax and we need to priorize moves which are closest the latest made move
        """
        symbol_gamer = "X"
        symbol_ai = "O"
        board = self.create_board()
        cells_to_investigate = []
        while True:
            row, column = self.choose_next_move(board)
            board = self.board.next_move(board,symbol_gamer, row, column)
            if (row, column) in cells_to_investigate:
                cells_to_investigate.remove((row,column))
            self.print_board(board)
            
            nearest_moves = self.op.find_nearest_free_cells(board, row, column)
            for move in nearest_moves:
                if move in cells_to_investigate:
                    cells_to_investigate.remove(move)
                cells_to_investigate.append(move)
            
            if self.board.check_win(board, row, column):
                self.game_won(symbol_gamer)
                break
            
            value, ai_row, ai_col = self.op.minmax(board, 0, 3, row, column, True, float("-inf"), float("inf"), cells_to_investigate)
            self.board.next_move(board, symbol_ai, ai_row, ai_col)
            if (ai_row, ai_col) in cells_to_investigate:
                cells_to_investigate.remove((ai_row,ai_col))
            self.print_board(board)
            
            nearest_moves = self.op.find_nearest_free_cells(board, ai_row, ai_col)
            for move in nearest_moves:
                if move in cells_to_investigate:
                    cells_to_investigate.remove(move)
                cells_to_investigate.append(move)
                    
            if self.board.check_win(board, ai_row, ai_col):
                self.game_won(symbol_ai)
                break

    def print_board(self, board):
        """Prints the board to command line"""

        alphabets = "   " + \
            "   ".join(string.ascii_uppercase[:20])
        print(alphabets)

        for i, row in enumerate(board):
            print(f"{str(i+1).rjust(2)}", end=" ")
            print(" | ".join(row))
            print(" " * 3 + "-" * (4 * (len(board))-2))

    def choose_next_move(self, board):
        """ Asks the next wanted move from the player. Divides it into right sections; 
        column and row which are returned and imported to the create_move function 
        which is run everytime after this function.
        """

        while True:
            try:
                choice = input(
                    "Valitse seuraava siirtosi (esim. C5 or F15): ").strip().upper()
                if len(choice) < 2:
                    raise ValueError(
                        "Virhe. Syötäthän siirtosi esim. C5 or F15 ")
                column = string.ascii_uppercase.index(choice[0])
                row = int(choice[1:]) - 1
                if board[row][column] == " ":
                    return row, column
                else:
                    print("Ruudussa on jo nappula. Valitse toinen ruutu")
                    continue
            except (ValueError, IndexError):
                print("Virhe. Syötäthän siirtosi esim. C5 or F15")

    def game_won(self, symbol):
        """ Announces the winner after the game """

        if symbol == "X":
            print("\n")
            return "Peli päättyi. Onnea voitit pelin!"
        return "Peli päättyi. AI vei voiton tällä kertaa"

    def game_rules(self):
        print("\n")
        print("Pelaat merkillä X ja AI merkillä O. Pelin tarkoituksena on laittaa vuorotellen nappuloita 20x20 kokoiselle \n laudalle syöttämällä halutun ruudun koordinaatit muodossa (sarake+rivi. Esim. B7) \n Se kumpi saa ensiksi viisi omaa merkkiään peräkkäin laudalle pysty-, vaaka- tai vinoriville on voittaja. \n TSEMPPIÄ! \n")
        print("1. OK aloitetaan")
        print("2. Hmm en haluakkaan pelata juuri nyt")
        choice = input("Kumpi on valintasi tänään? ")
        if choice == "1":
            self.start_game()
        if choice == "2":
            return
