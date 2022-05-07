# Converting ideo into grayscale and showing both original and grayscale videos
import cv2
cap = cv2.VideoCapture('E:/tutorial.mp4')
while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('Original Video', frame)
  cv2.imshow('Garyscale Video', gray)
  if cv2.waitKey(25) == ord('q):
    break
cap.release()
cv2.destroyAllWindows()
                
