import cv2 as cv
import numpy as np



def click_event_photoshope(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
         print((x,y))


def getEventsfromCV():
    events=[i for i in dir(cv) if 'EVENT' in i]

    print(events)


# ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON',
#  'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY',
#  'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP',
#  'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP',
#  'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL',
#  'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']    
 
   

def click_event(event,x,y,flags,param):
    global img
    if event==cv.EVENT_LBUTTONDOWN:
        print(x,y)
        font=cv.FONT_HERSHEY_SCRIPT_SIMPLEX
        text=f"{str(x)} , {str(x)} "
        img=cv.putText(img,text,(x,y),font,.5,(200,250,0),2)
        cv.imshow("image", img)
        
    if event==cv.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        
        font=cv.FONT_HERSHEY_SCRIPT_SIMPLEX
        text=f"{str(blue)} , {str(green)} , {str(red)}"

        img=cv.putText(img,text,(x,y),font,.5,(200,250,0),2)
        cv.imshow("image", img)


def click_event_create_window(event,x,y,flags,param):
    if event==cv.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        myColorsImage=np.zeros((512,512,3),dtype=np.uint8)
        myColorsImage[:]=[blue,green,red]
        cv.imshow("Color", myColorsImage)


def click_event_draw(event,x,y,flags,param):
    points=[]
    global img
    if event ==cv.EVENT_LBUTTONDOWN:
        points.append((x,y))
        if len(points)>2:
            cv.line(img,points[-1],points[-2],(255,0,255),3)
        # if  len(points)>10:
        #     font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        #     img=cv2.putText(img,"finsh",(x,y),font,.5,(200,250,0),2)
        cv.imshow("image",img)
        





url="C:\Projects\Collage\ML\computer vision\image"
img=f"{url}\gamal.jpg"

img=cv.imread(img,0)
img=cv.resize(img,(400,400))


#getEventsfromCV()

cv.imshow("image",img)

cv.setMouseCallback("image",click_event_draw)

k=cv.waitKey(0)

if k==27:
    cv.destroyAllWindows()
elif k==ord("s"):
    cv.imwrite(f"{url}new.png",img)
    cv.destroyAllWindows()

