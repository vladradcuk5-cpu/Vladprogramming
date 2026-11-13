
import json
import requests
import sys
import os
import time
from datetime import datetime

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_DIR = "cache"
CACHE_FILE = os.path.join(CACHE_DIR, "rates.json")
CACHE_TIME = 3600

def get_rates():
    os.makedirs(CACHE_DIR, exist_ok=True)

    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as file:
            cache = json.load(file)

        age = time.time() - cache["timestamp"]

        if age < CACHE_TIME:
            print("Джерело даних: кеш")
            print("Вік кешу:", round(age), "секунд")
            return cache["data"]

    response = requests.get(
        URL,
        params={"json": ""},
        timeout=10
    )
    response.raise_for_status()

    data = response.json()

    cache = {
        "timestamp": time.time(),
        "retrieved_at": datetime.now().isoformat(),
        "data": data
    }

    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump(cache, file, ensure_ascii=False, indent=4)

    print("Джерело даних: API")
    print("Кеш оновлено:", cache["retrieved_at"])

    return data

try:
    rates = get_rates()

    for currency in rates:
        if currency["cc"] in ["USD", "EUR"]:
            print(
                currency["cc"],
                currency["rate"],
                currency["exchangedate"]
            )

except (requests.RequestException, OSError, ValueError, KeyError) as error:
    print("Помилка:", error, file=sys.stderr)
    sys.exit(1)
