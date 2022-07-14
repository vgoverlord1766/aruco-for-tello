import cv2
import numpy as np

# Create an object to read camera video
cap = cv2.VideoCapture(0)

video_cod = cv2.VideoWriter_fourcc(*'XVID')
video_output = cv2.VideoWriter('captured_video.avi',
                               video_cod,
                               10,
                               (640, 480))

while (True):
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([22, 70, 0])
    upper = np.array([60, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('output', output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release video capture
# and video write objects
cap.release()
video_output.release()

# Closes all the frames
cv2.destroyAllWindows()
