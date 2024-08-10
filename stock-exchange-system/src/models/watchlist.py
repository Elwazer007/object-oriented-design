# This file contains the WatchList class.


class WatchList:
    """WatchList class."""

    def __init__(self, id, name, stocks):
        """__init__ method for WishList class."""
        self.id = id
        self.name = name
        self.stocks = stocks

    def add_stock(self, stock):
        """Add stock to watchlist."""
        self.stocks.append(stock)

    def remove_stock(self, stock):
        """Remove stock from watchlist."""
        self.stocks.remove(stock)

    def get_stocks(self):
        """Get all stocks in watchlist."""
        return self.stocks
