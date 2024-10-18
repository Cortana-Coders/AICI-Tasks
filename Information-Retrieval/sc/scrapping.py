import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

location_data = []
data_json = {
    'name': '',
    'address': '',
    'city': '',
    'province': '',
    'scraped_at': '',
}
filename = 'superindo_locations.json'

url = 'https://www.superindo.co.id/hubungi-kami/lokasi-superindo/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'    
}

page_response = requests.get(url, headers=headers)
soup = BeautifulSoup(page_response.content, "html.parser")

if page_response.status_code == 200:
    location_list = soup.find('ul', class_='list-unstyled row')

    if location_list:
        locations = location_list.find_all('li')

        for location in locations:
            data_json['name'] = location.find('h4').text.strip()
            address_parts = location.find('p').text.strip().split(',')
            data_json['address'] = ','.join(address_parts[:-2]).strip()
            data_json['city'] = address_parts[-2].strip()
            data_json['province'] = address_parts[-1].strip()
            data_json['scraped_at'] = str(datetime.now().strftime("%d %B %Y, %H:%M WIB"))
            
            location_data.append(dict(data_json))
    else:
        print("Couldn't find the location list on the page.")
else:
    print(f'Request to {url} failed (Status code: {page_response.status_code})!')

# Save location data to JSON file
if location_data:
    with open(filename, "w") as write_file:
        json.dump(location_data, write_file, indent=3)
    print(f'Data successfully saved to {filename}!')
else:
    print('No data was scraped!')