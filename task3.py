
class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not value.strip():
            raise ValueError("Owner name cannot be empty")
        self.__owner = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = round(value, 2)

    @property
    def is_empty(self):
        return self.__balance == 0

wallet = Wallet("Vladyslav Radchuk", 1500)

print("Власник:", wallet.owner)
print("Баланс:", wallet.balance)

wallet.balance = 1200.555
print("Новий баланс:", wallet.balance)

print("Гаманець порожній:", wallet.is_empty)

try:
    wallet.balance = -500
except ValueError as error:
    print("Помилка:", error)

try:
    wallet.is_empty = True
except AttributeError as error:
    print("Помилка:", error)