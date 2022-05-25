from re import S
from bs4 import BeautifulSoup
import requests

url = f'https://www.billiger.de/products/2953961849-asus-dual-geforce-rtx-3060-v2-oc-12-gb-gddr6-1837-mhz-90yv0gb2-m0na10'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

div = soup.find('div', attrs={'class':'btn btn-solid orange ctr-button'})

price = div.text.split(' ')[6]

price = price.split(',')

price = int(price[0])

if price > 470:
    print("Preis ist gestiegen auf ", price, "€")
elif price <469:
    print("Preis ist gesunken auf ", price, "€")
elif price == 469:
    print("Preis ist noch immer ", price, "€")
