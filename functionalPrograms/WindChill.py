'''
    @Author : Priyanka Salunkhe
    @Date : 2022-07-06  13:35:00
    @Last Modified by : Priyanka Salunkhe
    @Last Modified Time : 2022-07-06  13:50:00
    @Title : Compute the wind chill by using formula.
'''

import math
import sys

t = float(sys.argv[1])
v = float(sys.argv[2])

if (t <= 50) and (v < 120) and (v > 3):
    windChill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v,0.16)
    print("Wind Chill is: ", math.floor(windChill))
else:
    print("Values Are Not Valid ")