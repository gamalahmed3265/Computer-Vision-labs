import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt
from preprocessing import *
from detectTrackcount import DetectionTracking

url="assets"
imageName=getImage(8)
videoName=getVideo(2)
path=f"{url}/{imageName}"


isExists(path)


######### img #########
def image(img):
    img=cv.imread(img)
    
    img=resize(img,scale_percent=60)
    
    # print(img.shape,img2.shape)

    DetectionTracking(img)
   
    cv.imshow("img",img)
    # cv.setMouseCallback('img',clickEventImg)
    closeImg()






######### video #########

def realTime(video):
    cap=cv.VideoCapture(video)
    w,h=getDimVideo(cap)
    while True:
        rat,frame=cap.read()
        if rat is False:
            break
        frame=resize(frame)
        DetectionTracking(frame)
        
        # cv.imshow("frame",roi)
        # cv.setMouseCallback('frame',clickEventImg)
        
        if cv.waitKey(60)==27:
            break
        
    cv.destroyAllWindows()
    cap.release()


if __name__ =="__main__":
    image(path)
    # realTime(path)
   
    

        
        