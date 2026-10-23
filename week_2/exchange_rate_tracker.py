"""Live Exchange Rate Tracker.

Fetches real-time USD/KES exchange rates from the open.er-api.com API,
displays the active rate, and computes USD equivalents for benchmark KES amounts.
"""

import json
import urllib.request

API_URL = "https://open.er-api.com/v6/latest/USD"
BENCHMARK_AMOUNTS_KES = [10000, 50000, 100000]


def fetch_usd_to_kes_rate(url=API_URL, timeout=10):
    """Fetches the latest USD to KES conversion rate from the exchange rate API."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (ExchangeRateTracker/1.0)"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP request failed with status {response.status}")
        data = json.loads(response.read().decode("utf-8"))

    if "rates" not in data or "KES" not in data["rates"]:
        raise KeyError("KES rate not found in API response.")

    return float(data["rates"]["KES"]), data.get("time_last_update_utc", "N/A")


def run():
    """Executes the exchange rate fetch and currency conversions."""
    print("=" * 50)
    print("         LIVE EXCHANGE RATE TRACKER (USD/KES)")
    print("=" * 50)

    try:
        kes_rate, last_updated = fetch_usd_to_kes_rate()

        print(f"API Source       : open.er-api.com")
        print(f"Last Updated UTC : {last_updated}")
        print(f"Current Rate     : 1 USD = KES {kes_rate:,.2f}")
        print("-" * 50)
        print("CONVERSIONS (KES to USD)")
        print("-" * 50)

        for kes in BENCHMARK_AMOUNTS_KES:
            usd = kes / kes_rate
            print(f"  KES {kes:>7,d}  ->  ${usd:>8,.2f} USD")

        print("=" * 50)

    except urllib.error.URLError as e:
        print(f"Network Error: Unable to reach exchange rate API: {e}")
    except json.JSONDecodeError:
        print("Parsing Error: Received malformed JSON from API endpoint.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    run()
