import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

##start = dt.datetime(2000,1,1)
##end = dt.datetime(2016,12,31)
##
##df = web.DataReader('TSLA', 'yahoo', start, end)
###print(df.tail(6)) #print last 6 rows
##df.to_csv('tsla.csv')#save as tsla.csv

df = pd.read_csv('tsla.csv',parse_date=True, index_col=0)

#create a new column
#100ma is 100 days moving aveager
df['100ma']=df['Adj Close'].rolling(window=100,min_periods=0).mean()

#print all of tsla number untill the tail
#print(df.tail())
print(df.head())

ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
