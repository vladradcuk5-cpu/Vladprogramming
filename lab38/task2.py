
import csv
import requests
import sys
from decimal import Decimal

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def get_rate(currency, url=URL, timeout=10):
    response = requests.get(
        url,
        params={"valcode": currency, "json": ""},
        timeout=timeout
    )
    response.raise_for_status()

    data = response.json()
    return Decimal(str(data[0]["rate"])), data[0]["exchangedate"]


def main():
    try:
        total = Decimal("0")

        with open("data/expenses.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                total += Decimal(row["amount"])

        usd_rate, usd_date = get_rate("USD")
        eur_rate, eur_date = get_rate("EUR")

        print("Vlad Radchuk, IT-32")
        print("rate date:", usd_date)
        print(f"total: {total:.2f} UAH")
        print(f"= {total / usd_rate:.2f} USD")
        print(f"= {total / eur_rate:.2f} EUR")

    except requests.RequestException as error:
        print(f"Network error: {error}", file=sys.stderr)
        sys.exit(1)


def test_error(error_type):
    try:
        if error_type == "connection":
            requests.get(
                "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange",
                timeout=10
            ).close()
            raise requests.ConnectionError("Simulated connection error")

        elif error_type == "http":
            get_rate("USD", url="https://bank.gov.ua/nonexistent-path")

        elif error_type == "timeout":
            get_rate("USD", timeout=0.001)

    except requests.ConnectionError:
        print("ConnectionError: Internet connection unavailable",
              file=sys.stderr)
        sys.exit(1)

    except requests.Timeout:
        print("Timeout: Request timed out", file=sys.stderr)
        sys.exit(1)

    except requests.HTTPError as error:
        print(f"HTTPError: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_error(sys.argv[1])
    else:
        main()
