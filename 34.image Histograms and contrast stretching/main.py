import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt
from preprocessing import *
from detectTrackcount import DetectionTracking

url="assets"
# imageName="early.png"
imageName="orange.png"
# imageName2="apple.png"
# imageName="contours.png"
# imageName="logo.png"
# imageName="Geometric Shapes .png"
# videoName="pepole.mp4"
# videoName="highway.mp4"
# videoName="Vehicle detection and counting.mp4"

path=f"{url}/{imageName}"

isExists(path)

######### img #########
# img=blakImage()
# cv.rectangle(img,(0,250),(500,500),(255,255,255),-1)
# cv.rectangle(img,(23,66),(121,157),(234,148,207),-1)

img=cv.imread(path)

img=resize(img,scale_percent=60)

# print(img.shape,img2.shape)

b,g,r=cv.split(img)

print(img.ravel())
plt.hist(img.ravel(),255,[0,255])

plt.hist(b.ravel(),255,[0,255])
plt.hist(g.ravel(),255,[0,255])
plt.hist(r.ravel(),255,[0,255])

#or 

hist=cv.calcHist(img,[0],None,[255],[0,250])
plt.plot(hist)

# plt.hist(img.ravel(),255,[0,255])
# plt.show()

cv.imshow("img",img)
cv.imshow('r',r)
cv.imshow('g',g)
cv.imshow('b',b)

cv.setMouseCallback('img',clickEventImg)
k=cv.waitKey(0)

if k==27:
    cv.destroyAllWindows()








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




