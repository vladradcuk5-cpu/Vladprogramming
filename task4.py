
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


class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(expense.amount for expense in self.expenses)

    def by_category(self):
        result = {}

        for expense in self.expenses:
            result[expense.category] = result.get(expense.category, 0) + expense.amount

        return result

    def top(self, count=5):
        return sorted(self.expenses, key=lambda expense: expense.amount, reverse=True)[:count]


book = ExpenseBook()

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
        book.add(expense)

print("Загальна сума витрат:")
print(f"{book.total():.2f} грн")

print("\nВитрати за категоріями:")

for category, amount in book.by_category().items():
    print(f"{category}: {amount:.2f} грн")

print("\nТоп-5 найбільших витрат:")

for expense in book.top(5):
    print(expense.describe())

print("\nКількість записів:", len(book.expenses))
