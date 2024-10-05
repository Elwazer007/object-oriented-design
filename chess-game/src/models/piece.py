from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, state):
        self.color = color
        self.state = state

    @abstractmethod
    def is_valid_move(self, start, end):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return self.__str__()