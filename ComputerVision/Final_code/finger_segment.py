import freenect

import cv2 as cv

import numpy as np

from cythontry import threshold_fast 

 

threshold = 100

current_depth = 0

depth=[]



def coords_mouse_disp(event,x,y,flags,param):

    if event == cv.EVENT_LBUTTONDBLCLK:

        distance=100/(-0.00307 * depth[y][x] + 3.33)

        print(distance) 

 

def change_threshold(value):

    global threshold

    threshold = value

 

 

def change_depth(value):

    global current_depth

    current_depth = value

 

 

def show_depth():

    global threshold

    global current_depth

    global depth

 

    depth, timestamp = freenect.sync_get_depth()

    if timestamp==None:

        return

    

    

    R1=np.logical_and(depth >= current_depth - threshold,depth <= current_depth + threshold)

    R2=depth >= current_depth - threshold

    R3=depth <= current_depth + threshold



    depth = depth * np.logical_and(depth >= current_depth - threshold,

                                 depth <= current_depth + threshold)



    

    #depth = cv.GaussianBlur(depth, (7, 7), 0) 



#if depth<=current_depth-



    #R=(depth==0)

    #depth[R]=150	



    #print(current_depth)



    depth = depth.astype(np.uint8)

    

    

    #%load_ext cython

    #%%cython -a

    h = depth.shape[0]

    w = depth.shape[1]

    #print(h,w)



    image1=np.zeros(shape=(h,w,3),dtype = float)

    cv.imshow('new image',image1)

    #print(depth.shape)

    depth =  cv.cvtColor(depth,cv.COLOR_GRAY2RGB)

    img = cv.Sobel(depth,cv.CV_32F,1,0,ksize=3)

    cv.imshow('new image',img)

    img1 = threshold_fast(50,img,image1)

    new_img = np.asarray(img1)

    cv.imshow("lala",new_img)

    

    

    """kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

    img_prewittx = cv.filter2D(depth, -1, kernelx)

    img_prewitty = cv.filter2D(depth, -1, kernely)

    prewitt=(img_prewittx+img_prewitty)"""





    #image = cv.CreateImageHeader((depth.shape[1], depth.shape[0]),cv.IPL_DEPTH_8U,1)

    #cv.SetData(image, depth.tostring(),depth.dtype.itemsize * depth.shape[1])

    cv.imshow('Depth', depth)

    cv.setMouseCallback("Depth",coords_mouse_disp,depth)



    #cv.imshow("perwitt",prewitt)

    #cv.setMouseCallback("Depth image",coords_mouse_disp,depth)

 

 

def show_video():

    array,_ = freenect.sync_get_video()

    array = cv.cvtColor(array,cv.COLOR_RGB2BGR)

    cv.imshow('Video', array)

 

 

cv.namedWindow('Depth')

cv.namedWindow('Video')

cv.createTrackbar('threshold', 'Depth', threshold,     500,  change_threshold)

cv.createTrackbar('depth',     'Depth', current_depth, 2048, change_depth)

 

#print('Press ESC in window to stop')

 

 

while 1:

    show_depth()

    show_video()

    

    k = cv.waitKey(5) & 0xFF

    if k == 27:

        break



cv.destroyAllWindows()