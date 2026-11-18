import os
import requests


def load_dotenv(path=".env"):
    """Load simple KEY=VALUE entries from a .env file."""
    if not os.path.exists(path):
        return

    with open(path, encoding="utf-8") as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)

load_dotenv()

api_key = os.getenv("EXCHANGE_RATE_KEY")

if not api_key:
    print("\n[Configuration Error] EXCHANGE_RATE_KEY not found in .env.")
    exit(1)

base_currency = input("Enter base currency (e.g. USD, EUR, KES): ").strip().upper()

if not base_currency:
    print("\n[Input Error] Base currency code cannot be empty.")
    exit(1)

# Endpoint: https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        rates = data.get("conversion_rates", {})
        update_time = data.get("time_last_update_utc", "N/A")

        target_currencies = ["USD", "EUR", "GBP", "KES", "JPY"]

        print("\n" + "=" * 42)
        print(f"     EXCHANGE RATES (BASE: {base_currency})")
        print("=" * 42)
        print(f" Last Updated: {update_time}")
        print("-" * 42)

        for target in target_currencies:
            if target != base_currency and target in rates:
                print(f" 1 {base_currency} = {rates[target]:>10.2f} {target}")

        print("=" * 42 + "\n")

    elif response.status_code == 401 or response.status_code == 403:
        print(f"\n[Error {response.status_code}] Unauthorized: Check your API key in .env.")

    elif response.status_code == 404:
        print(f"\n[Error 404] Currency code '{base_currency}' not found.")

    else:
        print(f"\n[Error {response.status_code}] API returned an unexpected response.")

except requests.exceptions.ConnectionError:
    print("\n[Network Error] Connection failed. Check your network.")
except requests.exceptions.Timeout:
    print("\n[Network Error] Request timed out.")