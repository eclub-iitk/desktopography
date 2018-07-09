import cv2
import cython
import numpy as np

@cython.boundscheck(False)
cpdef double[:, :,:] threshold_fast(int T, float[:,:] image, double[:, :,:] image1,int thr,int th):
    # set the variable extension types
    cdef int x, y, w, h, z,t,c, c1,i,x1

    cdef double start,tempb,tempg,temp,tempr
    #cv2.imshow('newimage',image)
    # grab the image dimensions
    h = image.shape[0]
    w = image.shape[1]
    # loop over the image
    for y in range(0, h):
        for x in range(0, w):
            temp = image[y][x]
            #temp = (image[y][x][0] + image[y][x][1] + image[y][x][2])/3.0
            if(temp < T and temp > -1*T):
                image1[y][x][0] = 0
                image1[y][x][1] = 0
                image1[y][x][2] = 0
            elif(temp > 0):
                image1[y][x][0] = 255
                image1[y][x][1] = 0
                image1[y][x][2] = 0
            elif(temp < 0):
                image1[y][x][0] = 0
                image1[y][x][1] = 255
                image1[y][x][2] = 0
            else:
                image1[y][x][0] = 0
                image1[y][x][1] = 0
                image1[y][x][2] = 255            
    for y in range(0, h):
        x1 = 0
        while x1 < w:
            tempb = image1[y][x1][0]
            if(tempb == 255):
                for t in range(x1+1,w):
                    tempg = image1[y][t][1]
                    if (tempg == 255):
                        break  
                if ((t-x1)<=th and (t-x1) >= thr):
                    
                    for c in range(x1 ,t+1):
                        image1[y][c][0]=255
                        image1[y][c][1]=255
                        image1[y][c][2]=255    

                    '''elif( (t-x1)>th):    
                        for c in range(x1 ,t+1):
                            image1[y][c][0]=255
                            image1[y][c][1]=255
                            image1[y][c][2]=0''' 
                    '''c1 = (int)((t+x1)/2)
                    image1[y][c1][0]=0
                    image1[y][c1][1]=255
                    image1[y][c1][2]=255'''
                    
                x1 = t
            x1 = x1+1          
    for x in range(0,w):
        for y in range(0,h):

            temp = (image1[y][x][0] + image1[y][x][1] + image1[y][x][2])/3.0
            tempb = image1[y][x][0]
            tempg = image1[y][x][1]
            tempr = image1[y][x][2]
            if((tempb == 255 and tempg == 0 and tempr == 0) or (tempg == 255 and tempr == 0 and tempb == 0)):
                    image1[y][x][0]=0
                    image1[y][x][1]=0
                    image1[y][x][2]=0
            '''if(temp == 255):
                if((image1[y][x-1][0]==255 or image1[y][x+1][1] == 255) or (image1[y][x-1][1] == 255 or image1[y][x+1][0]) == 255):                      
                    image1[y][x][0] = 0
                    image1[y][x][1] = 0
                    image1[y][x][2] = 255
                    image1[y-1][x][0] = 0
                    image1[y-1][x][1] = 0
                    image1[y-1][x][2] = 255
                    image1[y-1][x-1][0] = 0
                    image1[y-1][x-1][1] = 0
                    image1[y-1][x-1][2] = 255
                    image1[y-1][x+1][0] = 0
                    image1[y-1][x+1][1] = 0
                    image1[y-1][x+1][2] = 255
                    image1[y][x+1][0] = 0
                    image1[y][x+1][1] = 0
                    image1[y][x+1][2] = 255
                    image1[y][x-1][0] = 0
                    image1[y][x-1][1] = 0
                    image1[y][x-1][2] = 255
                    image1[y+1][x][0] = 0
                    image1[y+1][x][1] = 0
                    image1[y+1][x][2] = 255
                    image1[y+1][x-1][0] = 0
                    image1[y+1][x-1][1] = 0
                    image1[y+1][x-1][2] = 255
                    image1[y+1][x+1][0] = 0
                    image1[y+1][x+1][1] = 0
                    image1[y+1][x+1][2] = 255'''           
    # return the thresholded image
    return image1
       

