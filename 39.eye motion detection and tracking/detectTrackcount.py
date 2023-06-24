import cv2
import numpy as np
from preprocessing import grayImage,resize
from tracker import TrackerMaster

track=TrackerMaster()
# font=cv2.FONT_HERSHEY_PLAIN
# font=cv2.FONT_HERSHEY_SIMPLEX
font=cv2.FONT_HERSHEY_COMPLEX




def DetectionTracking(frame: np.ndarray, roi:np.ndarray):
    gray_roi=grayImage(roi)
    gray_roi=cv2.GaussianBlur(gray_roi,(7,7),0)
    _,col,row=roi.shape[::-1]
    
    
    _,threshold=cv2.threshold(gray_roi,75,255,cv2.THRESH_BINARY_INV)
    # threshold=cv2.resize(threshold,(500,500))
    contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    
    for con in contours:
        # print(con)
        x,y,w,h=cv2.boundingRect(con)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(25,234,0),1)
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),row),(34,234,0),2)
        cv2.line(roi,(0,y+int(h/2)),(col,y+int(h/2)),(25,200,0),2)
        # print(x,y,w,h)
        break
    # res=cv2.matchTemplate(gray_roi,gray,cv2.TM_CCORR_NORMED)
    
    # threshold=0.999
    # loc=np.where(res>=threshold)
    
    
    # for pt in zip(*loc[::-1]): #zip(loc[1],loc[0])
    #     cv2.rectangle(frame,(pt),(pt[0]+w,pt[1]+h),(0,255,0),1)

    
    cv2.imshow("frame",frame)
    cv2.imshow("threshold",threshold)
    cv2.imshow("gray_roi",gray_roi)
    cv2.imshow("roi",roi)
    
        





