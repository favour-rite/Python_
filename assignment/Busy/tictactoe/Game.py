from tictactoe.Board import Board
from tictactoe.Players import Players

class Game:

    def __init__(self):
        self.player1 = Players("Player 1", "X")
        self.player2 = Players("Player 2", "O")
        self.current_player = self.player1
        self.board = Board()

    def make_move(self, row, column, player):
        if 0 <= row < 3 and 0 <= column < 3 and self.board[row][column] == '_':
            self.board[row][column] = player
            raise ValueError("Must be between 1 and 3")
            return True
        return False

    def is_draw(self,row,column):
        for row in range (3):
            for column in range (3):
                if self.board[row][column] == '_':
                    return False
        return True


    def check_win(self, row, column, player):

        for row in range(3):
            if self.board[row][1] == player and self.board.display_board()[row][1]:
                return True
        for column in range(3):
            if self.board[column][1] == player and self.board[column][1] == player and self.board[column][2] == player:
                return True
        for row in range(3):
            if self.board[row][1] == player and  self.board[row][2] == player and self.board[row][3] == player:
                return True
            if self.board[row][1] == player and self.board[row][2] == player and self.board[row][3] == player:
                return True
            if self.board[row][1] == player and self.board[row][2] == player and self.board[row][3] == player:
                return True
        return False










