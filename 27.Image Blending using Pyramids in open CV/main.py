import cv2 as cv
import numpy as np
import os
from preprocessing import isExists,resize
from image_blending import ImageBlending

url="assets"
# imageName="early.png"
imageName="smarties.png"
imageName2="ba.png"


path=f"{url}/{imageName}"
# path2=f"{url}/{imageName2}"

isExists(path)
# isExists(path2)

img=cv.imread(path)
# img2=cv.imread(path2)

# img=cv.resize(img,(550,250)) # w,h
img=resize(img)
# img2=resize(img2)

# img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# ImageBlending(img,img2)

cv.imshow("img",img)

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()