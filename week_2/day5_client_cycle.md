# Phase II - Week 2 - Day 10: The Full Client Cycle

Track B: Data Analyst  
Project: Kiambu Dairy Co-op Price Checker  
Budget: KES 8,000  
Timeline: 3 Working Days (Targeted by End of Week)  
Status: Delivered and Tagged `v1.0`  

---

## Stage 1: Read and Analyse the Brief

### 1. The Problem
A small dairy cooperative in Kiambu with approximately 30 farmer members currently spends excessive administrative time each week calling or messaging each farmer individually on WhatsApp to share the fluctuating buying price per litre. They lack a self-service or local tool that allows farmers and staff to instantly calculate total payout amounts based on daily milk delivery volumes.

### 2. The Deliverable
A simple, reliable, standalone computer program that takes a farmer's name and milk volume in litres as inputs, looks up the current weekly buying price, and outputs the exact total payment owed to the farmer.

### 3. The Deadline
End of the current week (approximately 3 to 4 working days from kickoff).

### 4. What Is Unclear in the Brief
- **Price Storage**: Where does the weekly price live, and how is it updated? (Text file, spreadsheet cell, hardcoded script variable, or database?)
- **User Interface**: What hardware or platform will run the program? (Office desktop, terminal script, or mobile?)
- **Historical Records**: Does the tool only compute on-the-spot totals, or is there an expectation to persist a delivery history log for monthly payroll?
- **Member Validation**: Does the co-op maintain a pre-approved list of 30 farmer names/member IDs, or can any name be typed in?

---

## Stage 2: Clarifying Question and Stated Assumption

### 1. The One Clarifying Question
> "Where does your weekly buying price currently live, and who updates it? If someone types it in manually once a week, I can have the program read it from a simple, editable text file (`price.txt`) on your computer so you can change the rate in seconds without editing any code."

### 2. Assumption Stated in the Proposal
> "I assume the weekly buying price will be stored in a simple, editable text file (`price.txt`) on the co-op's computer. If the price must be fetched from an external spreadsheet, database, or cloud service, the timeline extends by 1 working day."

---

## Stage 3: The Winning Proposal (Under 200 Words)

You are spending valuable hours each week calling and messaging 30 farmers with fluctuating milk rates. I will build a simple, standalone calculator that lets any farmer enter their name and litres supplied to instantly see their total payout at the current weekly price.

I assume the manager updates the weekly price in a simple text file (`price.txt`). If it must sync from an external database, the timeline extends by 1 working day.

Approach: A lightweight Python tool that reads the active rate from `price.txt`, validates milk volume, computes the payout, and displays a clear summary.

Deliverables:
- Standalone Python calculator script
- `price.txt` configuration file for zero-code weekly rate updates
- Plain-English setup guide and README
- 15-minute handover call

Price and timeline: KES 8,000. Delivered in 3 working days from receiving the deposit. Payment terms: 50% upfront (KES 4,000), 50% upon delivery confirmation.

Where is the computer located that farmers will use to check their totals?

*(Word count: 158 words)*

---

## Stage 4: Built Deliverables & Automated Testing

