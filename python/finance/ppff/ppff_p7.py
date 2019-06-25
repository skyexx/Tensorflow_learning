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
#you will all the companys you need, one company has one file

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

#get_data_from_yahoo()

#-------------------------------------------------p.7
# We shoule combine them together and pulled them rather then saving them it could have
# added them joned them to a main data frame

#compile them all into one data frame

# frist we should come up with a new function compile data

def compile_data():
    whit open('sp500tickers。pickle','rb') as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    for count,ticker in enumerate(tickers):
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Data', inplace=True)

        df.rename(columns = {'Adj Close':ticker}, inplac=True
        df.drop(['open','high','low','close','volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)
                  
    print(main_df.head())
    main_df.to_csv('sp500_jioned_closes.csv')

compile_data()

















