
import csv
import json
import os

print("Vladyslav Radchuk, IT-32")

with open("data/expenses.csv", "r", encoding="utf-8-sig") as file:
    lines = [line for line in file if line.strip()]

    reader = csv.DictReader(lines, delimiter=";")
    expenses = []

    for row in reader:
        expenses.append({
            "date": row["date"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "comment": row["description"]
        })

with open("data/expenses.json", "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=2, ensure_ascii=False)

size = os.path.getsize("data/expenses.json")

print("records:", len(expenses))
print(f"saved: data/expenses.json ({size} bytes)")
