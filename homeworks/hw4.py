rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def convert_to_kgs(self):
        return self.amount * rates[self.currency]
    def __add__(self, other):
        return Money(self.convert_to_kgs() + other.convert_to_kgs(), "KGS")
    def __sub__(self, other):
        return Money(self.convert_to_kgs() - other.convert_to_kgs(), "KGS")
    def __mul__(self, number):
        return Money(self.amount * number, self.currency)
    def __truediv__(self, number):
        return Money(self.amount / number, self.currency)
    def __str__(self):
        amount = int(self.amount) if self.amount == int(self.amount) else self.amount
        return f"{amount} {self.currency}"

money1 = Money(115, "USD")
money2 = Money(8000, "KGS")
print(money1 + money2)
print(money1 - money2)
print(money1 * 3)
print(money2 / 2)