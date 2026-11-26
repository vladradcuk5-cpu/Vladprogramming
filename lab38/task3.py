
import requests
import sys

URL = "https://api.open-meteo.com/v1/forecast"

CITY = "Lutsk"
LATITUDE = 50.75
LONGITUDE = 25.34


def main():
    try:
        response = requests.get(
            URL,
            params={
                "latitude": LATITUDE,
                "longitude": LONGITUDE,
                "current": "temperature_2m,wind_speed_10m"
            },
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        current = data["current"]
        units = data["current_units"]

        print("Vlad Radchuk, IT-32")
        print(
            f'{CITY} ({LATITUDE}, {LONGITUDE}): '
            f'{current["temperature_2m"]} '
            f'{units["temperature_2m"]}, '
            f'wind {current["wind_speed_10m"]} '
            f'{units["wind_speed_10m"]}'
        )

    except requests.RequestException as error:
        print(f"Network error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
