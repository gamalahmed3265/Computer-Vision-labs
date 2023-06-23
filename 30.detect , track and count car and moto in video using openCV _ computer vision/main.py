import cv2 as cv
import numpy as np
import os
from preprocessing import isExists,resize,getDimVideo,clickEventImg
from detectTrackcount import DetectionTracking

url="assets"
# imageName="early.png"
# imageName="orange.png"
# imageName2="apple.png"
# imageName="contours.png"
# imageName="logo.png"

# videoName="pepole.mp4"
videoName="highway.mp4"

path=f"{url}/{videoName}"

isExists(path)

# img=cv.imread(path)

# img=resize(img,scale_percent=60)

# print(img.shape,img2.shape)


cap=cv.VideoCapture(path)

# getDimVideo(cap)



count=0
while True:
    rat,frame=cap.read()
    if frame is None:
        break
    
    frame=resize(frame,flag=False,size=(750,450))
    
    DetectionTracking(frame,count)

    cv.imshow("frame",frame)
    
    cv.setMouseCallback('frame',clickEventImg)
    
    if cv.waitKey(60)==27:
        break
    
cv.destroyAllWindows()
cap.release()



# cv.imshow("img",img)

