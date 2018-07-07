
import cv2
import numpy as np

device=cv2.VideoCapture(0)
while True:
    ret, frame = device.read()

    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    low_range_blue = np.array([110,50,50])
    up_range_blue = np.array([130,255,255])
    mask1 = cv2.inRange(hsv,low_range_blue,up_range_blue)

    lower_range_red = np.array([150, 70, 30])
    upper_range_red=np.array([180,255,150])
    mask2=cv2.inRange(hsv,lower_range_red,upper_range_red)


    cv2.imshow('org show',frame)

    result1=cv2.bitwise_and(frame,frame,mask=mask1)
    result2=cv2.bitwise_and(frame,frame,mask=mask2)
    cv2.imshow('show1',result1)
    cv2.imshow('show2',result2)
    if cv2.waitKey(1)==13:
        break
device.release()
cv2.destroyAllWindows()

