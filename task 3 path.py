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

locations = [[-135.5,0],[-267,0],[-267,-111.25],[-267,-222.5],[-133.5,-222.5],[0,-111.25],[0,-222.5],[133.5,-222.5],[267,-222.5],[267,-111.25],[267,0],[133.5,0],[267,0],[267,111.25],[267,222.5],[133.5,222.5],[0,222.5],[0,111.5],[-133.5,222.5],[-267,222.5],[-267,111.25]]
currentX = 0
currentY = 0

tello.go_xyz_speed(int(locations[0][0]-currentX),int(locations[0][1]-currentY),0,100)
time.sleep(1)
currentX = locations[0][0]
currentY = locations[0][1]
tello.rotate_clockwise(90)
#search
time.sleep(1)
tello.rotate_counter_clockwise(180)
time.sleep(2)
tello.rotate_counter_clockwise(90)

tello.land()
