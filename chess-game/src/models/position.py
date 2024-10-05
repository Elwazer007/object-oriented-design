class Position:
    def __init__(self, x, y, color, piece=None):
        self.x = x
        self.y = y
        self.color = color
        self.piece = piece

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"