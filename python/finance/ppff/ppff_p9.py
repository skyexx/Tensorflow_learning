'''one company at a time period
   and chart patterns，use indicator on
   just that company to predict。
   machine learning everything becomes
   features and labels。
   features define something and label is target。
   so we try to label everything as a buy sell or hold'''

# the data within the next seven trading days did price go up more than
# 2% if yes that's a buy，did it fall more than 2% if yes that's sell
import numpy as np
import pandas as pd
import pickle

def process_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv',index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace = True)

    for i in range(1,hm_days + 1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i)-df[ticker])/df[ticker]

    df. fillna(0,inplace = True)
    return tickers, df


