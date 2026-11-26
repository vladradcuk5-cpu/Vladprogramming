
import json
import requests
import sys
import time
from pathlib import Path

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_DIR = Path("cache")
CACHE_FILE = CACHE_DIR / "rates.json"
CACHE_TIME = 3600


def get_rates():
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as file:
                cache = json.load(file)

            age = time.time() - cache["timestamp"]

            if 0 <= age < CACHE_TIME:
                print(f"source: cache (age {int(age)} s)")
                return cache["rates"]

        except (OSError, json.JSONDecodeError, KeyError, TypeError):
            pass

    response = requests.get(
        URL,
        params={"json": ""},
        timeout=10
    )
    response.raise_for_status()

    rates = response.json()

    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    cache = {
        "timestamp": time.time(),
        "rates": rates
    }

    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump(cache, file, ensure_ascii=False, indent=4)

    print("source: api (cache saved)")
    return rates


def main():
    try:
        print("Vlad Radchuk, IT-32")

        rates = get_rates()

        for code in ("USD", "EUR"):
            currency = next(
                item for item in rates
                if item["cc"] == code
            )

            print(
                f'{code}: {currency["rate"]} UAH, '
                f'date: {currency["exchangedate"]}'
            )

    except requests.RequestException as error:
        print(f"Network error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
