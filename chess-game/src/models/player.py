from src.models.account import Account
from src.models.board import Board


class Player(Account):
    def __init__(self, name, email, password, is_white):
        super().__init__(name, email, password)
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.is_white = is_white

    def get_move(self, board: Board):
        pass

    def __str__(self):
        return self.name
    



