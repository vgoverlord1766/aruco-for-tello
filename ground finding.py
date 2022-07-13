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
tello.move_up(60)
while tello.is_flying != True:
    time.sleep(1)
if tello.is_flying == True:
    print("Take off success!")

x = -200
y = -200
z = 0

distance = math.sqrt(x**2 + y**2)
newx = (distance- 152)/distance * x
newy = (distance-152)/distance * y
newz = (distance-152)/distance * z

video_capture = cv2.VideoCapture(0)

tello.go_xyz_speed(int(newx),int(newy),int(newz),20)
#tello.go_xyz_speed(x,y,z,20)
while(True):
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


       # Retrieve the actual values to use later
       # notice the awkward mutliple indexing to get values
       ID = ids[0][0]
       Corner1 = corners[0][0][0]
       Corner2 = corners[0][0][1]
       Corner3 = corners[0][0][2]
       Corner4 = corners[0][0][3]

       time.sleep(3)
       # Draw a box around the ArUco marker from corner to corner
       # on all 4 sides
       cv2.line(image, (int(Corner1[0]), int(Corner1[1])),
                (int(Corner2[0]), int(Corner2[1])), (0, 0, 255), 2)

       cv2.line(image, (int(Corner2[0]), int(Corner2[1])),
                (int(Corner3[0]), int(Corner3[1])), (0, 0, 255), 2)

       cv2.line(image, (int(Corner3[0]), int(Corner3[1])),
                (int(Corner4[0]), int(Corner4[1])), (0, 0, 255), 2)

       cv2.line(image, (int(Corner4[0]), int(Corner4[1])),
                (int(Corner1[0]), int(Corner1[1])), (0, 0, 255), 2)

       # Show the image
       cv2.imshow('frame', gray)
    except:
      print("no frames")
      cv2.imshow('frame', gray)

    if cv2.waitKey(1) == ord('m'):
       break

      # Wait until any key is pressed to exit
