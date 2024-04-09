"""Program to convert currency using API"""

import requests
import os
import time
from pprint import pprint
from tqdm import tqdm  # import the tqdm module

api_key = os.environ['CRYPTO_API']
headers = {
    'Authorization': f'Bearer {api_key}'
}
user_input = str(input(
    "\n1. List of currencies and their symbols\n2. Change currencies\n3. Exit\n\nYour input: "))

if user_input == '1':
    exchange = 'binance'  # specify the exchange
    page = 1
    dict_currency = {}

    while True:
        response = requests.get(f"https://api.freecryptoapi.com/v1/getExchange?exchange={exchange}&page={page}", headers=headers)
        response_json = response.json()

        # If no symbols are returned, break the loop
        if not response_json['symbols']:
            break

        # Add the symbols from this page to the dictionary
        dict_currency.update({item['symbol']: item['last'] for item in response_json['symbols']})

        # Print the dictionary with a 3-second delay between each iteration
        for symbol, last in tqdm(dict_currency.items()):
            print(f"{symbol}: {last}")
            time.sleep(3)

        # Go to the next page
        page += 1