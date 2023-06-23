import cv2 as cv
import numpy as np
import os
from preprocessing import isExists,resize,getDimVideo
from MotionDetectionTracking import MotionDetectionTracking

url="assets"
# imageName="early.png"
# imageName="orange.png"
# imageName2="apple.png"
# imageName="contours.png"
# imageName="logo.png"

videoName="pepole.mp4"

path=f"{url}/{videoName}"

isExists(path)

# img=cv.imread(path)

# img=resize(img,scale_percent=60)

# print(img.shape,img2.shape)


cap=cv.VideoCapture(path)

# getDimVideo(cap)


while True:
   
    # frame1=resize(frame1)
    # frame2=resize(frame2)
    
    MotionDetectionTracking(cap)
    
    # frame1=frame2
    # rat,frame2=cap.read()
    
    if cv.waitKey(60)==27:
        break
    
cv.destroyAllWindows()
cap.release()



# cv.imshow("img",img)

