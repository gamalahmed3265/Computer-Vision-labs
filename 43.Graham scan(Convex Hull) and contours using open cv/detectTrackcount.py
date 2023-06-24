import cv2
import numpy as np
from preprocessing import *
from tracker import TrackerMaster
import mediapipe as mp

track=TrackerMaster()

font=getFonts(1)

def DetectionTracking(frame: np.ndarray):
    gray=grayImage(frame)
    gray=cv2.GaussianBlur(gray,(7,7),0)

    ret,threshold=cv2.threshold(gray,55,255,0)
    # # threshold=cv2.resize(threshold,(500,500))
    contoursy,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # bfilter=cv2.bilateralFilte(gray,11,17,17)
    
    for i in range(len(contoursy)):
        # print(con)
        hull=cv2.convexHull(contoursy[i])
        cv2.drawContours(frame,[hull],-1,(33,244,0),2)
    
    cv2.imshow("frame",frame)
    cv2.imshow("threshold",threshold)
    # cv2.imshow("threshold",bfilter)
            





