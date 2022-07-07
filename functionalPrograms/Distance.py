'''
    @Author : Priyanka Salukhe
    @Date : 2022-07-06  23:20:00
    @Last Modified by : Priyanka Salunkhe
    @Last Modified Time : 2022-07-06  23:30:00
    @Title : prints the Euclidean distance from the point (x, y) to the origin (0, 0).
'''

import math
import sys

x1 = 0
y1 = 0

x2 = int(sys. argv[1])
y2 = int(sys. argv[2])

distance = math.sqrt((math.pow(x2,2)) +(math.pow(y2,2)))
print("Distance from the point (x,y) to the origin is",distance)