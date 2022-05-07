#Convert the image into grayscale and save it on clicking 's'
import cv2
img = cv2.imread('E:/cat.jpg',0)
img = cv2.resize(img,(700,400))
cv2.imshow('Grayscale Image',img)
k = cv2.waitKey()
if k == ord('s'):
  cv2.imwrite('E:/output.png',img)
cv2.destroyAllWindows()
