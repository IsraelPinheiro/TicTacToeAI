from player import *

class TicTacToe():
    def __init__(self):
        self.current_winner = None
        self.empty_symbol = " "
        self.board = self.make_board(self.empty_symbol)

    @staticmethod
    def make_board(empty_symbol):
        return [empty_symbol for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        #| 0 | 1 | 2 |
        #| 3 | 4 | 5 |
        #| 6 | 7 | 8 |
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| "+ ' | '.join(row) + " |")
        print("")

    def make_move(self, square, symbol):
        if self.board[square] == self.empty_symbol:
            self.board[square] = symbol
            if self.winner(square, symbol):
                self.current_winner = symbol
            return True
        return False

    def winner(self, square, symbol):
        #Check rows
        row_index = square//3
        row = self.board[row_index*3:(row_index+1)*3]
        if all([spot == symbol for spot in row]):
            return True

        #Check columns
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == symbol for spot in column]):
            return True

        #Check Diagonals, but only if square is a even number
        if square % 2 == 0:
            lr_diagonal = [self.board[i] for i in [0, 4, 8]] #Left -> Right Diagonal
            if all([s == symbol for s in lr_diagonal]):
                return True
            rl_diagonal = [self.board[i] for i in [2, 4, 6]] #Right -> Left Diagonal
            if all([s == symbol for s in rl_diagonal]):
                return True

        #All checks failed, not a winning move
        return False

    def empty_squares(self):
        return self.empty_symbol in self.board

    def num_empty_squares(self):
        return len(self.available_moves())
        #return self.board.count(self.empty_symbol)

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == self.empty_symbol]

def play(game:TicTacToe, x_player:Player, o_player:Player, print_game:bool=True):
    if print_game:
        game.print_board_nums()

    symbol = "X"
    while game.empty_squares():
        #Get player turn
        if symbol == "X":
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, symbol):
            if print_game:
                print(f"{symbol} makes a move to square {square}")
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f"{symbol} wins!")
                #End the loop and exits the game
                return symbol 

            #Switches player
            symbol = "O" if symbol == "X" else "X"
            if symbol=="X":
                if x_player.player_type=="computer": time.sleep(0.8)
            else:
                if o_player.player_type=="computer": time.sleep(0.8)

    if print_game:
        print("It's a tie!")

def banner():
    print(r"#======================================================#")
    print(r"#   _____ _         _____             _____            #")
    print(r"#  |_   _(_) ___   |_   _|_ _  ___   |_   _|__   ___   #")
    print(r"#    | | | |/ __|____| |/ _` |/ __|____| |/ _ \ / _ \  #")
    print(r"#    | | | | (_|_____| | (_| | (_|_____| | (_) |  __/  #")
    print(r"#    |_| |_|\___|    |_|\__,_|\___|    |_|\___/ \___|  #")
    print(r"#                                                      #")
    print(r"#                        v1.0.0                        #")
    print(r"#======================================================#")
    print("")


def select_player(symbol:str):
    print("1 - Human Player")
    print("2 - Computer Player (Random)")
    print("3 - Computer Player (AI)")
    option = input(f"Select the {symbol.upper()} Player: ")
    if option=="1":
        return HumanPlayer(symbol)
    elif option=="2":
        return RandomComputerPlayer(symbol)
    elif option=="3":
        return AIComputerPlayer(symbol)
    else:
        print("Invalid option!")
        return select_player(symbol)

if __name__ == '__main__':
    #Print the game banner
    banner()
    #Select X Player
    x_player = select_player("X")
    #Select O Player
    o_player = select_player("O")
    #Create da game
    game = TicTacToe()
    #Start the game
    play(game, x_player, o_player, print_game=True)