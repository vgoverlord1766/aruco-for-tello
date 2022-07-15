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
from droneblocksutils.aruco_utils import detect_distance_from_image_center, detect_markers_in_image

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
while(True):
    tello.rotate_clockwise(1)
    frame = tello.get_frame_read().frame

    image, marker_details = detect_markers_in_image(frame, draw_center = True,
                                                        draw_reference_corner = False,
                                                        target_id = None,
                                                        draw_target_id = True,
                                                        draw_border = False)

    print(marker_details)

    try:
       id = marker_details[0][1]
       center_x, center_y = marker_details[0][0]
       print(id)



       # # Retrieve the actual values to use later
       # # notice the awkward mutliple indexing to get values
       # ID = ids[0][0]
       # Corner1 = corners[0][0][0]
       # Corner2 = corners[0][0][1]
       # Corner3 = corners[0][0][2]
       # Corner4 = corners[0][0][3]
       #
       # time.sleep(3)
       # # Draw a box around the ArUco marker from corner to corner
       # # on all 4 sides
       # cv2.line(image, (int(Corner1[0]), int(Corner1[1])),
       #          (int(Corner2[0]), int(Corner2[1])), (0, 0, 255), 2)
       #
       # cv2.line(image, (int(Corner2[0]), int(Corner2[1])),
       #          (int(Corner3[0]), int(Corner3[1])), (0, 0, 255), 2)
       #
       # cv2.line(image, (int(Corner3[0]), int(Corner3[1])),
       #          (int(Corner4[0]), int(Corner4[1])), (0, 0, 255), 2)
       #
       # cv2.line(image, (int(Corner4[0]), int(Corner4[1])),
       #          (int(Corner1[0]), int(Corner1[1])), (0, 0, 255), 2)
       #
       # area = (Corner1[0] - Corner3[0]) * (Corner1[1] - Corner3[1])
       #
       # center_x, center_y = marker_details[0][0]

       image, x_distance, y_distance, distance = detect_distance_from_image_center(image, int(center_x), int(center_y))

       if id not in visited:
           yaw = x_distance * (75/1080)
           if yaw < 0:
               tello.rotate_counter_clockwise(int(yaw))
           else:
               tello.rotate_clockwise(int(yaw))

           tello.move_forward(int(x_distance)-10)
           visited.append(id)

       print(area)
       if area > 80000:
           break
       # Show the image
       tello.move_forward(100)
       cv2.imshow('frame', image)
    except Exception as err:
      print(err)
      print("no frames")
      cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('m'):
       break

      # Wait until any key is pressed to exit
