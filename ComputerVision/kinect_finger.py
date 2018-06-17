import cv2
import numpy as np
import copy
import math
import freenect


thresh=60
blurvalue=41

threshold=100
depth_med=600

def change_threshold(value):
    global threshold
    threshold=value

def change_depth(value):
    global depth_med
    depth_med=value

def calculateFingers(res,drawing):
    if len(hull)>3:
        defects=cv2.convexityDefects(res,hull)
        if type(defects)!=type(None):
            cnt=0
            for i in range(defects.shape[0]):
                s,e,f,d=defects[i][0]
                start=tuple(res[s][0])
                end = tuple(res[e][0])
                far = tuple(res[f][0])
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
                if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
                    cnt += 1
                    cv2.circle(drawing, far, 8, [255, 255, 255], -1)
                    print(cnt)
            return True, cnt
    return False, 0

def show_depth():
    global threshold
    global depth_med

    depthMap,timestamp=freenect.sync_get_depth()

    depth_and=np.logical_and(depthMap>=depth_med-threshold,
                             depthMap<=depth_med+threshold)
    depth=np.multiply(depthMap,depth_and)
    depth=depth.astype(np.uint8)
    return depth

cv2.namedWindow('Depth')
cv2.createTrackbar('threshold', 'Depth', threshold,     500,  change_threshold)
cv2.createTrackbar('depth',     'Depth', depth_med , 2048, change_depth)


while True:
    gray=show_depth()
    blur=cv2.GaussianBlur(gray,(blurvalue,blurvalue),0)
    cv2.imshow("Depth",blur)

    threshimg=copy.deepcopy(blur)
    _,contours,hierarchy=cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    length=len(contours)
    maxArea=-1
    if length>0:
        for i in range(length):
            temp=contours[i]
            area=cv2.contourArea(temp)
            if area>maxArea:
                maxArea=area
                ci=i

        res=contours[ci]
        hull=cv2.convexHull(res)
        drawing=np.zeros(gray.shape,np.uint8)
        cv2.drawContours(drawing,[res],0,255,2)
        cv2.drawContours(drawing,[hull],0,255,3)

        isFinished,cnt=calculateFingers(res,drawing)
        if triggerSwitch is True:
            print(cnt)

    k=cv2.waitkey(5)
    if k==27:
        break

cv2.destroyAllWindows()
