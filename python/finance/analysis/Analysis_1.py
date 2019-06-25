import tushare as ts
import numpy as np
import talib

class Analysis_1(object):
    function = 'Analysis some stock'
    
    def RSI6(self,number):
        df=ts.get_k_data('number')
        close = [float(x) for x in df['close']]
        df['RSI']=talib.RSI(np.array(close), timeperiod=6)     #RSI的天数一般是6、12、24
        df['MOM']=talib.MOM(np.array(close), timeperiod=5)
        df.tail(6)

