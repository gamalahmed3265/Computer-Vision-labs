import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt
from preprocessing import *
from detectTrackcount import DetectionTracking

url="assets"
# imageName="early.png"
# imageName="orange.png"
# imageName2="apple.png"
imageName="contours.png"
# imageName="logo.png"
# imageName="Geometric Shapes .png"
# videoName="pepole.mp4"
# videoName="highway.mp4"
# videoName="Vehicle detection and counting.mp4"

path=f"{url}/{imageName}"

isExists(path)

face_cascade=cv.CascadeClassifier("harrcascade_frontalface_default.xml")
######### img #########

# img=cv.imread(path)

# img=resize(img,scale_percent=60)

# print(img.shape,img2.shape)


# DetectionTracking(img)

# cv.imshow('face',img)
# closeImg()








######### video #########
cap=cv.VideoCapture(path)

getDimVideo(cap)



while True:
    rat,frame=cap.read()
    if frame is None:
        break
    
    frame=resize(frame,flag=False,size=(750,450))
    gray=grayImage(img)
    # DetectionTracking(frame)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    
    cv.imshow("frame",frame)
    
    # cv.setMouseCallback('frame',clickEventImg)
    
    if cv.waitKey(60)==27:
        break
    
cv.destroyAllWindows()
cap.release()




