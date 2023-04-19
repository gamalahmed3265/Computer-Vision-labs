import cv2 as cv
import datetime


url="../"

# start a voido by camara or call by path
cap=cv.VideoCapture(0)
#prepare the void and remove the noise and choise here the 'XVID'
fource=cv.VideoWriter_fourcc(*"XVID")
output=cv.VideoWriter(f"{url}output.avi",fource,20.0,(640,480))

# print(output.isOpened())
# print(cap.isOpened())
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cap.set(3,600)
# cap.set(4,600)
# sparte()
# print(cap.get(3))
# print(cap.get(4))

font=cv.FONT_HERSHEY_SCRIPT_SIMPLEX

while cap.isOpened():
    rat,frame=cap.read()
    if rat==True:
        
       
        textFrame=f"width : {cap.get(3)} , hight : {cap.get(4)}"
        dateFrame=str(datetime.now())
        frame=cv.putText(frame,textFrame,(40,200),font,1,(200,250,0),3)
        frame=cv.putText(frame,dateFrame,(40,230),font,1,(200,250,0),3)
        output.write(frame)
        
        # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv.imshow("frame",frame)
        # cv2.imshow("frame",gray)
        if cv.waitKey(1) & 0xFF ==ord("q"):
            break
    else:
        break
    

        
cap.release()
output.release()
cv.destroyAllWindows()