The deliverable was built in [`week_2/dairy_calculator/`](file:///home/mwaniasamuel/AI-masterclass2/week_2/dairy_calculator/):
- [`dairy_calculator.py`](file:///home/mwaniasamuel/AI-masterclass2/week_2/dairy_calculator/dairy_calculator.py): Core calculation engine and command-line interface.
- [`price.txt`](file:///home/mwaniasamuel/AI-masterclass2/week_2/dairy_calculator/price.txt): Decoupled configuration file containing the active rate (`55.0`).
- [`README.md`](file:///home/mwaniasamuel/AI-masterclass2/week_2/dairy_calculator/README.md): Client documentation.

### Test Results Matrix

| Test Case | Inputs | Expected Output | Status |
|:---|:---|:---|:---:|
| Normal delivery | Name: John Kamau, Litres: 25.5 | KES 1,402.50 at KES 55.00/litre | Passed |
| High volume delivery | Name: Mary Wanjiku, Litres: 60.0 | KES 3,300.00 at KES 55.00/litre | Passed |
| Fractional volume | Name: Peter Njoroge, Litres: 14.2 | KES 781.00 at KES 55.00/litre | Passed |
| Non-numeric input | Name: Grace Muthoni, Litres: `abc` | Friendly error: enter a valid number | Passed |
| Negative volume | Name: David Mwangi, Litres: `-10` | Error: must be greater than zero | Passed |
| Blank name | Name: `""` | Error: Farmer name is required | Passed |

---

## Stage 5: Package and Deliver

### Code Cleanup Audit
- Removed all debug statements and temporary print calls.
- Decoupled `price.txt` path handling using `pathlib.Path` so the script can be executed from any directory.
- Implemented graceful fallback: defaults to `KES 55.00` if `price.txt` is missing.
- Verified zero external dependencies (pure Python standard library).

### Delivery Message to Client

**Subject:** Delivery: Kiambu Dairy Co-op Payment Calculator (v1.0)

Hello [Manager Name],

The payment calculator for Kiambu Dairy Co-op is ready for handover. Here is a summary of what was delivered:

- A lightweight Python calculator script (`dairy_calculator.py`) that instantly computes milk payouts for your 30 member farmers
- A separate `price.txt` file that allows you to update the weekly buying rate in seconds without touching any code
- Built-in validation that prevents typos, negative numbers, or missing names
- A clear setup guide and README with full operating instructions

To run the calculator on your office computer:
1. Open the terminal and navigate to the project directory: `cd week_2/dairy_calculator`
2. Run: `python3 dairy_calculator.py`
3. Enter the farmer's name and litres delivered to view the payment summary.

To change next week's price, open `price.txt` in Notepad, update the number (e.g. `58.0`), and save.

This completes all deliverables agreed in the brief. Please test it with your staff over the next two business days. If everything meets your expectations, please reply confirming your approval and send the remaining 50% balance (KES 4,000) to M-Pesa.

Please let me know if you have any questions.

---

## Stage 6: Scope Management - Handling the Revision Request

### The Client's Request
> *"This is great! Can we also add a feature where it keeps a log of every farmer's payment so we can see the history at the end of the month?"*

### Evaluation
- **Classification**: **New Feature (Out of Scope)**.
- **Rationale**: The original brief specified a simple on-the-spot calculator without persistent database storage, reporting, or export functionality. A monthly payment ledger requires file appending, timestamping, data modeling (e.g. CSV logging), and aggregation views, which were not priced into the KES 8,000 quote.

### Professional Client Response
> "Hello [Manager Name], that is a great idea and a very natural next step for the co-op's payroll workflow. Adding an automated monthly delivery log with timestamps and exportable history was not part of the initial calculator brief, so it falls under a separate feature add-on.
> 
> Everything in our original agreement is working as delivered. Let us complete the sign-off and balance payment for this calculator milestone first. Once that is wrapped up, I can scope and quote the monthly ledger add-on for KES 4,500 with a 2-day delivery. Ready for sign-off on the current tool when you are."

---

## Technical Addendum: Track B Day 10 Live Exchange Rate Tracker

In addition to the simulated client cycle, Track B requires building an automated script that queries a live financial API.

- **Source Code**: [`week_2/exchange_rate_tracker.py`](file:///home/mwaniasamuel/AI-masterclass2/week_2/exchange_rate_tracker.py)
- **API Endpoint**: `https://open.er-api.com/v6/latest/USD`
- **Error Handling**: Wrapped in `try...except` catching `urllib.error.URLError`, `json.JSONDecodeError`, and general exceptions.

### Live Output
```
==================================================
         LIVE EXCHANGE RATE TRACKER (USD/KES)
==================================================
API Source       : open.er-api.com
Last Updated UTC : Fri, 23 Oct 2026 00:02:31 +0000
Current Rate     : 1 USD = KES 129.87
--------------------------------------------------
CONVERSIONS (KES to USD)
--------------------------------------------------
  KES  10,000  ->  $   77.00 USD
  KES  50,000  ->  $  385.01 USD
  KES 100,000  ->  $  770.02 USD
==================================================
```
