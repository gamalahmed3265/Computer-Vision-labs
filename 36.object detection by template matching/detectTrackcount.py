import cv2
import numpy as np
from preprocessing import grayImage,resize
from tracker import TrackerMaster

track=TrackerMaster()
# font=cv2.FONT_HERSHEY_PLAIN
# font=cv2.FONT_HERSHEY_SIMPLEX
font=cv2.FONT_HERSHEY_COMPLEX




def DetectionTracking(img: np.ndarray):
    gray=grayImage(img)
    
    face=gray[10:370,170:350]
    #       hight   width
    w,h=face.shape[::-1]
    
    # print("Wigth ",w," hight ",h)
    
    res=cv2.matchTemplate(gray,face,cv2.TM_CCORR_NORMED)
    # print(res)
    
    threshold=0.99
    loc=np.where(res>=threshold)
    
    # print(loc)
    
    for pt in zip(*loc[::-1]): #zip(loc[1],loc[0])
        print(pt)
        # cv2.putText(img,"gamal",(pt),font,1,(255,209,45),0)
        cv2.rectangle(img,(pt),(pt[0]+w,pt[1]+h),(0,255,0),2)
    
    cv2.imshow('image',img)
    # cv2.setMouseCallback('image',click_event)
    
    cv2.imshow('face',face)
    cv2.imshow('gray',gray)
    cv2.imshow('res',res)
        





