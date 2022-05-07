# Read an image and convert it into grayscale
import cv2
img = cv2.imread('E:/cat.jpg',0)
cv2.imshow('Grayscale Image',img)
cv2.waitKey()
cv2.destroyAllWindows()
