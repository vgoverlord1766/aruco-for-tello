import sys
sys.path.append("..")
import cv2
from cv2 import aruco
import imutils
from djitellopy import Tello
import cv2
import time
import numpy as np
import cv2 as cv
import sys
import math

tello = Tello()
tello.connect()
battery = tello.get_battery()
if battery <= 20:
    print("[WARNING]: Battery is low.", battery, "%")
else:
    print("Battery: ", battery, "%")

tello.streamon()
time.sleep(2)
tello.takeoff()
while tello.is_flying != True:
    time.sleep(1)
if tello.is_flying == True:
    print("Take off success!")

locations = [[-155.75, -155.75]]
locations2 = locations[:]
sortedLocations = []
newX = 0
newY = 0
currentX = 0;
currentY = 0;

#0: forward, 1: right, 2: backwards, 3: left
direction = 0;
for int2 in range(0,len(locations)):
    tello.rotate_clockwise(1)
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
    sortedLocations.append(shortLocation)
    print(shortLocation)

print(sortedLocations)

for newLocation in sortedLocations:
    time.sleep(2)
    print(newLocation[0])
    print(type(newLocation[0]))
    x = int(newLocation[0])
    y = int(newLocation[1])
    time.sleep(2)
    tello.go_xyz_speed(x - currentX - 40,y -currentY - 40, 0, 80)
    currentX = newLocation[0]
    currentY = newLocation[1]
    time.sleep(.5)

    while (True):
        tello.rotate_clockwise(1)
        image = tello.get_frame_read().frame
        aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)

        aruco_params = aruco.DetectorParameters_create()

        # Read in an image
        # resize so it is easier to view
        # convert to gray scale, because ArUco package requires a gray scale image

        image = imutils.resize(image, width=800)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # call the detectMarkers function from the OpenCV ArUco package
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=aruco_params)

        try:
            for id in ids:
                print(id)
            break
        except:
            tello.rotate_clockwise(90)
            tello.move_forward(40)
            tello.move_left(40)

        if cv2.waitKey(1) == ord('m'):
            break

tello.go_xyz_speed(0,0,100)
tello.land()