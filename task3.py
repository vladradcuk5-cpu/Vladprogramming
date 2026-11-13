
import json
import os
import sys

print("Vladyslav Radchuk, IT-32")

if not os.path.exists("settings.json"):
    settings = {
        "owner": "Vladyslav Radchuk",
        "group": "IT-32",
        "currency": "UAH",
        "monthly_limit": 6000,
        "categories": ["Food", "Transport", "Entertainment", "Education"]
    }

    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=2, ensure_ascii=False)

    print("settings.json not found, default created")
    sys.exit(0)

try:
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)

except json.JSONDecodeError as error:
    print("JSON error at line:", error.lineno, file=sys.stderr)
    sys.exit(1)

with open("data/expenses.json", "r", encoding="utf-8") as file:
    expenses = json.load(file)

spent = sum(item["amount"] for item in expenses)
limit = settings["monthly_limit"]
left = limit - spent

print("owner:", settings["owner"])
print("group:", settings["group"])
print("currency:", settings["currency"])
print("categories:", settings["categories"])
print(f"limit: {limit:.2f} UAH, spent: {spent:.2f} UAH, left: {left:.2f} UAH")
