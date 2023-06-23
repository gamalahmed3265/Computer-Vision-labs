import cv2 as cv
import numpy as np
import os


def isExists(path: str):
    assert os.path.exists(path)
    
def resize(img):
    #img=cv.resize(img,(550,250)) # w,h
    scale_percent = 30
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    #dsize
    dsize = (width, height)
    img = cv.resize(img, dsize)
    
    return img
    