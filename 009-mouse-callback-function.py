
#Create a fucntion which help to find cordinate of any pixel and its color
import cv2 as cv

def mouse_event(event, x, y, flags, param):
    print('event== ', event)
    print('x== ',x)
    print('y== ',y)
    print('flags== ',flags)
    print('param== ', param)
    
    font = cv.FONT_HERSHEY_PLAIN
    
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        
        cord = '. '+ str(x) + ', ' + str(y)
        cv.putText(img, cord, (x,y), font, 1, 
                   (152,125,100), 2)
    
    if event == cv.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        
        color_bgr = ". "+str(b) + ', '+ str(g)+ ', '+ str(r)
        cv.putText(img, color_bgr, (x,y), font, 1, 
                   (152,255,130), 2)
        
cv.namedWindow(winname = 'res')
img = cv.imread('G:\MyImages\Krishna.jpg')
cv.setMouseCallback('res', mouse_event)

while True:
    img = cv.resize(img, (400,700))
    cv.imshow('res', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break 
    
cv.destroyAllWindows()
