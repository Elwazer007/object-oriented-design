from src.models.account import Account


class Member(Account):
    """Member model class."""

    def __init__(self, funds: float, stock_positions, active_orders):
        self.funds = funds
        self.stock_positions = stock_positions
        self.active_orders = active_orders

    def add_funds(self, amount):
        """Add funds to member account."""
        self.funds += amount

    def withdraw_funds(self, amount):
        """Withdraw funds from member account."""
        self.funds -= amount

    def place_limit_buy_order(self, stock, quantity, price):
        """Place limit buy order."""
        pass

    def place_limit_sell_order(self, stock, quantity, price):
        """Place limit sell order."""
        pass

    def place_market_buy_order(self, stock, quantity):
        """Place market buy order."""
        pass

    def place_market_sell_order(self, stock, quantity):
        """Place market sell order."""
        pass

    def cancel_order(self, order):
        """Cancel order."""
        pass
