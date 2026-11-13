
import requests
import sys

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
params = {"json": ""}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("Статус відповіді:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Кількість валют:", len(data))

    for currency in data:
        if currency["cc"] in ["USD", "EUR"]:
            print(
                currency["cc"],
                currency["txt"],
                currency["rate"],
                currency["exchangedate"]
            )

except requests.RequestException as error:
    print("Помилка:", error, file=sys.stderr)
    sys.exit(1)
