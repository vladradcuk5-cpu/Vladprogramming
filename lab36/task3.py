
import json
import sys

print("Vlad Radchuk, IT-32")

settings_file = "settings.json"
expenses_file = "data/expenses.json"

default_settings = {
    "owner": "Vlad Radchuk",
    "group": "IT-32",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

# Перевірка наявності файлу налаштувань
try:
    with open(settings_file, "r", encoding="utf-8") as file:
        settings = json.load(file)

except FileNotFoundError:
    with open(settings_file, "w", encoding="utf-8") as file:
        json.dump(default_settings, file, indent=2, ensure_ascii=False)

    print("settings.json not found, default created")
    sys.exit(0)

except json.JSONDecodeError as error:
    print(
        f"JSON error on line {error.lineno}: {error.msg}",
        file=sys.stderr
    )
    sys.exit(1)

# Читання витрат
with open(expenses_file, "r", encoding="utf-8") as file:
    expenses = json.load(file)

spent = sum(item["amount"] for item in expenses)
limit = settings["monthly_limit"]
left = limit - spent

print(f"owner: {settings['owner']}")
print(f"group: {settings['group']}")
print(f"currency: {settings['currency']}")
print(f"categories: {settings['categories']}")
print(f"limit: {limit:.2f} UAH, spent: {spent:.2f} UAH, left: {left:.2f} UAH")
