import cv2
import numpy as np


cam = cv2.VideoCapture(0)
while True:
    ret, im =cam.read()

    cv2.imshow('im',im) 
    if cv2.waitKey(10)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()