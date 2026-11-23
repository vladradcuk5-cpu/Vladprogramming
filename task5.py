class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __del__(self):
        print(f"Гаманець {self.owner} видалено")

print("1. Видалення єдиного посилання:")
wallet = Wallet("Vladyslav Radchuk", 1000)
del wallet

print("\n2. Два посилання на один об'єкт:")
wallet = Wallet("Vladyslav Radchuk", 2000)
other = wallet

del wallet
print("Об'єкт ще доступний через other")

del other

print("\n3. Видалення наприкінці програми:")
wallet = Wallet("Vladyslav Radchuk", 3000)
print("Програма завершується")