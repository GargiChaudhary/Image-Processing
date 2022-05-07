#Read an image and then show the resized image 
import cv2
img = cv2.imread("E:/Images/w2.jpg") #path of image
img = cv2.resize(img,(800,450)) #(width,height)
cv2.imshow("Original Image",img)
cv2.waitKey()
cv2.destroyAllWindows()
