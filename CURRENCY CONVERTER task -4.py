import requests

def get_exchange_rates():
    """
    Fetch exchange rates from an API.

    Returns:
        dict: A dictionary containing exchange rates.
    """
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

def convert_currency(amount, source_currency, target_currency, rates):
    """
    Convert currency based on exchange rates.

    Args:
        amount (float): The amount to be converted.
        source_currency (str): The source currency code.
        target_currency (str): The target currency code.
        rates (dict): A dictionary containing exchange rates.

    Returns:
        float: The converted amount.
    """
    if source_currency not in rates or target_currency not in rates:
        print("Invalid currency code!")
        return None

    source_rate = rates[source_currency]
    target_rate = rates[target_currency]

    converted_amount = amount * (target_rate / source_rate)
    return converted_amount

def display_currencies(rates):
    """
    Display available currencies.

    Args:
        rates (dict): A dictionary containing exchange rates.
    """
    print("Available currencies:")
    for currency in rates:
        print(currency)

def currency_converter():
    """
    Perform currency conversion based on user input.
    """
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

def main():
    """
    Main function to start the currency converter program.
    """
    print("Welcome to Currency Converter")
    currency_converter()

if __name__ == "__main__":
    main()



Instructions for API usage:

The currency converter uses the ExchangeRate-API to fetch live exchange rates. You can sign up for a free account at https://www.exchangerate-api.com/ to obtain an API key.
Once you have the API key, replace the URL in the get_exchange_rates function with the appropriate endpoint provided by ExchangeRate-API, along with your API key.
Ensure that you handle any errors that may occur during the API request, such as network issues or invalid responses.
Test the currency converter to ensure that it retrieves exchange rates correctly and performs accurate currency conversions.
