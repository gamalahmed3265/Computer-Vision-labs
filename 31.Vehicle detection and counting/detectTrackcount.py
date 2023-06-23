import cv2
import numpy as np
from preprocessing import grayImage,resize
from tracker import TrackerMaster

track=TrackerMaster()
# font=cv2.FONT_HERSHEY_PLAIN
font=cv2.FONT_HERSHEY_SIMPLEX

BGS= cv2.createBackgroundSubtractorMOG2(history=10)


ww=50
hh=50

detec=[]
offset=6
y1=300

def page_center(x,y,w,h):
    h=int(h/2)
    w=int(w/2)
    cx=x+h
    cy=y+w
    return cx,cy


count=0
def DetectionTracking(frame: np.ndarray):
    gray=grayImage(frame)
    #blur
    blur=cv2.GaussianBlur(gray,(3,3),5)
    #subtrationg
    img_sub=BGS.apply(blur)
    
    dilat=cv2.dilate(img_sub,np.ones((5,5)))
    
    contour,hierarchy=cv2.findContours(dilat,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        
    cv2.line(frame,(25,y1),(1200,y1),(255,0,0),3)
    
    for (i,c) in enumerate(contour):
        (x,y,w,h)=cv2.boundingRect(c)
        
        valider_contorno=(w>=ww)and (h>=hh)
        
        if not valider_contorno:
            continue
        
        cv2.rectangle(frame,(x,x),(x+w,y+h),(0,255,0),2)
        center=page_center(x, y, w, h)
    
        detec.append(center)
    
        cv2.circle(frame,center,4,(0,0,255),-1)
        
        for (x,y) in detec:
            if y<(y1+offset) and y>(y1-offset):
                global count
                count+=1
                cv2.line(frame,(25,y1),(1200,y1),(0,170,3),3)
                detec.remove((x,y))
                print(f"No. cars{count}")
                
    cv2.putText(frame,f"Nm. {count}",(25,y1),font,1,(244,45,2),4)


    cv2.imshow("frame",frame)
    # cv2.imshow("gray",gray)
    # cv2.imshow("blur",blur)
    cv2.imshow("img_sub",img_sub)
    





