from src.models.piece import Piece


class King(Piece):
    def __init__(self, color, state):
        super().__init__(color, state)

    def is_valid_move(self, start, end):
        return abs(start.x - end.x) <= 1 and abs(start.y - end.y) <= 1

    def __str__(self):
        return "KING"