from re import S
from bs4 import BeautifulSoup
import requests

"""
Dieses Programm geht auf die beiden Webseiten von billiger.de,
schaut auf den Preis der Graphikarte die in dem 'Angebote Button' steht,
vergleicht den Preis mit dem Wert vom 25.5.2022 als dieses Programm geschreiben wurde 
und gibt den neuen Wert mit Different an. 
"""

url_3060_billigerDE = f'https://www.billiger.de/products/2953961849-asus-dual-geforce-rtx-3060-v2-oc-12-gb-gddr6-1837-mhz-90yv0gb2-m0na10'
url_3050_billigerDE = f'https://www.billiger.de/pricelist/3633968402-asus-phoenix-geforce-rtx-3050-8g-gaming-90yv0hh2-m0na00'
page_3060 = requests.get(url_3060_billigerDE)
page_3050 = requests.get(url_3050_billigerDE)
soup_3060 = BeautifulSoup(page_3060.content, 'html.parser')
soup_3050 = BeautifulSoup(page_3050.content, 'html.parser')

div_3060 = soup_3060.find('div', attrs={'class':'btn btn-solid orange ctr-button'})
div_3050 = soup_3050.find('div', attrs={'class':'btn btn-solid orange ctr-button'})

userinput = input("Welche Graka wollen sie finden?")

if userinput == "3060":

    price = div_3060.text.split(' ')[6]

    price = price.split(',')

    price = int(price[0])

    if price > 469:
        print("Preis ist gestiegen auf", price, "€. Und somit um", price - 469, "€ gestiegen.")
    elif price < 469:
        print("Preis ist gesunken auf", price, "€ Und somit um", 469 - price, "€ gesunken.")
    elif price == 469:
        print("Preis ist noch immer", price, "€.")

elif userinput == "3050":

    price = div_3050.text.split(' ')[6]

    price = price.split(',')

    price = int(price[0])

    if price > 319:
        print("Preis ist gestiegen auf ", price, "€. Und somit um", price - 319, "€ gestiegen.")
    elif price <319:
        print("Preis ist gesunken auf ", price, "€. Und somit um", price - 319, "€ gestiegen.")
    elif price == 319:
        print("Preis ist noch immer ", price, "€")
else:
    print("Falscher Input du Hund")