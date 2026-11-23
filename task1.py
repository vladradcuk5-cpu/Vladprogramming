
class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Owner name cannot be empty")

        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self.balance = round(balance, 2)

wallet = Wallet("Vladyslav Radchuk", 6000)

print("Власник:", wallet.owner)
print("Баланс:", wallet.balance, "грн")

try:
    wallet1 = Wallet("", 1000)
except ValueError as error:
    print("Помилка:", error)

try:
    wallet2 = Wallet("Vladyslav Radchuk", -500)
except ValueError as error:
    print("Помилка:", error)