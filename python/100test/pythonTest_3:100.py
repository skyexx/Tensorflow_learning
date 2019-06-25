#Q3 一個整数加上100和268后都是一个完全平方

import math

for i in range(100000):

#转化为整值

    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))

    if (x*x == i+100) and (y*y == i+268):
        print(i)
