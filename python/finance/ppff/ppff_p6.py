
#Automating getting the S&P 500 list - Python Programming for Finance p.5

import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
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

#-------------------------------------------------p.6

#save_sp500_tickers()

def get_data_from_yahoo(reload_sp500 = False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2000,1,1)
    end= dt.datetime(2016,12,31)

    for ticker in tickers[:50]: # it well save first 50 data,if you want all
                                # the data get off the '[:50]'
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo',start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()
            
