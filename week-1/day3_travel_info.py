import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

weather_api_key = os.getenv("OPENWEATHER_API_KEY")
countries_api_key = os.getenv("RESTCOUNTRIES_API_KEY", "rc_live_demo")


def save_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\nData saved to {filename}")


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric"
    }
    response = requests.get(url, params=params, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None


def get_country_info(country_code):
    url = f"https://api.restcountries.com/countries/v5/codes.alpha_2/{country_code}"
    headers = {"Authorization": f"Bearer {countries_api_key}"}

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        payload = response.json()
        objects = payload.get("data", {}).get("objects", [])
        if objects:
            return objects[0]
    return None


def parse_currencies(raw_currencies):
    if isinstance(raw_currencies, list):
        return ", ".join(c.get("code", "") for c in raw_currencies if isinstance(c, dict) and c.get("code"))
    if isinstance(raw_currencies, dict):
        return ", ".join(raw_currencies.keys())
    return "N/A"


def run_tool():
    if not weather_api_key:
        print("Error: OPENWEATHER_API_KEY not found in .env file.")
        return

    print("Travel Weather Tool")
    print("-------------------")
    city = input("Enter a city name: ").strip()

    if not city:
        print("No city entered. Exiting.")
        return

    print(f"\nFetching data for {city}...")

    weather_data = get_weather(city)

    if not weather_data:
        print(f"Could not find weather data for '{city}'. Check the city name and try again.")
        return

    country_code = weather_data["sys"]["country"]
    country_data = get_country_info(country_code)

    print(f"\n=== {city.title()}, {country_code} ===")
    print(f"Temperature : {weather_data['main']['temp']}°C")
    print(f"Condition   : {weather_data['weather'][0]['description'].title()}")
    print(f"Humidity    : {weather_data['main']['humidity']}%")
    print(f"Wind        : {weather_data['wind']['speed']} m/s")

    if country_data:
        population = country_data.get("population", 0)
        region = country_data.get("region", "Unknown")
        currencies = parse_currencies(country_data.get("currencies", []))

        print("\n=== Country Info ===")
        print(f"Region      : {region}")
        print(f"Population  : {population:,}")
        print(f"Currency    : {currencies}")

    save_to_file(weather_data, f"{city.lower()}_weather.json")


if __name__ == "__main__":
    run_tool()