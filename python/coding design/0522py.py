import numpy as np # 用np來取代numpy
import pylab as plt # 用plt來取代pylab

x = np.linspace(0,6*np.pi,100) # 0到6pi的意思，要引進pi的話，要寫成：.pi
y = np.sin(x)

# Turn on interative mpde
plt.ion()

def myplot(y):    # 定義函數
    plt.plot(y)   # 畫在心裡
    plt.draw()    # 顯示出來
    plt.pause(0.0001)
	
for i in range(10):  # for 迴圈不需要有end
    y = np.random.random([10,1])
    myplot(y)   # 呼叫myplot(y)來繪圖
	
	#plt.clf()
