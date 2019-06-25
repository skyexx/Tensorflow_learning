import numpy as np

def RSI(array_list, periods=14):
    length = len(array_list)
    rsies = [np.nan] * length
    if length <= periods:
        return rsies
    up_avg = 0
    down_avg = 0

    first_t = array_list[:periods + 1]
    for i in range(1, len(first_t)):
        if first_t[i] >= first_t[i - 1]:
            up_avg += first_t[i] - first_t[i - 1]
        else:
            down_avg += first_t[i - 1] - first_t[i]
    up_avg = up_avg / periods
    down_avg = down_avg / periods
    rs = up_avg / down_avg
    rsies[periods] = 100 - 100 / (1 + rs)

    for j in range(periods + 1, length):
        up = 0
        down = 0
        if array_list[j] >= array_list[j - 1]:
            up = array_list[j] - array_list[j - 1]
            down = 0
        else:
            up = 0
            down = array_list[j - 1] - array_list[j]
        up_avg = (up_avg * (periods - 1) + up) / periods
        down_avg = (down_avg * (periods - 1) + down) / periods
        rs = up_avg / down_avg
        rsies[j] = 100 - 100 / (1 + rs)
    return rsies
    ```
