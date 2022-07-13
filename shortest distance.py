import math
import sys

locations = ([20, 20], [40, 60], [-100, -20], [300, -40])
shortLocation = locations[0]
minDistance = 10000000000
newX = 0
newY = 0
for location in locations:
    x = location[0]
    y = location[1]

    if math.sqrt(x ** 2 + y ** 2) < minDistance:
        minDistance = math.sqrt(x** 2 + y** 2)
        shortLocation = location



print(shortLocation)