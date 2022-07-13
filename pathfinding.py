import math
import sys

locations = [[200, 20], [400, 20], [-100, -20], [600, -40]]
locations2 = locations[:]

newX = 0
newY = 0

for int in range(0,len(locations)):
    shortLocation = []
    minDistance = 10000000000
    for location2 in locations2:
        x = location2[0]
        y = location2[1]

        if math.sqrt((x-newX) ** 2 + (y-newY) ** 2) < minDistance:
            minDistance = math.sqrt(x** 2 + y** 2)
            shortLocation = location2

    newX = shortLocation[0]
    newY = shortLocation[1]
    locations2.remove(shortLocation)
    print(shortLocation)