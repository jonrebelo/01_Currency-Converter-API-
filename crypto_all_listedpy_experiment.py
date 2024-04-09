import requests
import os
import time
from pprint import pprint
from tqdm import tqdm  # import the tqdm module

api_key = os.environ['CRYPTO_API']
headers = {
    'Authorization': f'Bearer {api_key}'
}

response = requests.get("https://api.freecryptoapi.com/v1/getCryptoList", headers=headers)
response_json = response.json()

# Check if the request was successful
if 'result' in response_json:
    for symbol in response_json['result']:
        print(f"{symbol['symbol']}")
else:
    print("No symbols in response.")