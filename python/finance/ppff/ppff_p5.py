
#Automating getting the S&P 500 list - Python Programming for Finance p.5

import bs4 as bs
import pickle
import requests

def save_sp500_tickers():
    #first we shoult ge sourse code
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    #response that text = text of the sourse code
    soup = bs.BeautifulSoup(resp.text,"lxml")
    #use beautiful soup to find something now we want find 'table'
    table = soup.find('table',{'class':'wikitable sortable'})
    tickers =[]
    
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        ticker.append(ticker)

    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers, f)

    print(tickers)
    
    return tickers

save_sp500_tickers()
