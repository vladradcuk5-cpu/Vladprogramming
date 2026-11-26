
import requests
import sys

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def main():
    try:
        response = requests.get(
            URL,
            params={"json": ""},
            timeout=10
        )
        response.raise_for_status()

        rates = response.json()

        print("Vlad Radchuk, IT-32")
        print("status:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type"))
        print("currencies:", len(rates))

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
