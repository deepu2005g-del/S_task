# Task 5: Currency Converter

import requests

def currency_converter():
    try:
        base = input("Enter base currency : ").upper().strip()
        target = input("Enter target currency : ").upper().strip()

        if len(base) != 3 or len(target) != 3:
            print("Currency codes must be 3 letters")
            return

        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")
        except ValueError:
            print("Invalid amount")
            return

        url = f"https://api.exchangerate-api.com/v4/latest/{base}"

        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 404:
                print(f"Invalid base currency: {base}")
                return

            response.raise_for_status()
            data = response.json()

        except requests.exceptions.RequestException as e:
            print("API Request Error:", e)
            return

        rates = data.get("rates")

        if not rates or target not in rates:
            print(f"Invalid target currency: {target}")
            return

        result = amount * rates[target]

        print(f"\n {amount} {base} = {result:.2f} {target}")

    except Exception as e:
        print("Unexpected Error:", e)

if __name__ == "__main__":
    currency_converter()