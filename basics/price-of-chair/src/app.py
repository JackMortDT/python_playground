__author__ = "LuisSas"

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com.mx/Alexander-Alois-Silla-Secretarial-Winchester/dp/B01MAVVSV9/ref=sr_1_6?ie=UTF8&qid=1543779581&sr=8-6&keywords=sillas")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice", "class": "a-size-medium a-color-price"})
string_price = element.text.strip() # "$1,424.84"

price_without_symbol = string_price[1:] # "$1,424.84"

price = float(price_without_symbol)

if price < 1000:
    print("Buy the chair")
    print("The current price is {}".format(string_price))
else:
    print("Don't buy the char")

# <span id="priceblock_ourprice" class="a-size-medium a-color-price">$1,424.84</span>
