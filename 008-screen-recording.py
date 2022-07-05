#Records your screen 
import cv2 as cv
import pyautogui as p
import numpy as np

#create resolution
rs = p.size()

#file name
fn = input("Enter file name and path: ")

#fix the frame rate
fps = 60.0

fourcc = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter(fn, fourcc, fps, rs)

#create recordin module
cv.namedWindow("Screen Recording", cv.WINDOW_NORMAL)
cv.resizeWindow("Screen Recording", (600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f.cvtColor(f, cv.COLOR_BGR2RBG)
    output.write(f)
    cv.imshow("Screen Recording",f)
    k = cv.waitKey(1)
    if k == ord('q'):
        break
    
output.release()
cv.destroyAllWindows()
