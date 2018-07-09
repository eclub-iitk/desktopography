

import freenect
import cv2 as cv
import numpy as np
from cythontry import threshold_fast
from cythontry import align
from cythontry import segment
import cmath 
from cythontry import coordinates_gui_to_kinect
from cythontry import coordinates_kinect_to_gui
import time
import socket
from operator import itemgetter
#from flask import Flask, Response
#from gevent.pywsgi import WSGIServer
#from gevent.queue import Queue
#from flask import render_template
#import json
#import random
import Queue as Q
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP

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
def update():
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
    #cv.imshow('Video', array)
    image1=np.zeros(shape=(h,w,3),dtype = float) 
    depth2 = np.zeros((480,640))  
    image3=np.zeros(shape=(h,w,3),dtype = float)
    img1, new_depth = align(array, depth, image1, depth2)   
    image2 = np.zeros(shape=(h,w,3),dtype = float)
    img2 = segment(img1 ,new_depth, image2, 0.5,1.8)
    img2 = np.asarray(img2)
    img2 = img2.astype(np.uint8)
    #cv.imshow("segmented image",img2)    
    new_depth = np.asarray(new_depth)
    raw_aligned_depth = new_depth.copy()
    raw_aligned_depth = np.float32(raw_aligned_depth)
    new_depth = new_depth.astype(np.uint8)
    cv.imshow("aligned depth",new_depth)    
    hsv = cv.cvtColor(img2, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, (0,48,0), (50,255,255))          
    test_kernel = np.ones((5,5),np.uint8)    
    mask = cv.medianBlur(mask,7)   
    mask3 = mask
    mask5 = cv.cvtColor(mask3,cv.COLOR_GRAY2BGR)
    cv.imshow("mask3",mask3)
    _,cnts,_ = cv.findContours(mask3,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    coloured = cv.cvtColor(mask3,cv.COLOR_GRAY2BGR)
    new_color = coloured.copy()
    maxArea = 0
    maxIter = 0
    for i in range(len(cnts)):
        if(cv.contourArea(cnts[i]) > maxArea):
            maxArea = cv.contourArea(cnts[i])
            maxIter = i
    skinMask2 = cv.drawContours(new_color,[cnts[maxIter]],0,(0,0,255),thickness = 3) 
    coloured[:] = 0
    skinMask3 = cv.drawContours(coloured,[cnts[maxIter]],0,(255,255,255),thickness = cv.FILLED) 
    skinMask3 = cv.medianBlur(skinMask3,5)
    skinMask3 = cv.cvtColor(skinMask3,cv.COLOR_BGR2GRAY)
    M = cv.moments(cnts[maxIter])
    handX = int(M["m10"] / M["m00"])
    handY = int(M["m01"] / M["m00"])
    #x,y,w,h = cv.boundingRect(cnts[maxIter])
    #skinMask2 = cv.rectangle(skinMask2,(x,y),(x+w,y+h),(0,255,0),2)   
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7,7))
    kernel2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
    erode_skin = cv.erode(skinMask3,kernel,iterations  = 3)
    erode_skin = cv.dilate(erode_skin,kernel,iterations = 3)
    
    cv.imshow("erode",erode_skin)
    new_skin = skinMask3 - erode_skin
    #new_skin = cv.medianBlur(new_skin,5)
    #new_skin = cv.dilate(new_skin,kernel2,iterations  = 2)        
    #new_skin = cv.erode(new_skin,kernel2,iterations  = 1)        
    cv.imshow("new",new_skin)
    _,cnts2,_ = cv.findContours(new_skin,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    erode_2 = cv.cvtColor(new_skin,cv.COLOR_GRAY2BGR)
    #maxArea = 0
    #maxIter = 0
    qu = Q.PriorityQueue()
    for i in range(len(cnts2)):
        qu.put((-1*cv.contourArea(cnts2[i]),i))
    skin_2 = erode_2.copy()
    how_many = len(cnts2)
    mid_ptscx = []
    mid_ptscy = []
    fingertips = []
    #cv.imshow("thin strips",erode_2)
    if(len(cnts2) > 5):
        
        how_many = 5
    for i in range(how_many):
        try:
            cnt = cnts2[qu.get()[1]]
            skin_2 = cv.drawContours(erode_2,[cnt],-1,(255,0,0),thickness = 1)
            (x,y),(MA,ma),angle = cv.minAreaRect(cnt)
            angle = ((np.pi)/180.0)*angle
            angle = np.pi/2 + angle
            x1 = x+(MA)*np.cos(angle)
            y1 = y+(MA)*np.sin(angle)

            x2 = x-(MA)*np.cos(angle)
            y2 = y-(MA)*np.sin(angle)
            #cv.line(img2,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),3)
            #cv.line(skin_2,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),3)            
            ellipse = cv.fitEllipse(cnt)
            #img2 = cv.ellipse(img2,ellipse,(0,255,0),2)
            rect = cv.minAreaRect(cnt)
            #print(rect)
            box = cv.boxPoints(rect)
            box = np.int0(box)
            endpoint1 = ((box[0][0]+box[1][0])/2,(box[0][1]+box[1][1])/2)
            endpoint2 = ((box[2][0]+box[3][0])/2,(box[2][1]+box[3][1])/2)
            endpoint3 = ((box[1][0]+box[2][0])/2,(box[1][1]+box[2][1])/2)
            endpoint4 = ((box[0][0]+box[3][0])/2,(box[0][1]+box[3][1])/2)
            dist1 = (endpoint1[0] - endpoint2[0])**2 + (endpoint1[1] - endpoint2[1])**2
            dist2 = (endpoint3[0] - endpoint4[0])**2 + (endpoint3[1] - endpoint4[1])**2
            if(dist2 > dist1):
                endpoint1 = endpoint3
                endpoint2 = endpoint4
            dist3 = (endpoint1[0] - handX)**2 + (endpoint1[1] - handY)**2
            dist4 = (endpoint2[0] - handX)**2 + (endpoint2[1] - handY)**2

            if(dist3 > dist4):
                endpoint = endpoint1
            else:
                endpoint = endpoint2
            fingertips.append(endpoint)       
            cv.circle(skin_2,endpoint,1,(255,0,0),5)
            #cv.drawContours(skin_2,[box],0,(0,0,255),2)
            M = cv.moments(cnt)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            mid_ptscx.append(cX)
            mid_ptscy.append(cY)
            #skin_2 = cv.circle(skin_2,(int(x),int(y)),3,(0,0,255),3)
            skin_2 = cv.circle(skin_2,(int(cX),int(cY)),1,(0,255,0),5)    
            img2 = cv.circle(img2,(int(cX),int(cY)),1,(0,255,0),5)
            skin_2 = cv.circle(skin_2,(int(handX),int(handY)),1,(0,255,255),5)    
            #skin_2 = cv.ellipse(skin_2,ellipse,(0,255,0),2)

            #print(x,y,MA,ma,angle)"""
        except Exception as e:
            print(e)
            a = 1+2        
    
    sumx = 0
    sumy = 0
    for finger in fingertips:
        
        cX = finger[0]
        sumx += cX
        cY = finger[1]
        sumy += cY

    avgx = sumx/len(fingertips)
    avgy = sumy/len(fingertips)
    finger_names = ["little","ring","middle","index","thumb"]
    if(len(fingertips) == 5):
        if(np.absolute(handX-avgx) > np.absolute(handY-avgy)):
            flag = "hor"
            fingertips = sorted(fingertips, key =  itemgetter(1))
            if(handX > avgx):
                flag = "hor1"
                little = fingertips[0]
                ring = fingertips[1]
                middle = fingertips[2]
                index = fingertips[3] 
                thumb = fingertips[4]
            else:
                flag = "hor2"
                little = fingertips[4]
                ring = fingertips[3]
                middle = fingertips[2]
                index = fingertips[1]            
                thumb = fingertips[0]
                finger_names.reverse()

        else:
            flag = "ver"
            fingertips = sorted(fingertips, key =  itemgetter(0))
            if(avgy > handY):
                flag = "ver1"
                little = fingertips[0]
                ring = fingertips[1]
                middle = fingertips[2]
                index = fingertips[3]            
                thumb = fingertips[4]
            else:
                flag = "ver2"
                little = fingertips[4]
                ring = fingertips[3]
                middle = fingertips[2]
                index = fingertips[1]          
                thumb = fingertips[0]
                finger_names.reverse()  
        img2 = cv.putText(img2, flag, (int(handX) , int(handY)),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)                
        img2 = cv.putText(img2, "index", (index[0] , index[1]),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)                
    
    finger_distance = []
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
    count = 0
    cv.circle(img2,(520,365),3,(0,0,0),-1)
    touching = []
    is_touched = 0
    for dist,name in zip(finger_distance,finger_names):
        if(dist < 10):
            count = count + 1
            touching.append(name)
            if(name == "index"):
                is_touched = 1
    #print(str(count)+ "/" + str(len(finger_distance)))
    print(touching,is_touched)
    p, q = coordinates_kinect_to_gui(index[0],index[1])
    send_string = str(p) + "," + str(q) + "," + str(is_touched) 
    sock.sendto(str(send_string), (UDP_IP, UDP_PORT))
    cv.imshow("contour",skinMask2)
    cv.imshow("skin_2",skin_2)
    cv.imshow("img2",img2)
    cv.setMouseCallback("Depth",coords_mouse_disp,depth)
    
    
     
cv.namedWindow('Depth')
cv.createTrackbar('threshold', 'Depth', threshold,     500,  change_threshold)
cv.createTrackbar('depth',     'Depth', current_depth, 2048, change_depth)
cv.namedWindow('img2')
cv.createTrackbar('dmin','img2', min ,200, change_min)
cv.createTrackbar('dmax','img2', max ,200, change_max)

while(1):
    start = time.time()
    update()
    end =  time.time()
    print("FPS: ",1.0/(end - start))
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()        
