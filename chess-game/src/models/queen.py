from src.models.piece import Piece


class Queen(Piece):
    def __init__(self, color, state):
        super().__init__(color, state)

    def is_valid_move(self, start, end):
        pass

    def __str__(self):
        return "QUEEN"