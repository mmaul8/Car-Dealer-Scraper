import csv, requests

head = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Authorization": "<YOUR_AUTHORIZATION>",
    "Connection": "keep-alive",
    "Host": "ilm.toyota-emc.tech",
    "Origin": "https://www.toyota.astra.co.id",
    "Referer": "https://www.toyota.astra.co.id/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-platform": "Windows"
}

def serviceStatus(value):
    return "Available" if value == 1 else "Not Available"

def dealers():
    with open('dealer_toyota.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Dealer Name', 'Address', 'Phone', 'Fax', 'City Name', 'Province Name', 'Tradein', 'Charging Station', 'TOSS']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for d in range(1, 231):
            api = 'https://ilm.toyota-emc.tech/api/v1/dealers?field=all&city_id='+str(d)+'&charging_st=1&tradein=1&toss=1'
            isi = {
                "field": "all",
                "city_id": d,
                "charging_st": "1",
                "tradein": "1",
                "toss": "1"
            }
            z = requests.get(api, headers=head, data=isi)
            data = z.json()

            for entry in data:
                if isinstance(entry, dict):
                    name = entry.get('name', 'N/A')
                    address = entry.get('address', 'N/A')
                    phone = entry.get('phone', 'N/A')
                    fax = entry.get('fax', 'N/A')
                    city_name = entry.get('city_name', 'N/A')
                    province_name = entry['province'].get('name', 'N/A')
                    tradein = serviceStatus(entry.get('tradein', 'N/A'))
                    charging_st = serviceStatus(entry.get('charging_st', 'N/A'))
                    toss = serviceStatus(entry['main_dealer'].get('toss', 'N/A'))

                    writer.writerow({
                        'Dealer Name': name,
                        'Address': address,
                        'Phone': phone,
                        'Fax': fax,
                        'City Name': city_name,
                        'Province Name': province_name,
                        'Tradein': tradein,
                        'Charging Station': charging_st,
                        'TOSS': toss
                    })

dealers()