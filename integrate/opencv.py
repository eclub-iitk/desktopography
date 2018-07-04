import cv2


def mouse_disp(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
      	print(x,y)


img=cv2.imread('calc.png')
print(img.shape)

cv2.imshow('opencv frame',img)
cv2.setMouseCallback('opencv frame',mouse_disp,img)
cv2.waitKey()
cv2.destroyAllWindows()
