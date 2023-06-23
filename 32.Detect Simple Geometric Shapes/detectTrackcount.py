import cv2
import numpy as np
from preprocessing import grayImage,resize
from tracker import TrackerMaster

track=TrackerMaster()
# font=cv2.FONT_HERSHEY_PLAIN
font=cv2.FONT_HERSHEY_SIMPLEX

def putTextOnImage(img,text,x,y):
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,text,(x,y),font,0.5,(3,6,4))
    return img


def DetectionTracking(frame: np.ndarray):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,thresh=cv2.threshold(gray,240,255,cv2.CHAIN_APPROX_NONE)
    countours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
                    
    # dat=pd.DataFrame(countours).reshape()
    # print(dat)
    
    for contour in countours:
        # (x,y,w,h)=cv2.boundingRect(contour)
        # cv2.rectangle(img,(x,y),((x+w),(y+h)),(244,34,55),4)
        approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        # print(approx)
        
        cv2.drawContours(frame,[approx],0,(180,3,8),5)
        (x,y,w,h)=cv2.boundingRect(approx)
        aspectRato=w/h
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        if len(approx)==3:
            putTextOnImage(frame,"Triangle",x,y)
        elif len(approx)==4:
            if aspectRato>=0.95 and aspectRato<=1.5:
                putTextOnImage(frame,"squre",x,y)
            else:
                putTextOnImage(frame,"Rectangle",x,y)
    
        elif len(approx)==10:
            putTextOnImage(frame,"Star",x,y)
        # elif len(approx)==5:
        #     putTextOnImage(frame,"Pentagon",x,y)
        # else:
        #     putTextOnImage(frame,"Circle",x,y)
            
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('threshold',thresh)
    
        





