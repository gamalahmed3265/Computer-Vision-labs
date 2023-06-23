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

######### img #########

img=cv.imread(path)

img=resize(img,scale_percent=60)

# print(img.shape,img2.shape)


# DetectionTracking(img)


ret1,thr1=cv.threshold(img,127,255,cv.THRESH_BINARY)

ret2,thr2=cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

blur=cv.GaussianBlur(img,(5,5),0)

ret3,thr3=cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# imags=[img ,0,thr1,
#        img ,0,thr2,
#        blur,0,thr3]



cv.imshow("img",img)
cv.imshow("img",thr1)
# cv.imshow("img",thr2)
# cv.imshow("img",v)

closeImg()








######### video #########
# cap=cv.VideoCapture(path)

# getDimVideo(cap)



# while True:
#     rat,frame=cap.read()
#     if frame is None:
#         break
    
#     frame=resize(frame,flag=False,size=(750,450))
    
#     DetectionTracking(frame)

#     cv.imshow("frame",frame)
    
#     # cv.setMouseCallback('frame',clickEventImg)
    
#     if cv.waitKey(60)==27:
#         break
    
# cv.destroyAllWindows()
# cap.release()




