import cv2 as cv
import numpy as np
import os


def isExists(path: str):
    assert os.path.exists(path)
    
def resize(img :np.ndarray,scale_percent=30,flag:bool=True,size: tuple =(512,512)):
    
    if flag:
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        #dsize
        dsize = (width, height)
        img = cv.resize(img, dsize)
    else:
        img=cv.resize(img,size) # w,h
    return img

def whiteImage():
    img=np.ones([512,512,3],np.uint8)
    img.fill(255)
    return img

# def blacImage():
#     img=np.zeros([512,512,3],np.uint8)
#     img.fill(255)

def grayImage(img):
    img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return img