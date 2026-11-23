
import csv

class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Owner name cannot be empty")
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = round(value, 2)

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Not enough money")
        self.__balance = round(self.__balance - amount, 2)

wallet = Wallet("Vladyslav Radchuk", 6000)

print("Власник:", wallet.owner)
print("Початковий баланс:", wallet.balance, "грн")
print("\nСписок витрат:")

with open("data/expenses.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")

    for row in reader:
        amount = float(row["amount"])

        try:
            wallet.withdraw(amount)
            print(f'{row["date"]} | {row["category"]} | {row["description"]} | {amount:.2f} грн')
        except ValueError:
            print(f'Недостатньо коштів для витрати: {row["category"]}')
            break

print("\nЗалишок:", wallet.balance, "грн")