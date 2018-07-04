import freenect
import cv2 as cv
import numpy as np
from cythontry import threshold_fast
from cythontry import align
from cythontry import segment
import cmath 
from Ycrcb import ycbcr
from cythontry import coordinates_gui_to_kinect
from cythontry import coordinates_kinect_to_gui

    
threshold = 100
current_depth = 600
depth=[]
min = 0
max = 100
f1u = 601.9457306
f1v = 596.05263911
c1u = 322.50529377
c1v = 230.96510472 
def coords_mouse_disp(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print(depth[y][x]) 
 
def change_threshold(value):
    global threshold
    threshold = value 
def change_max(value):
    global max
    max = value
def change_min(value):
    global min
    min = value    
def change_depth(value):
    global current_depth
    current_depth = value
def get_video():
    array,_ = freenect.sync_get_video(0,freenect.VIDEO_IR_10BIT)
    return array
def pretty_depth(depth):
    np.clip(depth,0,2**10 - 1,depth)
    depth >>= 2
    depth = depth.astype(np.uint8)
    return depth 
def show_depth():
    global threshold
    global current_depth
    global depth 
    global max
    global min
    depth, timestamp = freenect.sync_get_depth()
    if timestamp==None:
        return
    
   
    depthnew = depth * np.logical_and(depth >= current_depth - threshold,depth <= current_depth + threshold)
    depthnew = depthnew.astype(np.uint8)
    cv.imshow("Depth",depthnew)
    h = depth.shape[0]
    w = depth.shape[1]
    array,_ = freenect.sync_get_video()
    array = cv.cvtColor(array,cv.COLOR_RGB2BGR)
    image1=np.zeros(shape=(h,w,3),dtype = float) 
    depth2 = np.zeros((480,640))  
    image3=np.zeros(shape=(h,w,3),dtype = float)
    img1,new_depth = align(array,depth,image1,depth2)   
    image2 = np.zeros(shape=(h,w,3),dtype = float)
    img2 = segment(img1,new_depth, image2, 1.0,1.😎
    img2 = np.asarray(img2)
    img2 = img2.astype(np.uint8)
    cv.imshow("segmented image",img2)    
    new_depth = np.asarray(new_depth)
    raw_aligned_depth = new_depth.copy()
    new_depth = new_depth.astype(np.uint8)
    cv.imshow("aligned depth",new_depth)    
    hsv = cv.cvtColor(img2, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, (0,48,0), (50,255,255)) 
    ycrcb = cv.cvtColor(array, cv.COLOR_BGR2YCrCb)
    mask2 = ycbcr(ycrcb) 
    res2 = cv.bitwise_and(ycrcb, ycrcb, mask = mask2)
    mask2 = cv.dilate(mask2, None, iterations = 1)           
    test_kernel = np.ones((5,5),np.uint8)    
    mask = cv.medianBlur(mask,7)   
    mask3 = mask
    mask5 = cv.cvtColor(mask3,cv.COLOR_GRAY2BGR)
    cv.imshow("mask3",mask3)
    ,cnts, = cv.findContours(mask3,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    mask5 = cv.drawContours(mask5,cnts,-1,(255,0,255),3)
    maxArea = 0.0
    maxiter = 0
    for c in range(0,len(cnts)):
        if(maxArea < cv.contourArea(cnts[c])):
            maxArea = cv.contourArea(cnts[c])
            maxiter = c
    hull = cv.convexHull(cnts[maxiter])
    hull2 = cv.convexHull(cnts[maxiter],returnPoints = False)
    defects = cv.convexityDefects(cnts[maxiter],hull2)
    cnt = cnts[maxiter]
    fingertips = []    
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        temp = []
        if(start[0] > 100 and start[0] < 540 and start[1] > 100 and start[1] < 380):
            if(len(fingertips) > 0):
                flag = 0
                for x in fingertips:
                    dist = ((start[0] - x[0])**2 + (start[1] - x[1])**2)**0.5
                    if(dist < 10):
                        flag = 1
                        break
                if(flag == 0):
                    fingertips.append(start)
                    mask5 = cv.circle(img2,start,5,[255,0,255],-1)
                   
            else:
                fingertips.append(start)
                mask5 = cv.circle(img2,start,5,[255,0,0],-1)

    cv.imshow("mask5",mask5)
    finger_distance = []
    flag = 0
    for finger in fingertips:
        coord = raw_aligned_depth[finger[1]][finger[0]]
        distance=1.0/(-0.00307 * coord + 3.33)
        min_x = finger[1]
        min_y = finger[0]
        max_x = finger[1]
        max_y = finger[0]
        temp_min = coord
        temp_max = coord
        for i in range(-10,10):
            for j in range(-10,10):
                if(raw_aligned_depth[finger[1]+i][finger[0]+j] < temp_min):
                    temp_min = raw_aligned_depth[finger[1]+i][finger[0]+j]
                    min_x = finger[1] + i
                    min_y = finger[0] + j
                if(raw_aligned_depth[finger[1]+i][finger[0]+j] > temp_max):
                    temp_max = raw_aligned_depth[finger[1]+i][finger[0]+j]
                    max_x = finger[1] + i
                    max_y = finger[0] + j    
        finger_distance.append(raw_aligned_depth[max_x][max_y]-raw_aligned_depth[min_x][min_y])
        cX = finger[0]
        cY = finger[1]
        z1 = distance
        x1 =  z1*(cX-c1u)/f1u
        y1 =  z1*(cY-c1v)/f1v   
        if(flag == 0):
            flag = 1
            mask5 = cv.putText(mask5, str(cX) + "," + str(cY), (cX - 20, cY - 20),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    c1,c2 = coordinates_gui_to_kinect(500,500)
    print(c1,c2)
    mask5 = cv.circle(mask5 ,(c1,c2) ,5 ,[0,0,0],-1)
    j1 = 0
    for i in range(0,len(finger_distance)):
        if(finger_distance[i] > 6 ):
            j1+=1
    print(str(j1)+ "/" + str(len(finger_distance)))        
    cv.imshow("contour",mask5)
    cv.setMouseCallback("Depth",coords_mouse_disp,depth)
 
def show_video():
    array,_ = freenect.sync_get_video()
    array = cv.cvtColor(array,cv.COLOR_RGB2BGR)
    
    cv.imshow('Video', array)
     
cv.namedWindow('Depth')
cv.createTrackbar('threshold', 'Depth', threshold,     500,  change_threshold)
cv.createTrackbar('depth',     'Depth', current_depth, 2048, change_depth)
cv.namedWindow('img2')
cv.createTrackbar('dmin','img2', min ,200, change_min)
cv.createTrackbar('dmax','img2', max ,200, change_max)
 
while 1:
    show_depth()
    show_video()
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
