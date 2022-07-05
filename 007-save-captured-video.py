import cv2 as cv

#Capture a video from yoour webcam and save it 

cap = cv.VideoCapture(0)   #parameter 0 is used for webcam

#it is 4 byte code which is use to specify the video codec
fourcc = cv.VideoWriter_fourcc(*"XVID")  # *"XVID"
output = cv.VideoWriter("output.mp4",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    success, frame = cap.read()   #here read the frame
    
    if success==True:
        
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        output.write(gray)
        
        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    else:
        break
cap.release()
output.release()
cv2.destroyAllWindows(
