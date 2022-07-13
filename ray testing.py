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
y = 0
z = 0



tello.go_xyz_speed(int(x-142),int(y),int(z),20)
#tello.go_xyz_speed(x,y,z,20)
