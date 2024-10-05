from src.models.piece import Piece
from src.models.position import Position


class Movement:
    def __init__(self, start: Position, end: Position, piece: Piece):
        self.start = start
        self.end = end
        self.piece = piece
        self.captured_piece = None

    def __str__(self):
        return f"{self.piece} from {self.start} to {self.end}"
    
    def is_valid(self):
        return self.piece.is_valid_move(self.start, self.end)
    
    def execute(self):
        self.captured_piece = self.end.piece
        self.end.piece = self.piece
        self.start.piece = None


