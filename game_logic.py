from constants import PLAYER_X, PLAYER_O, EMPTY

class TicTacToe:
    def __init__(self):
        self.board = [EMPTY for _ in range(9)]
        self.current_winner = None

    def make_move(self, position, player):
        if self.board[position] == EMPTY:
            self.board[position] = player
            if self.check_winner(position, player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, pos, player):
        # Check row
        row_ind = pos // 3
        row = self.board[row_ind*3:(row_ind + 1)*3]
        if all([spot == player for spot in row]):
            return True

        # Check column
        col_ind = pos % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == player for spot in column]):
            return True

        # Check diagonals
        if pos % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == player for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == player for spot in diagonal2]):
                return True

        return False

    def empty_squares(self):
        return EMPTY in self.board

    def num_empty_squares(self):
        return self.board.count(EMPTY)

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == EMPTY]

    def reset(self):
        self.board = [EMPTY for _ in range(9)]
        self.current_winner = None