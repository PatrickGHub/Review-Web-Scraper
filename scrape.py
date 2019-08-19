import requests
import urllib.request
import time
import json
from bs4 import BeautifulSoup

url = 'https://www.carwow.co.uk/audi'
response = requests.get(url)
content = BeautifulSoup(response.content, 'html.parser')

models = content.find_all(class_= "card-generic")
car_arr = []

for car in models:

    carObject = {
        'manufacturer': car.find(class_='card-generic__media-title').text.replace('\n', ''),
        'model': car.find(class_='card-generic__media-subtitle').text.replace('\n', ''),
        'rating': car.find(class_='wowscore-numerator').text if car.find(class_='wowscore-numerator') else '0',
        'maxScore': car.find(class_='wowscore-denominator').text.split('/')[1] if car.find(class_='wowscore-denominator') else '10'
    }

    car_arr.append(carObject)

with open('carwowData.json', 'w') as outfile:
    json.dump(car_arr, outfile, indent=4)
