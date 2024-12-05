import random
from constants import PLAYER_X, PLAYER_O, EMPTY

class AIPlayer:
    @staticmethod
    def get_move(game):
        available_moves = game.available_moves()
        
        # Try to win
        for move in available_moves:
            game.board[move] = PLAYER_O
            if game.check_winner(move, PLAYER_O):
                game.board[move] = EMPTY
                return move
            game.board[move] = EMPTY
        
        # Block opponent's winning move
        for move in available_moves:
            game.board[move] = PLAYER_X
            if game.check_winner(move, PLAYER_X):
                game.board[move] = EMPTY
                return move
            game.board[move] = EMPTY
        
        # Take center if available
        if 4 in available_moves:
            return 4
        
        # Take corners
        corners = [0, 2, 6, 8]
        available_corners = [move for move in corners if move in available_moves]
        if available_corners:
            return random.choice(available_corners)
        
        # Take edges
        edges = [1, 3, 5, 7]
        available_edges = [move for move in edges if move in available_moves]
        if available_edges:
            return random.choice(available_edges)
        
        return random.choice(available_moves)