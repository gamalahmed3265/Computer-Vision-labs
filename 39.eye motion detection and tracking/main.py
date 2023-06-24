import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt
from preprocessing import *
from detectTrackcount import DetectionTracking

# url="assets"

# imageName="early.png"
# imageName="orange.png"
# imageName2="apple.png"
# imageName="contours.png"
# imageName="logo.png"
# imageName="Geometric Shapes .png"
# videoName="pepole.mp4"
# videoName="highway.mp4"
# videoName="Vehicle detection and counting.mp4"
videoName="eyes.mp4"
path=f"{url}/{videoName}"

isExists(path)

######### img #########

# img=cv.imread(path)

# img=resize(img,scale_percent=60)

# print(img.shape,img2.shape)


# DetectionTracking(img)

# cv.imshow('face',img)
# closeImg()








######### video #########
cap=cv.VideoCapture(path)

# w,h=getDimVideo(cap)



while True:
    rat,frame=cap.read()
    if rat is False:
        break
    frame=resize(frame,scale_percent=60)
    
    roi=frame[80:200,280:480]
    DetectionTracking(frame,roi)
    # cv.imshow("frame",frame)
    # cv.imshow("roi",roi)

    cv.setMouseCallback('frame',clickEventImg)

    if cv.waitKey(60)==27:
        break
    
cv.destroyAllWindows()
cap.release()




