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

tello.move_forward(20)
tello.move_down(20)
counter = 0;
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
    except:
        print("Not found yet")
    tello.rotate_clockwise(45)
    tello.move_forward(100)
    tello.rotate_counter_clockwise(90 + 45)
    counter += 1
    if counter == 4:
        break

    if cv2.waitKey(1) == ord('m'):
        break
time.sleep(3)