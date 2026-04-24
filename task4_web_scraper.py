# Task 4: Basic Web Scraper

import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    try:
        url = input("Enter website URL: ").strip()

        if not url.startswith("http"):
            raise ValueError("Invalid URL format")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Request Error:", e)
            return

        try:
            soup = BeautifulSoup(response.text, "html.parser")
        except Exception as e:
            print("Parsing Error:", e)
            return

        headlines = []

        for tag in ["h1", "h2", "h3"]:
            for item in soup.find_all(tag):
                text = item.get_text(strip=True)
                if text and len(text) > 20:
                    headlines.append(text)

        for item in soup.find_all("span", class_="titleline"):
            text = item.get_text(strip=True)
            if text:
                headlines.append(text)

        if not headlines:
            for link in soup.find_all("a"):
                text = link.get_text(strip=True)
                if text and len(text) > 30:
                    headlines.append(text)

        headlines = list(dict.fromkeys(headlines))

        if not headlines:
            print("No headlines found.")
        else:
            print("\nHeadlines:\n")
            for i, h in enumerate(headlines[:10], start=1):
                print(f"{i}. {h}")

    except ValueError as ve:
        print("Value Error:", ve)
    except Exception as e:
        print("Unexpected Error:", e)

if __name__ == "__main__":
    scrape_headlines()