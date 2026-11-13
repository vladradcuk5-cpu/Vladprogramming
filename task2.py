
import csv
import requests
import sys

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
STUDENT = "Радчук Владислав"
GROUP = "ІТ-32"

def get_rate(currency):
    response = requests.get(
        URL,
        params={"valcode": currency, "json": ""},
        timeout=10
    )
    response.raise_for_status()
    data = response.json()
    return data[0]["rate"], data[0]["exchangedate"]

def test_error(mode):
    if mode == "connection":
        requests.get("http://127.0.0.1:9999", timeout=10)
    elif mode == "http":
        requests.get("https://httpbin.org/status/404", timeout=10).raise_for_status()
    elif mode == "timeout":
        requests.get("https://bank.gov.ua", timeout=0.001)

try:
    if len(sys.argv) > 1:
        test_error(sys.argv[1])
    else:
        total = 0

        with open("data/expenses.csv", "r", encoding="utf-8-sig") as file:
            lines = (line for line in file if line.strip())
            reader = csv.DictReader(lines, delimiter=";")

            for row in reader:
                total += float(row["amount"])

        usd_rate, date = get_rate("USD")
        eur_rate, _ = get_rate("EUR")

        print("Студент:", STUDENT)
        print("Група:", GROUP)
        print("Загальні витрати:", total, "UAH")
        print("Курс валют на:", date)
        print("У доларах:", round(total / usd_rate, 2), "USD")
        print("У євро:", round(total / eur_rate, 2), "EUR")

except requests.RequestException as error:
    print("Помилка:", error, file=sys.stderr)
    sys.exit(1)
except (OSError, ValueError, KeyError, IndexError) as error:
    print("Помилка:", error, file=sys.stderr)
    sys.exit(1)
