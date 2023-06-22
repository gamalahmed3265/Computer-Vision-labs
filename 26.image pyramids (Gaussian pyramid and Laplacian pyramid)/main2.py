import cv2 as cv
import numpy as np
import os


def isExists(path: str):
    assert os.path.exists(path)
    

url="assets"
# imageName="early.png"
imageName="smarties.png"
# imageName="ba.png"


path=f"{url}/{imageName}"

isExists(path)
    
img=cv.imread(path)
img=cv.resize(img,(550,250)) # w,h
# img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


# layer=img.copy()
# gp=[layer]
# for i in range(6):
#     layer=cv.pyrDown(layer)
    
#     # layer=cv2.Laplacian(layer,cv2.CV_64F,ksize=3)
    
#     gp.append(layer)
#     cv.imshow(str(i),layer)
    
img1_copy=img.copy()
ga_img1=[img1_copy]
for i in range(6):
    img1_copy=cv.pyrDown(img1_copy)
    ga_img1.append(img1_copy)
 
#genrate laplacian pyramids for img1
img1_copy=ga_img1[5]
lap_img1=[img1_copy]
for i in range(5,0,-1):
    gaussian_expanded=cv.pyrUp(ga_img1[i])
    lapacian=cv.subtract(ga_img1[i],gaussian_expanded)
    lap_img1.append(lapacian)

#close windows
k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()