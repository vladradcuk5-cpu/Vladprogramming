from decimal import Decimal
import csv
from tabulate import tabulate

print("Vlad Radchuk, IT-32")

expenses = {}

with open("data/expenses.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        if not row or not row[0].strip() or row[0].strip().startswith("#"):
            continue

        if row[0].strip().lower() == "category":
            continue

        category = row[0].strip()
        amount = Decimal(row[1].strip())

        if category not in expenses:
            expenses[category] = {"count": 0, "total": Decimal("0")}

        expenses[category]["count"] += 1
        expenses[category]["total"] += amount

table = []

total_count = 0
total_sum = Decimal("0")

for category, values in expenses.items():
    table.append([category, values["count"], values["total"]])
    total_count += values["count"]
    total_sum += values["total"]

table.append(["TOTAL", total_count, total_sum])

print(tabulate(
    table,
    headers=["category", "count", "total"],
    tablefmt="github",
    floatfmt=".2f"
))