
import requests
import sys

try:
    if len(sys.argv) < 2:
        print("Вкажіть режим: connection, http або timeout")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "connection":
        requests.get("http://127.0.0.1:9999", timeout=10)
    elif mode == "http":
        response = requests.get("https://httpbin.org/status/404", timeout=10)
        response.raise_for_status()
    elif mode == "timeout":
        requests.get("https://bank.gov.ua", timeout=0.001)
    else:
        print("Невідомий режим")
        sys.exit(1)

except requests.RequestException as error:
    print("Помилка:", error, file=sys.stderr)
    sys.exit(1)
