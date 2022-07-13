from djitellopy import Tello
import time

x = -50
y= 0
z = 0

tello = Tello()
tello.connect()
battery = tello.get_battery()
if battery <= 20:
    print("[WARNING]: Battery is low.", battery, "%")
else:
    print("Battery: ", battery, "%")

while tello.is_flying != True:
    time.sleep(1)
if tello.is_flying == True:
    print("Take off success!")

tello.streamon()
time.sleep(2)
tello.takeoff()
tello.move_up(60)


tello.go_xyz_speed(x,y,z,20)

time.sleep(1)
tello.land()
