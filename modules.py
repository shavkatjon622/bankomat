class Bankomat():
    """This is bankomat command project"""
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return f"Your currently balance: {self.balance} $"

    def subtraction_balance(self, widraw):
        if widraw > self.balance:
            return "Not enough money!"
        else:
            self.balance = self.balance - widraw - widraw * 0.01
            return f"Your currently balance: {self.balance} $"
    def add_balance(self, amount):
        self.balance += amount
        return f"Your currently balance: {self.balance} $"