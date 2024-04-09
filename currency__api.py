"""Program to convert currency using API"""

import requests
import os

api_key = os.environ['CRYPTO_API']
headers = {
    'Authorization': f'Bearer {api_key}'
}

user_input = str(input(
    "\n1. List of currencies and their symbols\n2. Change currencies\n3. Exit\n\nYour input: "))

if user_input == '1':
    symbols = requests.get("https://api.freecryptoapi.com/v1/getData?symbol=BTC+ETH@binance", headers=headers)

    dict_currency = symbols.json()['symbols']

    for currency in dict_currency:
        try:
            print("Currency Name: " + currency['currencyName'])
            print("Currency Symbol: " + currency['currencySymbol'])
            print("Currency ID: " + currency['id'] + "\n")
        except KeyError:
            print("Currency ID: " + currency['id'] + "\n")



if user_input == '2':
    from_currency = str(input("From Currency: ")).upper()
    to_currency = str(input("To Currency: ")).upper()
    currency_rate = f"{from_currency}_{to_currency}"
    currency_amount = int(input("Enter the amount: "))

    currencies_rate = requests.get(
        f"https://free.currconv.com/api/v7/convert?q={currency_rate}&compact=ultra&apiKey={api_key}")

    dict_converted = float(currencies_rate.json()[currency_rate])
    print(
        f"\nThe currency rate from {from_currency} to {to_currency} is {dict_converted} equivalent to 1")
    print(f"Converted Amount: {dict_converted*currency_amount}\n")


