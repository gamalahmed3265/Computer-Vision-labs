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
imageName="Geometric Shapes .png"
# videoName="pepole.mp4"
# videoName="highway.mp4"
# videoName="Vehicle detection and counting.mp4"

path=f"{url}/{imageName}"

isExists(path)

img=cv.imread(path)

img=resize(img,scale_percent=60)

# print(img.shape,img2.shape)


# cap=cv.VideoCapture(path)




DetectionTracking(img)



k=cv.waitKey(0)

if k==27:
    cv.destroyAllWindows()






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



# cv.imshow("img",img)

