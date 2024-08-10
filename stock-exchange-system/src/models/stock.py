# Description: Stock model class.


class Stock:
    """Stock model class."""

    def __init__(self, symbol: str, name: str, price: float):
        self.symbol = symbol
        self.name = name
        self.price = price
