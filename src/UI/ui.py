import string
from board.board import Board
from logic.opponent import Opponent

class UI:
    def __init__(self):
        self.board = Board(size=20)
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

        board = self.board.create_board()
        self.print_board(board)
        return board
    
    def start_game(self):
        """ Starts the game. Loop jumps between player making the move and AI making the move. 
        After every move there is a check for possible win.
        """
        symbol_gamer = "X"
        symbol_ai = "O"
        board = self.create_board()
        while True:
            row, column = self.choose_next_move(board)
            board, previous_moves = self.board.next_move(symbol_gamer, row, column)
            self.print_board(board)
            if self.board.check_win(board, row, column) == -10000:
                self.game_won(symbol_gamer)
                break
            ai_row, ai_col = self.op.ai_create_move(board, row, column, previous_moves, max_depth=5 )
            board = self.board.next_move(symbol_ai, ai_row, ai_col)[0]
            self.print_board(board)
            if self.board.check_win(board, ai_row, ai_col) == 10000:
                self.game_won(symbol_ai)
                break

    def print_board(self, board):
        """Prints the board to command line"""

        alpha = "  " + "   ".join(string.ascii_uppercase[:self.board.board_size])
        print(alpha)

        for i, row in enumerate(board):
            print(f"{i+1}", end=" ")
            print(" | ".join(row))
            print(" " * 3 + "-" * (4 * len(board)))
    
    def choose_next_move(self, board):
        
        """ Asks the next wanted move from the player. Divides it into right sections; 
        column and row which are returned and imported to the create_move function 
        which is run everytime after this function.
        """
        
        while True:
            try:
                position = input("Valitse seuraava siirtosi (esim. C5 or F15): ").strip().upper()
                if len(position) < 2:
                    raise ValueError("Virhe. Syötäthän siirtosi esim. C5 or F15 ")
                column = string.ascii_uppercase.index(position[0])
                row = int(position[1:]) - 1
                if board[row][column] == " ":
                    return row, column
                else:
                    print("Ruudussa on jo nappula. Valitse toinen ruutu")
                    continue
            except (ValueError, IndexError):
                print("Virhe. Syötäthän siirtosi esim. C5 or F15")
    
    def game_won(self, symbol):
        """ Announce the winner after the game """

        if symbol == "X":
            print("\n")
            print("Peli päättyi. Onnea voitit pelin!")
        elif symbol == "O":
            print("\n")
            print("Peli päättyi. AI vei voiton tällä kertaa")

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




            
       




            