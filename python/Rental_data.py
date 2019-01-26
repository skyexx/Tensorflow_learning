import requests
from bs4 import BeautifulSoup

url = "https://www.skyscanner.com.tw/transport/flights/tpet/bjsa/190114/190217/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results"
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
price_data = soup.find_all('a')
print(price_data)
#for data in price_data:
    #a = ul.find_all('a')
