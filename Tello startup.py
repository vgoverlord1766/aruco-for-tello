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
