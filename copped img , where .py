import cv2 as cv
import numpy as np    
from preprocessing import *

img=blakImage()
cv.rectangle(img,(201,200),(351,350),(255,255,255),-1)


(x,y)=np.where(img==255)
(x1,y1)=(np.min(x),np.min(y))
(x2,y2)=(np.max(x),np.max(y))

crpped_img=img[x1:x2+1,y1:y2+1]
cv.imshow("img",img)
cv.imshow("crpped_img",crpped_img)
# cv.setMouseCallback('img',clickEventImg)
closeImg()
