import cv2 as cv
import numpy as np
import os


def isExists(path: str):
    assert os.path.exists(path)
    

url="assets"
# imageName="early.png"
imageName="ba.png"


path=f"{url}/{imageName}"

isExists(path)
    
img=cv.imread(path)
img=cv.resize(img,(550,250)) # w,h
# img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


blur=cv.blur(img,(11,11))#mean for pixels
gblur=cv.GaussianBlur(img,(5,5),0)#for noise image
mdblur=cv.medianBlur(img,5) #for salt and paper
bilateralFilter=cv.bilateralFilter(img,9,75,75)#preserve the borders

# blur avg for pixles
# GaussianBlur focuses center of pixles
# medianBlur salt and paper
# bilateralFilter focuses in edage

cv.imshow("img",img)
cv.imshow("blur",blur)
cv.imshow("gblur",gblur)
cv.imshow("mdblur",mdblur)
cv.imshow("bilateralFilter",bilateralFilter)



cv.imshow("img",img)


k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()