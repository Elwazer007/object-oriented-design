from src.models.piece import Piece


class Rock(Piece):
    def __init__(self, color, state):
        super().__init__(color, state)

    def is_valid_move(self, start, end):
        return start.x == end.x or start.y == end.y

    def __str__(self):
        return "ROCK"