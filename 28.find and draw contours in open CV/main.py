import cv2 as cv
import numpy as np
import os
from preprocessing import isExists,resize
from findDrawContours import findDrawContours

url="assets"
# imageName="early.png"
# imageName="orange.png"
# imageName2="apple.png"
imageName="contours.png"
imageName="logo.png"


path=f"{url}/{imageName}"

isExists(path)

img=cv.imread(path)

img=resize(img,scale_percent=60)

# print(img.shape,img2.shape)

findDrawContours(img)


# cv.imshow("img",img)

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()