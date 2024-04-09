"""Program to convert cryptocurrency using API"""

import requests
import os


api_key = os.environ['CRYPTO_API']
headers = {'Authorization': f'Bearer {api_key}'}
user_input = str(input(
    "\n1. List of top 10 Cryptocurrencies and current USD Price\n2. Convert Currencies\n3. Exit\n\nYour input: "))

while user_input == "1" or "2":
    if user_input == '1':
        symbols = ['BTC', 'USDT', 'ETH', 'SOL', 'BNB', 'XRP', 'DOGE', 'ADA',  'SHIB', 'TON']

        # Create the symbol parameter for the GET request
        symbol_param = '+'.join(symbols)

        # Make the GET request
        response = requests.get(f"https://api.freecryptoapi.com/v1/getData?symbol={symbol_param}", headers=headers)

        # Check the status of the response
        if response.status_code == 200:
            # Parse the JSON response
            response_json = response.json()

            # Check if 'symbols' key exists in the response
            if 'symbols' in response_json:
                # Print the current prices
                for symbol_data in response_json['symbols']:
                    print(f"{symbol_data['symbol']}: {symbol_data['last']}")
            else:
                print("The key 'symbols' does not exist in the response.")
        else:
            print(f"Request failed with status code {response.status_code}")
        user_input = str(input(
        "\n1. List of top 10 Cryptocurrencies and current USD Price\n2. Convert Currencies\n3. Exit\n\nYour input: "))
    if user_input == '2':
        from_currency = str(input("From Currency: ")).upper()
        to_currency = str(input("To Currency: ")).upper()
        currency_rate = f"{from_currency}_{to_currency}"
        currency_amount = int(input("Enter the amount: "))

        currencies_rate = requests.get(
        f"https://api.freecryptoapi.com/v1/getConversion?from={from_currency}&to={to_currency}&amount={currency_amount}", headers=headers)

        # Then try to access the 'result' key
        dict_converted = float(currencies_rate.json()["result"])
        print(f"{dict_converted} {to_currency}")
        user_input = str(input(
        "\n1. List of top 10 Cryptocurrencies and current USD Price\n2. Convert Currencies\n3. Exit\n\nYour input: "))

    if user_input == '3':
        print("Exiting...\n")
        break    

    if user_input not in ["1", "2", "3"]:
        print("Invalid entry, try again")
        user_input = str(input(
        "\n1. List of top 10 Cryptocurrencies and current USD Price\n2. Convert Currencies\n3. Exit\n\nYour input: "))


