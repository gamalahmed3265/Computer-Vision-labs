import cv2
import numpy as np
from preprocessing import grayImage,resize

def MotionDetectionTracking(cap: cv2.VideoCapture):
    rat,frame1=cap.read()
    rat,frame2=cap.read()
    assert rat==True
    
    frame1=resize(frame1)
    frame2=resize(frame2)
    
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    
    blur=cv2.GaussianBlur(gray,(5,5),0)
    
    _,threshold=cv2.threshold(blur,60,255,cv2.THRESH_BINARY)
    
    dilated=cv2.dilate(threshold,None,iterations=10)
    
    contourst,hierarchy=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    for contour in contourst:
        (x,y,w,h)=cv2.boundingRect(contour)
        
        if cv2.contourArea(contour)<900:
            continue
        
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"status; {}".format("Movement"),(10,20),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3
                    )
    # image=cv2.resize(frame1,(1280,720))
        
    #
    cv2.imshow("frame",frame1)
    
    frame1=frame2
    rat,frame2=cap.read()
        

        
    

