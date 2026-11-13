
import json
from datetime import date

print("Vladyslav Radchuk, IT-32")

with open("data/expenses.json", "r", encoding="utf-8") as file:
    expenses = json.load(file)

new_expense = {
    "date": date.today().isoformat(),
    "category": "Food",
    "amount": 50,
    "comment": "New expense"
}

expenses.append(new_expense)

added = 1

old_count = len(expenses)

expenses = [item for item in expenses if item["amount"] >= 10]

deleted = old_count - len(expenses)

with open("data/expenses_updated.json", "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=2, ensure_ascii=False)

print("added:", added)
print("deleted:", deleted)
print("records:", len(expenses))
