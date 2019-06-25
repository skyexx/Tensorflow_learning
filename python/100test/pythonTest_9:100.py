import time

myD = {1: 'a',2: 'b'}
# dict.items()遍历字典列表
for key, value in dict.items(myD):
    print(key,value)
    time.sleep(1)
