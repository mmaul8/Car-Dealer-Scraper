import csv
import requests

def car_wuling():
    url = 'https://www2.wuling.id/api/dealers?type=all'

    w = requests.get(url)
    data = w.json()

    with open('wuling_dealers.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fields = [ 'City ID', 'Type', 'Name', 'Address', 'Phone', 'Group Name', 'City Name']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for entry in data['data']:
            value_type = entry.get("type", 'N/A')
            name = entry.get("name", 'N/A')
            address = entry.get("address", 'N/A')
            phone_number = entry.get("phone_number", 'N/A')
            group_name = entry.get("group_name", 'N/A')
            city_name = entry.get("city", {}).get("name", {}).get("en", 'N/A')
            city_id = entry.get("city", {}).get("id", 'N/A')

            writer.writerow({
                'City ID': city_id,
                'Type': value_type,
                'Name': name,
                'Address': address,
                'Phone': phone_number,
                'Group Name': group_name,
                'City Name': city_name,
            })

car_wuling()