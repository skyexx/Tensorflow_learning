import tushare as ts
import numpy as np
import talib

df_dwzj=ts.get_k_data('601198')
close_dwzj = [float(x) for x in df_dwzj['close']]
df_dwzj['RSI']=talib.RSI(np.array(close_dwzj), timeperiod=6)     #RSI的天数一般是6、12、24
df_dwzj['MOM']=talib.MOM(np.array(close_dwzj), timeperiod=5)
df_dwzj.tail(6)

df_yhzj=ts.get_k_data('601881')
close_yhzj = [float(x) for x in df_yhzj['close']]
df_yhzj['RSI']=talib.RSI(np.array(close_yhzj), timeperiod=6)     #RSI的天数一般是6、12、24
df_yhzj['MOM']=talib.MOM(np.array(close_yhzj), timeperiod=5)
df_yhzj.tail(6)

pro = ts.pro_api()
new = pro.cctv_news(date='20190131')

