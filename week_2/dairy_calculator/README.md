# Kiambu Dairy Co-op Payment Calculator

A lightweight, standalone command-line application built for the Kiambu Dairy Cooperative to quickly calculate daily milk payout amounts for its 30 member farmers based on a fluctuating weekly buying rate.

---

## Overview

The cooperative manager updates the milk buying rate once a week. When farmers deliver milk, the clerk or manager enters the farmer's name and volume in litres. The calculator instantly computes and displays the exact payout amount due, eliminating manual arithmetic and reducing inquiry phone calls.

---

## Project Structure

```
dairy_calculator/
|-- dairy_calculator.py  # Main interactive payment calculator script
|-- price.txt            # Current buying rate per litre (updated weekly)
\-- README.md            # Setup, configuration, and operating instructions
```

---

## Requirements

- Python 3.8 or higher.
- Built strictly with Python standard library. No external package installation required.

---

## Quick Start & Usage

1. Open your terminal and navigate to the project directory:
   ```bash
   cd week_2/dairy_calculator
   ```

2. Run the calculator:
   ```bash
   python3 dairy_calculator.py
   ```

3. Follow the on-screen prompts:
   - Type the farmer's name and press `Enter`.
   - Type the number of litres supplied and press `Enter`.

---

## How to Update the Weekly Buying Price

The co-op manager can update the weekly buying rate without modifying any Python code:

1. Open `price.txt` in any text editor (Notepad, TextEdit, Nano, VS Code).
2. Replace the number with the new rate (for example, `58.50`).
3. Save the file.
4. The next time `dairy_calculator.py` runs, it will automatically load and use the new rate.

If `price.txt` is accidentally moved or deleted, the application falls back safely to a default baseline rate of `KES 55.00/litre`.

---

## Sample Execution

```
============================================
  Kiambu Dairy Co-op Payment Calculator
============================================
Current buying price: KES 55.00 per litre

Enter farmer name: John Kamau
Enter litres supplied today: 25.5

--------------------------------------------
PAYMENT SUMMARY
--------------------------------------------
Farmer Name : John Kamau
Volume      : 25.5 litres
Rate        : KES 55.00 per litre
Total Owed  : KES 1,402.50
============================================
```

---

## Error Handling

The application validates user input cleanly:
- Empty farmer names trigger: `Error: Farmer name is required.`
- Non-numeric inputs for volume trigger: `Error: Please enter a valid number for litres.`
- Zero or negative litres trigger: `Error: Litres supplied must be greater than zero.`
