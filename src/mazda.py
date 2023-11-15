import csv, requests

def car_mazda():
    url = 'https://form.mazda.co.id/api/map/dealers?province'

    m = requests.get(url)
    data = m.json()
    
    with open('dealer_mazda.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fields = ['Dealer ID', 'Type', 'Dealer Name', 'Phone', 'Address', 'Province']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for entry in data:
            did = entry.get('dealer_id', 'N/A')
            valType = entry.get('type', 'N/A')
            name = entry.get('title', 'N/A')
            phone = entry.get('phone', 'N/A')
            a1 = entry.get('addressOne', 'N/A')
            a2 = entry.get('addressTwo', 'N/A')
            address = a1 + ' ' + a2
            province = entry.get('province', 'N/A')

            writer.writerow({
                'Dealer ID': did,
                'Type': valType,
                'Dealer Name': name,
                'Phone': phone,
                'Address': address,
                'Province': province,
            })

car_mazda()