"""
Book & Author Explorer CLI
--------------------------
Fetches book publication details and author biography by chaining two Open Library APIs.

Usage:
    python week-1/day3_exercise.py

Requirements:
    pip install requests
"""

import json
import requests


def save_to_file(data, filename):
    """Save combined dictionary data to a formatted local JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved full record to {filename}")


def search_book(title):
    """API Call 1: Search for a book by title and return the top match."""
    url = "https://openlibrary.org/search.json"
    params = {
        "q": title,
        "fields": "key,title,author_name,author_key,first_publish_year,edition_count",
        "limit": 1
    }
    headers = {"User-Agent": "MasterclassBookTool/1.0"}

    response = requests.get(url, params=params, headers=headers, timeout=10)
    if response.status_code == 200:
        docs = response.json().get("docs", [])
        if docs:
            return docs[0]
    return None


def get_author_details(author_key):
    """API Call 2: Fetch detailed author info using the author_key from Call 1."""
    url = f"https://openlibrary.org/authors/{author_key}.json"
    headers = {"User-Agent": "MasterclassBookTool/1.0"}

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None


def extract_bio(author_data):
    """Cleanly extract biography text whether Open Library returns a string or dict."""
    if not author_data:
        return "No biography available."
    bio = author_data.get("bio")
    if isinstance(bio, dict):
        bio = bio.get("value", "")
    if isinstance(bio, str) and bio.strip():
        clean_bio = bio.strip().replace("\r\n", " ").replace("\n", " ")
        return clean_bio[:280] + "..." if len(clean_bio) > 280 else clean_bio
    return "No biography available."


def run_tool():
    print("Book & Author Explorer")
    print("----------------------")
    query = input("Enter a book title: ").strip()

    if not query:
        print("\n[Input Error] Book title cannot be empty. Exiting.")
        return

    print(f"\nSearching for '{query}'...")

    try:
        # API Call 1: Get Book Info
        book = search_book(query)
        if not book:
            print(f"\n[Not Found] Could not find any books matching '{query}'.")
            return

        title = book.get("title", "Unknown Title")
        authors = book.get("author_name", ["Unknown Author"])
        author_name = authors[0]
        publish_year = book.get("first_publish_year", "N/A")
        editions = book.get("edition_count", 0)

        # API Call 2: Chain the author_key into the Authors API
        author_keys = book.get("author_key", [])
        author_data = None
        if author_keys:
            author_data = get_author_details(author_keys[0])

        birth_date = author_data.get("birth_date", "Unknown") if author_data else "Unknown"
        bio_summary = extract_bio(author_data)

        # Combine results from both API calls and save locally
        combined_data = {
            "query": query,
            "book": book,
            "author_details": author_data
        }
        safe_filename = f"{query.lower().replace(' ', '_')}_record.json"

        # Display clean output for non-technical user
        print("\n" + "=" * 50)
        print(f" BOOK SUMMARY: {title.upper()}")
        print("=" * 50)
        print(f" Author         : {author_name}")
        print(f" First Published: {publish_year}")
        print(f" Total Editions : {editions:,}")
        print("-" * 50)
        print(" AUTHOR PROFILE")
        print("-" * 50)
        print(f" Born           : {birth_date}")
        print(f" Biography      : {bio_summary}")
        print("=" * 50 + "\n")

        save_to_file(combined_data, safe_filename)

    except requests.exceptions.ConnectionError:
        print("\n[Network Error] Could not connect to the internet. Check your connection.")
    except requests.exceptions.Timeout:
        print("\n[Network Error] The request timed out. Please try again.")


if __name__ == "__main__":
    run_tool()