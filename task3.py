
import csv


class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        return f"{self.date} | {self.category} | {self.amount:.2f} грн | {self.description}"


expenses = []

with open("data/expenses.csv", "r", encoding="utf-8-sig", newline="") as file:
    lines = (line for line in file if line.strip())
    reader = csv.DictReader(lines, delimiter=";")

    for row in reader:
        expense = Expense(
            row["date"],
            row["category"],
            row["amount"],
            row["description"]
        )
        expenses.append(expense)

print("Список витрат:")

for expense in expenses:
    print(expense.describe())

print("\nВеликі витрати (понад 300 грн):")

for expense in expenses:
    if expense.is_big(300):
        print(expense.describe())

print("\nКількість витрат:", len(expenses))
