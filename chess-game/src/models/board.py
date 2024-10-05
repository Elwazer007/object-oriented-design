from src.models.position import Position
from src.models.pawn import Pawn
from src.models.rock import Rock
from src.models.knight import Knight
from src.models.bishop import Bishop
from src.models.queen import Queen
from src.models.king import King


class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.populate_board()
    
    def populate_board(self):
        for i in range(8):
            self.board[1][i] = Position(1, i, "BLACK", Pawn("BLACK", "NORMAL"))
            self.board[6][i] = Position(6, i, "WHITE", Pawn("WHITE", "NORMAL"))
        self.board[0][0] = Position(0, 0, "BLACK", Rock("BLACK", "NORMAL"))
        self.board[0][1] = Position(0, 1, "BLACK", Knight("BLACK", "NORMAL"))
        self.board[0][2] = Position(0, 2, "BLACK", Bishop("BLACK", "NORMAL"))
        self.board[0][3] = Position(0, 3, "BLACK", Queen("BLACK", "NORMAL"))
        self.board[0][4] = Position(0, 4, "BLACK", King("BLACK", "NORMAL"))
        self.board[0][5] = Position(0, 5, "BLACK", Bishop("BLACK", "NORMAL"))
        self.board[0][6] = Position(0, 6, "BLACK", Knight("BLACK", "NORMAL"))
        self.board[0][7] = Position(0, 7, "BLACK", Rock("BLACK", "NORMAL"))
        self.board[7][0] = Position(7, 0, "WHITE", Rock("WHITE", "NORMAL"))
        self.board[7][1] = Position(7, 1, "WHITE", Knight("WHITE", "NORMAL"))
        self.board[7][2] = Position(7, 2, "WHITE", Bishop("WHITE", "NORMAL"))
        self.board[7][3] = Position(7, 3, "WHITE", Queen("WHITE", "NORMAL"))
        self.board[7][4] = Position(7, 4, "WHITE", King("WHITE", "NORMAL"))
        self.board[7][5] = Position(7, 5, "WHITE", Bishop("WHITE", "NORMAL"))
        self.board[7][6] = Position(7, 6, "WHITE", Knight("WHITE", "NORMAL"))
        self.board[7][7] = Position(7, 7, "WHITE", Rock("WHITE", "NORMAL"))

