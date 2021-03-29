import math, random, time

class Player():
    def __init__(self, symbol, player_type):
        self.symbol = symbol
        self.player_type = player_type

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol,"human")

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            #Get human player input
            square = input(f"{self.symbol}'s turn. Input move (0-8): ")
            if square == "exit":
                exit()
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

class RandomComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol, "computer")

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class AIComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol, "computer")

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.symbol)["position"]
        return square

    def minimax(self, state, player):
        max_player = self.symbol  # yourself
        other_player = "O" if player == "X" else "X"

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {"position": None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {"position": None, 'score': 0}

        if player == max_player:
            #Each score should maximize
            best = {"position": None, 'score': -math.inf}  
        else:
            #Each score should minimize
            best = {"position": None, 'score': math.inf}  
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            #Simulate a game after making that move
            sim_score = self.minimax(state, other_player) 

            #Undo move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best