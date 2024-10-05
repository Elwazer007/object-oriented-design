from src.models.board import Board
from src.models.player import Player


class Game:
    def __init__(self, board: Board, player1: Player, player2: Player):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.winner = None
        self.state = None

    def get_winner(self):
        if self.board.is_checkmate():
            return self.player1 if self.current_player == self.player2 else self.player2

    def play(self):
        while self.winner is None:
            move = self.current_player.get_move(self.board)
            move.execute()
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2
            self.winner = self.get_winner()
        return self.winner