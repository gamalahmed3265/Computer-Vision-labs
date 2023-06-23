import cv2 as cv
import numpy as np
import os
from preprocessing import isExists,resize
from image_blending import ImageBlending

url="assets"
# imageName="early.png"
imageName="orange.png"
imageName2="apple.png"


path=f"{url}/{imageName}"
path2=f"{url}/{imageName2}"

isExists(path)
isExists(path2)

img=cv.imread(path)
img2=cv.imread(path2)

img=resize(img,flag=False)
img2=resize(img2,flag=False)

# print(img.shape,img2.shape)

# img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ImageBlending(img,img2)


# cv.imshow("img",img)
# cv.imshow("img2",img2)

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()