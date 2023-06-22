import cv2 as cv
import numpy as np
import os


def isExists(path: str):
    if os.path.exists(path):
        print("exists")


url="assets"
imageName="smarties.png"

path=f"{url}/{imageName}"

isExists(path)
    
img=cv.imread(path,-1)
img=cv.resize(img,(500,600))
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


_,mask=cv.threshold(img,220,255,cv.THRESH_BINARY_INV)

kernal=np.ones((5,5),np.uint8)

dilation=cv.dilate(mask,kernal,iterations=2)#good but increass the balls size because if any pixels under the kernal
erode=cv.erode(mask,kernal,iterations=2)#it encode the balls because if all pixels under the karnal not one erod
opening=cv.morphologyEx(mask,cv.MORPH_OPEN,kernal,iterations=2)# erosion dilation
closeing=cv.morphologyEx(mask,cv.MORPH_CLOSE,kernal,iterations=2)#dilation erosion



cv.imshow("img",img)
cv.imshow("mask",mask)
cv.imshow("dilation",dilation)
cv.imshow("erode",erode)
cv.imshow("opening",opening)
cv.imshow("closeing",closeing)

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()