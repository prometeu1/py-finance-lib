class Action:
    def __init__(self, symbol, name, quantity, buy_price, current_price):
        self.symbol = symbol
        self.name = name
        self.quantity = quantity
        self.buy_price = buy_price
        self.current_price = current_price

    @property
    def total_value(self):
        return round(self.quantity * self.current_price, 2)

    @property
    def profit(self):
        return round(self.total_value - (self.quantity * self.buy_price), 2)
