import requests
import urllib.request
import time
import json
from bs4 import BeautifulSoup

def carwow_scrape():
    start_time = time.time()
    manufacturer_url = 'https://www.carwow.co.uk/car-reviews'
    manufacturer_response = requests.get(manufacturer_url)
    manufacturer_content = BeautifulSoup(manufacturer_response.content, 'html.parser')
    manufacturers = []
    all_car_data = []

    for manufacturer in manufacturer_content.find_all(class_='multi-columns-list-reviews__brand-name'):
        manufacturers.append(manufacturer.text.replace('\n', '').replace(' ', '-'))

    for manufacturer in manufacturers:
        url = f'https://www.carwow.co.uk/{manufacturer}'
        response = requests.get(url)
        content = BeautifulSoup(response.content, 'html.parser')

        models = content.find_all(class_= "card-generic")
        car_data = []
        manufacturer_data = {
            'manufacturer': manufacturer,
            'models': car_data
        }

        for car in models:
            carObject = {
                'manufacturer': car.find(class_='card-generic__media-title').text.replace('\n', ''),
                'model': car.find(class_='card-generic__media-subtitle').text.replace('\n', ''),
                'rating': car.find(class_='wowscore-numerator').text if car.find(class_='wowscore-numerator') else '0',
                'maxScore': car.find(class_='wowscore-denominator').text.split('/')[1] if car.find(class_='wowscore-denominator') else '10'
            }
            car_data.append(carObject)

        all_car_data.append(manufacturer_data)
        time.sleep(1)

    with open('carwowData.json', 'w') as outfile:
        json.dump(all_car_data, outfile, indent=4)

    print('* Scraped cw in %s seconds *' % round(time.time() - start_time, 2))

carwow_scrape()
