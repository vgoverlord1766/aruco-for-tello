import sys
sys.path.append("..")
import cv2
from cv2 import aruco
import imutils
import scipy
from djitellopy import Tello
import cv2
import time
import numpy as np
import cv2 as cv
import sys
import math
from droneblocksutils.aruco_utils import detect_distance_from_image_center

def find():
    for num in range(0,3):
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
               if id in visited:
                   ids.pop(id)


           id = ids[0]
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

           area = (Corner1[0] - Corner3[0]) * (Corner1[1] - Corner3[1])

           print(area)
           center_x = (Corner1[0] + Corner2[0])/2
           center_y = (Corner1[1] + Corner2[1]) / 2


           if id not in visited:
               height = Corner1[1] - Corner3[1]
               x_distance = ((Corner1[0] + Corner2[0]) / 2) - 540

               yaw = x_distance * (75/1080)
               print(yaw)
               if yaw <20 and yaw > 0:
                   tello.rotate_clockwise(21)
               elif yaw > -20 and yaw < 0:
                   tello.rotate_counter_clockwise(21)
               else:
                   tello.rotate_counter_clockwise(int(yaw))


               tello.move_forward(int(5184.7 * (height * height)**-0.471))
               time.sleep(2)
               tello.move_back(int(5184.7 * (height * height) ** -0.471))
               if yaw < 20 and yaw > 0:
                   tello.rotate_counter_clockwise(21)
               if yaw > -20 and yaw < 0:
                   tello.rotate_clockwise(21)
               else:
                   tello.rotate_clockwise(int(yaw))
           print(area)

           if area > 80000:
               break
           # Show the image
           cv2.imshow('frame', image)
           visited.append(id)
        except Exception as err:
          print(err)
          print("no frames")
          cv2.imshow('frame', gray)

        if cv2.waitKey(1) == ord('m'):
           break

          # Wait until any key is pressed to exit

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


video_capture = cv2.VideoCapture(0)
visited = []
tello.move_back(267)
find()
find()
tello.move_right(int(222))
tello.rotate_counter_clockwise(45)
find()
find()
tello.rotate_counter_clockwise(-45)
tello.move_forward(267)
tello.rotate_counter_clockwise(90)
find()
find()
tello.rotate_clockwise(90)
tello.go_xyz_speed(133,111,0,100)
tello.rotate_clockwise(180)
find()
find()
tello.move_right(111)
find()
find()
tello.go_xyz_speed(-133,-111,0,100)
tello.rotate_clockwise(90)
find()
find()