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

def blakImage():
    img=np.zeros((500,500),np.uint8)
    return img

def grayImage(img):
    img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return img

def getDimVideo(cap: cv.VideoCapture):
    w=cap.get(cv.CAP_PROP_FRAME_WIDTH)
    h=cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    
    return w,h

def closeImg():
    k=cv.waitKey(0)
    if k==27:
        cv.destroyAllWindows()
        
def clickEventImg(event,x,y,flags,param):   
    if event==cv.EVENT_LBUTTONDOWN:
        print(x,y)
def getFonts(switch:int=0):
    return [
    cv.FONT_HERSHEY_SIMPLEX,
    cv.FONT_HERSHEY_PLAIN ,
    cv.FONT_HERSHEY_COMPLEX,
    ][switch]
    
def getImage(switch:int=0):
    return [
        "early.png",
        "orange.png",
        "apple.png",
        "contours.png",
        "logo.png",
        "Geometric Shapes .png",
        "car.png",
        "car plat.png",
        "book_page.png",
        "chess board.png"
        ][switch]

def getVideo(switch:int=0):
    return [
        "pepole.mp4",
        "highway.mp4",
        "Vehicle detection and counting.mp4",
        "eyes.mp4",
        ][switch]
