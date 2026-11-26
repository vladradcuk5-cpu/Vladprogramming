
import json
from datetime import date

print("Vlad Radchuk, IT-32")

input_file = "data/expenses.json"
output_file = "data/expenses_updated.json"

with open(input_file, "r", encoding="utf-8") as file:
    expenses = json.load(file)

new_expense = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 75.00,
    "comment": "Lunch"
}

expenses.append(new_expense)
added = 1

old_count = len(expenses)

expenses = [item for item in expenses if item["amount"] >= 10]

deleted = old_count - len(expenses)

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=2, ensure_ascii=False)

print(f"added: {added}")
print(f"deleted: {deleted}")
print(f"remaining: {len(expenses)}")
