import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.carwow.co.uk/audi'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup)
