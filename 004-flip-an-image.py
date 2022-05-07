# Read an image and flip it
import cv2
img = cv2.imread('E:/cat.jpg')
img = cv2.flip(img,1) # it accepts 3 parameters: 0, 1, -1
cv2.imshow('Flipped Image',img)
cv2.waitKey()
cv2.destroyAllWindows()
