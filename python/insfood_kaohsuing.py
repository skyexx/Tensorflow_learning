from bs4 import BeautifulSoup
import requests
import os

url = "https://www.instagram.com/kaohsiung_dacodie/"
html = requests.get(url).text
soup = BeautifulSoup(html,'lxml')
div_alt = soup.find_all('div',{"class":"KL4Bh"})
os.makedirs('./img/',exist_ok = True)

for img in div_alt:
    imgs = img.find_all("img")
    for img_alt in imgs:
        url = img['srcset']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open ('./img/%s' % image_name,'wb') as f:
            for chunk in r.iter_content(chunk_size = 128):
                f.writer(chunk)
        print('save %s' % image_name)
        
