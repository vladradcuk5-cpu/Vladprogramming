
import requests
import sys

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 50.7472,
    "longitude": 25.3254,
    "current": "temperature_2m,wind_speed_10m"
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data["current"]

    print("Місто: Луцьк")
    print("Координати: 50.7472, 25.3254")
    print("Температура:", current["temperature_2m"], "°C")
    print("Швидкість вітру:", current["wind_speed_10m"], "км/год")

except (requests.RequestException, KeyError, ValueError) as error:
    print("Помилка:", error, file=sys.stderr)
    sys.exit(1)