cpdef double[:, :,:] threshold_call(int T, float[:, :,:] image,float[:,:,:] img, double[:, :,:] image1):
    # set the variable extension types
    cdef int x, y, w, h, c ,t,max_x,max_y
    cdef double start,temp
    #cv2.imshow('newimage',image)
    # grab the image dimensions
    h = image.shape[0]
    w = image.shape[1]
    max_x = 0
    max_y = 0
    # loop over the image
    for y in range(0, h):
            for x in range(0,w):
                temp = (image[y][x][0] + image[y][x][1] + image[y][x][2])/3.0
                if(temp < T and temp > -1*T):
                    image1[y][x][0] = 0
                    image1[y][x][1] = 0
                    image1[y][x][2] = 0
                    image[y][x][0] = 0
                    image[y][x][1] = 0
                    image[y][x][2] = 0
                    
    for y in range(0, h):
            for x in range(0,w):
                temp = (image[y][x][0] + image[y][x][1] + image[y][x][2])/3.0
                if(temp > 0):
                    for t in range(x+1,w):
                        temp = (image[y][t][0] + image[y][t][1] + image[y][t][2])/3.0
                        if (temp<0):
                            break
                if ((t-x)>=150):
                    for c in range(x ,t+1):
                        image1[y][c][0]=255
                        image1[y][c][1]=255
                        image1[y][c][2]=255        
                    
    # return the thresholded image
    return image1  
cpdef  align(unsigned char[:, :,:] image1, unsigned short[:,:] depth,  double[:,:,:] final,double[:,:] new_depth):
    # set the variable extension types
    cdef double  w, h, z,u1 ,v1 ,u2 ,v2
    cdef int f1,f2,j,i,g1,g2
    cdef double start,temp
    cdef double c1u ,c1v ,f1u ,f1v ,c2u ,c2v ,f2u, f2v ,x2 ,y2, z2 ,x1 ,y1 ,z1,z11,max_x,max_y
    cdef double R[3][3] ,T[3][1]
    # grab the image dimensions
    h = image1.shape[0]
    w = image1.shape[1]

    R[0][:] = [ 0.99995735, -0.0017347 , -0.00907078]
    R[1][:] = [ 0.0017159 ,  0.99999637, -0.00207944]
    R[2][:] = [ 0.00907436,  0.00206379,  0.9999567]
    T[0][0] = 0.85816367e-02
    T[1][0] = -0.0460017e-02
    T[2][0] = 0.17192013e-02
    f2u = 527.97431353
    f2v = 523.22880991
    f1u = 601.9457306
    f1v = 596.05263911
    c2u = 312.66606295
    c2v = 255.35571034
    c1u = 322.50529377
    c1v = 230.96510472 
    i=0
    u1 = 0.0
    v1 = 0.0
    max_x = 0
    max_y = 0
    # loop over the image
    while(v1<h):
        u1 = 0.0
        while(u1<w):
            f1 = int(u1)
            f2 = int(v1)
            z1 = 1.0/(-0.00307 * depth[f2][f1] + 3.33)
            x1 =  z1*(u1-c1u)/f1u
            y1 =  z1*(v1-c1v)/f1v
            x2 = R[0][0]*x1 + R[0][1]*y1 + R[0][2]*z1 + T[0][0]
            y2 = R[1][0]*x1 + R[1][1]*y1 + R[1][2]*z1 + T[1][0]
            z2 = R[2][0]*x1 + R[2][1]*y1 + R[2][2]*z1 + T[2][0]
            u2 = ((x2*f2u)/z2+c2u) 
            v2 = ((y2*f2v)/z2+c2v) 
            g1 = int(u2)
            g2 = int(v2)
            
            if(g1 < 640 and g1>0 and g2 < 480 and g2 > 0):
                
                new_depth[g2][g1] = depth[f2][f1]
                final[g2][g1][0] = image1[g2][g1][0]
                final[g2][g1][1] = image1[g2][g1][1]
                final[g2][g1][2] = image1[g2][g1][2]
                
            u1+=1
        v1+=1
    
    # return the thresholded image
    return final,new_depth

cpdef double[:,:,:] segment(double[:, :, :] image1, double[:, :] depth,  double[:,:,:] final, double dmin, double dmax):
    # set the variable extension types
    cdef double dist
    cdef int x,y,w,h
    # grab the image dimensions
    h = image1.shape[0]
    w = image1.shape[1]
    for y in range(0, h):
        for x in range(0, w):
            dist = 1.0/(-0.00307*depth[y][x]+3.33)
            if(dist>dmin and dist<dmax):
                final[y][x][0] = image1[y][x][0]
                final[y][x][1] = image1[y][x][1]
                final[y][x][2] = image1[y][x][2]
    
    return final



cpdef coordinates_gui_to_kinect( int x, int y):
    cdef int p,q
    cdef double p1,q1
    p1 = x
    q1 = y
    p = int(470-((p1*350)/875))
    q = int(300-((q1*215)/520))
    return p,q   



cpdef coordinates_kinect_to_gui( int x, int y):
    cdef int p,q
    cdef double p1,q1
    p1 = 480 - x
    q1 = 300 - y
    p = int((p1/360)*875)
    q = int((q1/215)*520)
