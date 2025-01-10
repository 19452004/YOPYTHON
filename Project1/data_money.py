import requests
import json

base_currency = "IDR"
url = f'https://v6.exchangerate-api.com/v6/54d01aa0ad2b6b390fb0c7b2/latest/{base_currency}'

respons = requests.get(url)
data = respons.json()

output_file = 'database_currency.json'

with open(output_file, 'w') as file:
    json.dump(data, file, indent = 4)    