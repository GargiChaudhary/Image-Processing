# capturing video from your laptop's webcam
import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
while cap.isOpened():
    success,  frame = cap.read()
    if success:
        frame = cv.resize(frame, (600,400))
        cv.imshow('Original Video', frame)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('Grayscale Video', gray)
        k = cv.waitKey(1)
        if k==ord('q') & 0xFF:
            break            
        
cap.release()
cv.destroyAllWindows()
