
class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def monthly_cost(self):
        return self.amount

class RecurringExpense(Expense):
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self):
        return self.amount * self.times_per_month

class SharedExpense(Expense):
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        self.people = people

    def monthly_cost(self):
        return self.amount / self.people

class YearlyExpense(Expense):
    def monthly_cost(self):
        return self.amount / 12

expenses = [
    RecurringExpense("2026-11-01", "Transport", 20, 20),
    RecurringExpense("2026-11-05", "Mobile", 150, 1),
    SharedExpense("2026-11-10", "Rent", 6000, 3),
    SharedExpense("2026-11-15", "Internet", 600, 2),
    YearlyExpense("2026-11-20", "Yearly subscription", 1200)
]

total = 0

print("Місячні витрати:")

for expense in expenses:
    cost = expense.monthly_cost()
    total += cost
    print(f"{expense.category}: {cost:.2f} грн")

print(f"\nЗагальна місячна вартість: {total:.2f} грн")