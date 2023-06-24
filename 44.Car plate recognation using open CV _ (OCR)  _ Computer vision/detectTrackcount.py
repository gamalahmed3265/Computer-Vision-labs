import cv2
import numpy as np
from preprocessing import *
from tracker import TrackerMaster
import mediapipe as mp
import imutils
import easyocr

track=TrackerMaster()

font=getFonts()

def DetectionTracking(frame: np.ndarray):
    gray=grayImage(frame)

    bfilter=cv2.bilateralFilter(gray,11,17,17) #noise reduction
    edage=cv2.Canny(bfilter,30,300)
    contours=cv2.findContours(edage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # print(keypoints)
    contours=imutils.grab_contours(contours)
    contours=sorted(contours, key=cv2.contourArea,reverse=True)[:10]
    print(len(contours))
    location=None
    for contr in contours:
        # print(con)
        approx=cv2.approxPolyDP(contr,10,True)
        if len(approx) ==4:
            location=approx
            break
       
    print(location)
    
    make=np.zeros(frame.shape,np.uint8)
    new_img=cv2.drawContours(mask, [location],-1,255,-1)
    new_img=cv2.bitwise_and(img,img,mask=mask)
    
    (x,y)=np.where(frame==255)
    (x1,y1)=(np.min(x),np.min(y))
    (x2,y2)=(np.max(x),np.max(y))
    
    crpped_frame=frame[x1:x2+1,y1:y2+1]
    
    readr=easyocr.Reader(["en"])
    results=reader.readtext(crpped_frame)
    
    print(results)
    text=results[0][-2]
    
    cv2.putText(img,text,(approx[0][0][0], approx[1][0][1]+60),font,1,(255,0,0),5)
    cv2.rectangle(img,tuple(approx[0][0]),tuple(approx[2][0]),(250,225,85),3)
    
    cv.imshow("crpped_img",crpped_frame)
    
    
    cv2.imshow("frame",frame)
    # cv2.imshow("threshold",threshold)
    # cv2.imshow("gray",gray)
    # cv2.imshow("bfilter",edage)
    





