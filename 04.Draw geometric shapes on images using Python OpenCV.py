import cv2 as cv


url=".../"
cap=cv.VideoCapture(0)
#prepare the void and remove the noise and choise here the 'XVID'
fource=cv.VideoWriter_fourcc(*"XVID")
# to write in output.avi video
output=cv.VideoWriter(f"{url}output.avi",fource,20.0,(640,480))

# print(output.isOpened())
# print(cap.isOpened())
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while cap.isOpened():
    rat,frame=cap.read()
    if rat==True:
        
        output.write(frame)
        
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow("frame",gray)
        cv.imshow("frame",gray)
        if cv.waitKey(1) & 0xFF ==ord("q"):
            break
    else:
        break
    
cap.release()
output.release()
cv.destroyAllWindows()
