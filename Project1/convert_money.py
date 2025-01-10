import json


def load_exchange_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def convert_matauang(amount, from_currency, to_currency, exchange_data):
    rates = exchange_data["conversion_rates"]
    if from_currency not in rates or to_currency not in rates:
        return None
    return amount / rates[from_currency] * rates[to_currency]
    
file_path = "database_currency.json"
exchange_data = load_exchange_data(file_path)


def main_convert():
    while(True):
        amount = float(input("masukkan jumlah uang : "))
        from_currency = input("masukan mata uang asal : ")
        to_currency = input("Masukan mata uang tujuan : ")

        hasil = convert_matauang(amount, from_currency, to_currency, exchange_data)
        if hasil is not None:
            print(f"{amount} {from_currency} = {hasil:.2f} {to_currency}")
        else:
            print("Mata uang tidak ditemukan.")

        opsi = input("selesai convert (y/n): ")
        if opsi == "y" or opsi == "Y":
            break
        
    
