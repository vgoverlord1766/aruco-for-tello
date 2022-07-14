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
battery = tello.get_battery()cd
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

locations = [[200, 20], [400, 20], [-100, -20], [600, -40]]
locations2 = locations[:]
sortedLocations = []
newX = 0
newY = 0
currentX = 0;
currentY = 0;

#0: forward, 1: right, 2: backwards, 3: left
direction = 0;
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
    sortedLocations.append(shortLocation)
    print(shortLocation)

print(sortedLocations)

for location in sortedLocations:
    tello.go_xyz_speed(location[0]-currentX - 142,location[1]-currentY, 100)
    currentX = location[0]
    currentY = location[1]
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
            print("no frames")
            cv2.imshow('frame', gray)
            if direction == 0:
                tello.move_forward(20)
            elif direction == 1:
                tello.move_right(20)
            elif direction == 2:
                tello.move_back(40)
            elif direction == 3:
                tello.move_left(40)
                forward = True

        if cv2.waitKey(1) == ord('m'):
            break

tello.go_xyz_speed(0,0,100)
tello.land()