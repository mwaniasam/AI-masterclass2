import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -1.1026,
    "longitude": 37.0132,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    current = data.get("current", {})
    units = data.get("current_units", {})

    # Replace ISO standard delimiter with a space for readability
    raw_time = current.get("time", "N/A")
    readable_time = raw_time.replace("T", " ") if "T" in raw_time else raw_time

    temperature = current.get("temperature_2m", "N/A")
    temp_unit = units.get("temperature_2m", "°C")

    humidity = current.get("relative_humidity_2m", "N/A")
    humidity_unit = units.get("relative_humidity_2m", "%")

    wind_speed = current.get("wind_speed_10m", "N/A")
    wind_unit = units.get("wind_speed_10m", "km/h")

    print("\n" + "=" * 45)
    print("        CURRENT WEATHER REPORT: JUJA        ")
    print("=" * 45)
    print(f" Recorded At   : {readable_time}")
    print(f" Temperature   : {temperature:.1f} {temp_unit}")
    print(f" Humidity      : {humidity} {humidity_unit}")
    print(f" Wind Speed    : {wind_speed:.1f} {wind_unit}")
    print("=" * 45 + "\n")
else:
    print(f"Failed to fetch weather data. Status: {response.status_code}")