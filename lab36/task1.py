
import csv
import json
import os

print("Vlad Radchuk, IT-32")

input_file = "data/expenses.csv"
output_file = "data/expenses.json"

expenses = []

with open(input_file, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")

    for row in reader:
        expenses.append({
            "date": row["date"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "comment": row["comment"]
        })

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=2, ensure_ascii=False)

file_size = os.path.getsize(output_file)

print(f"records: {len(expenses)}")
print(f"saved: {output_file} ({file_size} bytes)")
