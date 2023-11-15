import csv, requests

def car_hyundai():
    url = 'https://www.hyundai.com/wsvc/template_en/spa/common/dealer/list.html?loc=ID&lan=id&defalut_latitude=-6.20278&defalut_long=106.84944&distanceUnit=K&distanceValue=5000&dealerService=241%2C242%2C321%2C322&search_type=E&s_dealer_name=&s_dealer_post_code=&s_dealer_address=&searchDealerNum=200&search_word=&search_dealer_type=D'
    h = requests.get(url)
    data = h.json()

    with open('dealer_hyundai.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fields = ['RNum', 'Type', 'Dealer Name', 'Phone', 'Address']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for entry in data:
            rid = entry.get('rnum', 'N/A')
            value_type = entry.get("dealer_service_nm", 'N/A')
            name = entry.get("dealer_name", 'N/A')
            address = entry.get("dealer_address", 'N/A')
            phone_number = entry.get("dealer_phone1", 'N/A')

            writer.writerow({
                'RNum': rid,
                'Type': value_type,
                'Dealer Name': name,
                'Phone': address,
                'Address': phone_number,
            })


car_hyundai()