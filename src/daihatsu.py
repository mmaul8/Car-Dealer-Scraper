import csv
import requests

def fetch_dealer_data(d):
    url = f'https://daihatsu.co.id/api/dealers?regencyId={d}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data for regencyId {d}: {e}")
        return None

def process_entry(entry, writer):
    if isinstance(entry, dict):
        name = entry.get('name', 'N/A')
        address = entry.get('address', 'N/A')
        phone = entry.get('phone', 'N/A')

        writer.writerow({
            'Dealer Name': name,
            'Address': address,
            'Phone': phone,
        })

def car_daihatsu():
    with open('dealer_daihatsu.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fields = ['Dealer Name', 'Address', 'Phone']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for d in range(1, 420):
            data = fetch_dealer_data(d)

            if data:
                for entry in data:
                    process_entry(entry, writer)

if __name__ == "__main__":
    car_daihatsu()
