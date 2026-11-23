
class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Owner name cannot be empty")
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("Not enough money")
        self.__balance -= amount

wallet = Wallet("Vladyslav Radchuk", 6000)

wallet.deposit(500)
wallet.withdraw(200)

print("Власник:", wallet.owner)

try:
    print(wallet.__balance)
except AttributeError as error:
    print("Помилка доступу:", error)

print("Баланс через name mangling:", wallet._Wallet__balance)