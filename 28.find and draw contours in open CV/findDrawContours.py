import cv2
import numpy as np
from preprocessing import grayImage

def findDrawContours(img: np.ndarray):
    imgray=grayImage(img)
    rat,threshold=cv2.threshold(imgray,20,255,0)
    # img, threshold value =20 , color ,type
    # min 20
    # if pixles value less than 20 it`s = 0 and put in background
    # if pixles value greater than 20, put in frontground
    contours,hierarchy=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    # img ,get contours in all thing on edage , get contours in all edage
    
    print(len(contours))
    print(contours[0])
    
    cv2.drawContours(img,contours,-1,(0,255,0),1)
    # img , all contours  , color , size of line 
    # #
    #show image
    cv2.imshow("img",img)
    cv2.imshow("img gray",imgray)
    cv2.imshow("img threshold",threshold)
    

