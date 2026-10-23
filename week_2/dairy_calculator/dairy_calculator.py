"""Kiambu Dairy Co-op Payment Calculator.

Reads the current milk buying price from price.txt, accepts farmer deliveries,
and calculates the total payout amount owed.
"""

from pathlib import Path

PRICE_FILE = Path(__file__).parent / "price.txt"
DEFAULT_PRICE = 55.0


def get_current_price(file_path=PRICE_FILE, default=DEFAULT_PRICE):
    """
    Reads the current buying price per litre from price.txt.
    Falls back to default price if file is missing or invalid.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            return float(content)
    except (FileNotFoundError, ValueError):
        return default


def calculate_payment(litres, price_per_litre):
    """Calculates total payment for given litres and price per litre."""
    return round(litres * price_per_litre, 2)


def run():
    """Runs the interactive dairy calculator terminal session."""
    price = get_current_price()

    print("=" * 44)
    print("  Kiambu Dairy Co-op Payment Calculator")
    print("=" * 44)
    print(f"Current buying price: KES {price:.2f} per litre\n")

    name = input("Enter farmer name: ").strip()
    if not name:
        print("Error: Farmer name is required.")
        return

    try:
        litres = float(input("Enter litres supplied today: ").strip())
        if litres <= 0:
            print("Error: Litres supplied must be greater than zero.")
            return
    except ValueError:
        print("Error: Please enter a valid number for litres.")
        return

    total = calculate_payment(litres, price)

    print("\n" + "-" * 44)
    print("PAYMENT SUMMARY")
    print("-" * 44)
    print(f"Farmer Name : {name}")
    print(f"Volume      : {litres:,.1f} litres")
    print(f"Rate        : KES {price:.2f} per litre")
    print(f"Total Owed  : KES {total:,.2f}")
    print("=" * 44)


if __name__ == "__main__":
    run()
