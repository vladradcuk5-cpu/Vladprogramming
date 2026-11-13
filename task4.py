
import json
from datetime import date

print("Vladyslav Radchuk, IT-32")

data = {
    "owner": "Vladyslav Radchuk",
    "date": date.today()
}

try:
    json.dumps(data)
except TypeError as error:
    print("TypeError:", error)

def date_default(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("Unsupported type")

with open("date1.json", "w", encoding="utf-8") as file:
    json.dump(data, file, default=date_default, indent=2)

with open("date1.json", "r", encoding="utf-8") as file:
    result = json.load(file)

result["date"] = date.fromisoformat(result["date"])

print("Method 1:", result == data)
print("Date type:", type(result["date"]))

def convert_to_string(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {key: convert_to_string(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [convert_to_string(value) for value in obj]
    return obj

def convert_to_date(obj):
    if isinstance(obj, dict):
        return {key: convert_to_date(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [convert_to_date(value) for value in obj]
    return obj

with open("date2.json", "w", encoding="utf-8") as file:
    json.dump(convert_to_string(data), file, indent=2)

with open("date2.json", "r", encoding="utf-8") as file:
    result = json.load(file)

result["date"] = date.fromisoformat(result["date"])

print("Method 2:", result == data)
print("Date type:", type(result["date"]))
