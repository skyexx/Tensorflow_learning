import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')

df = pd.read_csv('tslacsv.csv', parse_dates=Ture, index_col=0)


df_ohlc = df['Adj Close'].resample('10D').ohlc()
#10D is 10 days, also can use 10min
#ohlc() also could chanage to sum() mean()...
#ohlc means 'open high low close'
df_volume = df['Volume'].resample('10D').sum()
#then you can have each 10days data

#first you should reset the index  for df ohlc
df_ohlc.reset_index(inplace=Ture)

#convert timedate to a silly mdates
#like 2010-06-29 to 733952.0
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 =plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
ax1 =plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=ax1)

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volum.index.map(mdate2um), df_volum.values, 0)
plt.show()


