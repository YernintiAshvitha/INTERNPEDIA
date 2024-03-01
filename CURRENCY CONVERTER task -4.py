#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

# Function to fetch exchange rates from API
def get_exchange_rates():
    try:
        # API endpoint for exchange rates
        url = "https://api.exchangerate-api.com/v4/latest/USD"

        # Fetching exchange rates
        response = requests.get(url)
        data = response.json()

        return data["rates"]
    except requests.exceptions.RequestException as e:
        print("Error fetching exchange rates:", e)
        return None

# Function to convert currency
def convert_currency(amount, source_currency, target_currency, rates):
    if source_currency not in rates or target_currency not in rates:
        print("Invalid currency code!")
        return None

    source_rate = rates[source_currency]
    target_rate = rates[target_currency]

    converted_amount = amount * (target_rate / source_rate)
    return converted_amount

# Function to display available currencies
def display_currencies(rates):
    print("Available currencies:")
    for currency in rates:
        print(currency)

# Main function for currency conversion
def currency_converter():
    rates = get_exchange_rates()
    if not rates:
        return

    while True:
        print("\nCURRENCY CONVERTER MENU:")
        display_currencies(rates)

        source_currency = input("Enter source currency code: ").upper()
        if source_currency == "EXIT":
            print("Exiting...")
            break

        if source_currency not in rates:
            print("Invalid source currency code!")
            continue

        target_currency = input("Enter target currency code: ").upper()
        if target_currency not in rates:
            print("Invalid target currency code!")
            continue

        amount = input("Enter amount to convert: ")
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount!")
            continue

        converted_amount = convert_currency(amount, source_currency, target_currency, rates)
        if converted_amount is not None:
            print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")

# Main function to start the program
def main():
    print("Welcome to Currency Converter")
    currency_converter()

if __name__ == "__main__":
    main()


# In[ ]:




